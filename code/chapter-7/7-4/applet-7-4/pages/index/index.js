//index.js
//获取应用实例
const app = getApp()
const cookieUtil = require('../../utils/cookie.js')

Page({
  data: {
    isAuthorized: false,
    constellationData: null,
    stockData: null,
    weatherData: null
  },
  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },

  updateData: function() {
    wx.showLoading({
      title: '加载中',
    })
    // 获取Cookie并构建请求头
    var that = this
    var header = {}
    var cookie = cookieUtil.getCookieFromStorage()
    header.Cookie = cookie
    // 获取星座运势数据
    wx.request({
      url: app.globalData.serverUrl + app.globalData.apiVersion + '/service/constellation',
      header: header,
      success: function(res) {
        var data = res.data.data
        that.setData({
          constellationData: data
        })
        wx.hideLoading()
      }
    })
    // 更新天气数据
    wx.request({
      url: app.globalData.serverUrl + app.globalData.apiVersion + '/service/weather',
      header: header,
      success(res) {
        console.log('weather_data')
        console.log(res.data)
        that.setData({
          weatherData: res.data.data
        })
        wx.hideLoading()
      }
    })
    // 更新股票数据
    wx.request({
      url: app.globalData.serverUrl + app.globalData.apiVersion + '/service/stock',
      header: header,
      success(res) {
        console.log(res.data.data)
        that.setData({
          stockData: res.data.data
        })
        wx.hideLoading()
      }
    })
  },
  onPullDownRefresh: function() {
    // 首先判断是否已经登录了
    var that = this
    var cookie = cookieUtil.getCookieFromStorage()
    var header = {}
    header.Cookie = cookie
    wx.request({
      url: app.globalData.serverUrl + '/api/v1.0/auth/status',
      header: header,
      success: function(res) {
        var data = res.data.data
        console.log(data)
        if (data.is_authorized == 1) {
          that.updateData()
          that.setData({
            isAuthorized: true
          })
        } else {
          that.setData({
            isAuthorized: false
          })
          wx.showToast({
            title: '请先授权登录',
          })
        }
      }
    })
  },

  onLoad: function() {
    if (app.globalData.userInfo) {
      this.setData({
        userInfo: app.globalData.userInfo,
        hasUserInfo: true
      })
    } else if (this.data.canIUse) {
      // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
      // 所以此处加入 callback 以防止这种情况
      app.userInfoReadyCallback = res => {
        this.setData({
          userInfo: res.userInfo,
          hasUserInfo: true
        })
      }
    } else {
      // 在没有 open-type=getUserInfo 版本的兼容处理
      wx.getUserInfo({
        success: res => {
          app.globalData.userInfo = res.userInfo
          this.setData({
            userInfo: res.userInfo,
            hasUserInfo: true
          })
        }
      })
    }
    var that = this
    // 获取与django授权得到的sessionid
    var cookie = cookieUtil.getCookieFromStorage()
    if (cookie) {
      var header = {}
      header.Cookie = cookie
      wx.request({
        url: app.globalData.serverUrl + '/api/v1.0/auth/status',
        header: header,
        success: function(res) {
          var data = res.data.data
          if (data.is_authorized == 1) {
            app.globalData.auth.isAuthorized = true
            that.setData({
              isAuthorized: true
            })
            console.log(that.data.isAuthorized)
            that.updateData()
          }
        }
      })
    }
  },
  getUserInfo: function(e) {
    console.log(e)
    app.globalData.userInfo = e.detail.userInfo
    this.setData({
      userInfo: e.detail.userInfo,
      hasUserInfo: true
    })
  }
})