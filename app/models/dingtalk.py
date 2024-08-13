
import hmac
import hashlib
import base64
import urllib.parse
import time
from config import dingtalkConfig
import json

URL = dingtalkConfig.URL
secret = dingtalkConfig.SECRET

def get_timestamp_sign(timestamp):
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc,
                         digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    print("timestamp: ", timestamp)
    print("sign:", sign)
    return sign


def get_signed_url():
    timestamp = str(round(time.time() * 1000))
    sign = get_timestamp_sign(timestamp)
    webhook = URL + "&timestamp=" + timestamp + "&sign=" + sign
    return webhook


def get_webhook(mode):
    if mode == 0:  # only 敏感字
        webhook = URL
    elif mode == 1 or mode == 2:  # 敏感字和加签 或 # 敏感字+加签+ip
        # 加签： https://oapi.dingtalk.com/robot/send?access_token=XXXXXX&timestamp=XXX&sign=XXX
        webhook = get_signed_url()
    else:
        webhook = ""
        print("error! mode:   ", mode, "  webhook :  ", webhook)
    return webhook

def check_sign(post_sign,post_timestamp ):
    timestamp = str(round(time.time() * 1000))
    sign = get_timestamp_sign(timestamp)
    # 验证是否来自钉钉的合法请求
    # 这里需要需要两个要求，请求的sign和响应的sign要一致，且当前时间和响应的时间不能大于10分钟
    if (abs(int(post_timestamp) - int(timestamp)) < 3600000 and post_sign == sign):
        return True
    else:
        return False

def build_reply(post_userid,reply):
    # 构建请求头部
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8",
    }
    # 构建请求数据
    tex = "监控报警TEST\n回复消息{0}".format(reply)
    data = {

        "msgtype": "text",
        "text": {
            "content": tex
        },
        "at": {

            "isAtAll": False,
            'atMobiles': ['18#########2'],
            "atUserIds": [post_userid],
        }

    }
    # 对请求的数据进行json封装
    message_json = json.dumps(data)
    return (message_json,header)

def check_post_message(post_message):
    if True:
        reply ='收到有效信息'
    return reply

