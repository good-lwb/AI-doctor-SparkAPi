# 欢迎使用诊疗星火

SparkApi.py为星火官方文档提供的访问服务

serve.py也是官方提供的请求服务，在这里你需要上传你自己的appid、api_secret、api_key、domain等应用信息，在代码中我做出来一定修改是他能够更好的兼容ichat

main-API.py为ichat框架

## 使用诊疗星火
首先安装需要的包：`pip install itchat-uos` 
`pip install spark-ai-python`

使用命令即可运行：
`python main-API.py`

运行之后会生成微信登陆码，即QR码，扫码即可将当前微信挂载成为诊疗星火的载体，当微信接收到消息是就会自动生成回复内容。
最终实现的效果图：
![2b04549da28be056204f89579b47e29](https://github.com/user-attachments/assets/b9140c6a-13d2-4e7d-a07a-25ec6aff46b8)

更多项目文件及使用流程请参考:
