import itchat, time
from itchat.content import *
import serve

itchat.auto_login(hotReload=True)

itchat.send('小l上线', toUserName='filehelper')

# 消息监听器，监听文本，共享位置，名片，通知类，分享链接
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    # msg.user.send('%s: %s' % (msg.type, msg.text))
    if msg.text == '你好' or msg.text == 'hello':
        msg.user.send('你好,我是诊疗星火,你可以像我咨询医疗相关的问题,或者输入"清除记忆"来清楚上一段问题')
    elif '清除记忆' in msg.text:
        serve.clear_memory()
        msg.user.send('好的记忆以清除')
    else:
        text = str(msg.text)
        res = serve.main(text)
        res = str(res)
        res = res.replace("/n","").replace("**","")
        print(res)
        msg.user.send(res)

# 消息监听，监听图片，文件，语音，视频
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)

# 监听好友请求
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('hello')

# 监听群聊中的文本信息
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg.isAt:   # 如果有人at当前微信
        msg.user.send(u'@%s\u2005I received: %s' % (
            msg.actualNickName, msg.text))

# itchat.auto_login(True)
itchat.run(True)