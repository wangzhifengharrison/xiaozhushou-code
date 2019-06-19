IT教程吧-www.itjc8.com 收集整理
# Jarvis

课程：《django+小程序开发个人助手》的课程代码。
Jarvis、贾维斯，漫威电影里面钢铁侠的人工智能助手，我们课程也是个人助手，故起名为Jarvis。

## 小程序开发注意事项
1. 使用代码的时候要将appid替换成自己的appid。

## Django开发注意事项
### 聚合API
[官网](https://www.juhe.cn/)

关于聚合API相关的使用因为与课程章节主题关系不大，在视频课程里面没有介绍太多。在这里简单介绍一下聚合API，聚合API的使用需要注意三个部分的内容，第一是API地址，第二是API的使用权限KEY，第三个是请求参数。使用方法可参照`thirdparty/juhe.py`文件相关的代码。

在这里，使用聚合API进行开发的时候同学们需要**将相关API的KEY替换成自己申请的API。**

以下是课程使用到的API的申请地址：
- [天气预报](https://www.juhe.cn/docs/api/id/39)
- [星座运势](https://www.juhe.cn/docs/api/id/58)
- [股票数据](https://www.juhe.cn/docs/api/id/21)

### 和风天气API
在依赖服务高可用的内容中，使用了和风天气的API，和风天气的官网为：[链接](https://www.heweather.com/) [文档](https://www.heweather.com/documents/api/)。可以参考老师提供的代码和文档，进行自己的开发。
