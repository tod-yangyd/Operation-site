# 导入Flask类
from flask import jsonify, request
import time
import json
import requests
from ..models import dingtalk
from ..base import base

@base.route('/api/healthcheck')
def healthcheck():
    return jsonify({'results': 'success'})


@base.route('/api/alert', methods=['POST'])
def alert():
    headers = {'Content-Type': 'application/json'}
    webhook = dingtalk.get_webhook(1,'Production')  # 主要模式有 0 ： 敏感字 1：# 敏感字 +加签 3：敏感字+加签+IP
    data = request.get_json()
    for i in data:
        msg = {
            "scope": i['scope'],
            "name": i['name'],
            "rule_name": i['ruleName'],
            "alarm_message": i['alarmMessage'],
            "start_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(i['startTime']) / 1000)),
            "tags": str(i['tags'])
        }
        send_msg_tpl = {
            "msgtype": "text",
            "text": {
                "content": "服务名称：{scope} \n影响范围：{name} \n触发规则：{rule_name} \n开始时间：{start_time} \n告警内容：{alarm_message} "
                           "\n告警标签：{tags}".format(**msg)
            },
            "at": {
                "atUserIds": [
                    "manager5345"
                ],
                "isAtAll": False
            }
        }
        requests.post(webhook, data=json.dumps(send_msg_tpl), headers=headers)
        time.sleep(0.2)
    return jsonify({'results': 'success'})




@base.route('/api/comm', methods=['POST'])
def comm():
    post_sign = request.headers.get("Sign")
    post_timestamp = request.headers.get("Timestamp")
    request_data_dict = json.loads(request.get_data())
    # 请求用户id
    post_userid = request_data_dict.get("senderStaffId")
    # 请求的群机器人webhook
    post_webhook = request_data_dict.get("sessionWebhook")
    # 判断请求是否超时
    if dingtalk.check_sign(post_sign,post_timestamp):
        # 这里拿到的就是你@机器人是输入的文本，可以根据输入文本进行一些if判断
        post_message = request_data_dict.get("text").get("content").strip()
        print("请求内容： ", post_message)
        # 判断请求内容，并返回相应的内容
        reply = dingtalk.check_post_message(post_message)
    else:
        reply ="请求超时"
        print ("请求超时")
    message_json, header = dingtalk.build_reply(post_userid, reply)
    # 发送请求
    info = requests.post(url=post_webhook, data=message_json, headers=header)
    print("请求返回： "+info.text)
    return jsonify({'results': 'success'})
