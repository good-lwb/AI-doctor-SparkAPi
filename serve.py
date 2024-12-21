import SparkApi
import time
#以下密钥信息从控制台获取
appid = "XXXXXXX"     #填写控制台中获取的 APPID 信息
api_secret = "XXXXXX"   #填写控制台中获取的 APISecret 信息
api_key ="XXXXXXX"    #填写控制台中获取的 APIKey 信息

#调用微调大模型时，设置为“patch”
domain = "XXXXXXX"

#云端环境的服务地址
Spark_url = "wss://maas-api.cn-huabei-1.xf-yun.com/v1.1/chat"  # 微调v1.5环境的地址
# Spark_url = "wss://spark-api-n.xf-yun.com/v3.1/chat"  # 微调v3.0环境的地址

text =[]
# length = 0
def getText(role,content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text

def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length

def checklen(text):
    while (getlength(text) > 8000):
        del text[0]
    return text

def clear_memory():
    text.clear()


# 重试机制：最多尝试 3 次
def main(input):
    question = checklen(getText("user", input))
    SparkApi.answer = ""  # 确保答复为空字符串
    print("星火:", end="")
    retries = 3  # 最大重试次数
    for attempt in range(retries):
        try:
            SparkApi.main(appid, api_key, api_secret, Spark_url, domain, question)
            if SparkApi.answer:  # 如果有答复，则退出
                break
        except Exception as e:
            print(f"请求失败，正在重试... (尝试 {attempt + 1}/{retries})")
            time.sleep(2)  # 等待 2 秒后重试
    getText("assistant", SparkApi.answer)
    return SparkApi.answer


if __name__ == '__main__':
    clear_memory()
    while(1):
        Input = input("\n" + "我:")
        main(Input)

