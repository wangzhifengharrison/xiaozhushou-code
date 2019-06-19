const app = getApp()
const imageUrl = app.globalData.serverUrl + app.globalData.apiVersion + '/service/image'

Page({
  data: {
    // 需要上传的图片
    needUploadFiles: [],
    // 已下载的备份图片
    downloadedBackupedFiles: [],
  },

  // 选择图片上传
  chooseImage: function(e) {
    var that = this;
    wx.chooseImage({
      sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
      sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
      success: function(res) {
        // 返回选定照片的本地文件路径列表，tempFilePath可以作为img标签的src属性显示图片
        that.setData({
          needUploadFiles: that.data.needUploadFiles.concat(res.tempFilePaths)
        });
      }
    })
  },

  // 上传图片文件
  uploadFiles: function() {
    for (var i = 0; i < this.data.needUploadFiles.length; i ++){
      var filePath = this.data.needUploadFiles[i]
      wx.uploadFile({
        url: app.globalData.serverUrl + app.globalData.apiVersion + '/service/image',
        filePath: filePath,
        name: 'test',
        success: function(res){
          console.log(res)
        }
      })
    }
  },

  // 下载图片
  downloadFile: function (imgItem) {
    var that = this
    wx.downloadFile({
      url: app.globalData.serverUrl + app.globalData.apiVersion + '/service/image' + '?md5=' + '1ad78e3e075fd648882ba5299728369b',
      success: function(res){
        var tmpPath = res.tempFilePath
        var newDownloadedBackupedFiles = that.data.downloadedBackupedFiles
        newDownloadedBackupedFiles.push(tmpPath)
        that.setData({
          downloadedBackupedFiles: newDownloadedBackupedFiles
        })
      }
    })
  },

  // 删除图片
  deleteBackup: function(imgItem){
    wx.request({
      url: app.globalData.serverUrl + app.globalData.apiVersion + '/service/image' + '?md5=' + '1ad78e3e075fd648882ba5299728369b',
      method: 'DELETE',
      success: function(res){
        console.log(res.data)
        wx.showToast({
          title: '删除成功',
        })
      }
    })
  }
});