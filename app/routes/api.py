# 导入Flask类
from flask import jsonify, request
import time
import json
import requests
from ..models import dingtalk
from ..base import base

debug = False

@base.route('/api/healthcheck')
def healthcheck():
    return jsonify({'results': 'success'})


@base.route('/api/alert/<string:env>', methods=['POST'])
def alert_env(env):
    headers = {'Content-Type': 'application/json'}
    webhook = dingtalk.get_webhook(1, env)  # 主要模式有 0 ： 敏感字 1：# 敏感字 +加签 3：敏感字+加签+IP
    data = request.get_json()
    if debug:
        print(data)
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
                "content": "**服务名称**：{scope} \n**影响范围**：{name} \n**触发规则**：{rule_name} \n**开始时间**：{start_time} \n**告警内容**：{alarm_message} "
                           "\n**告警标签**：{tags}".format(**msg)
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


@base.route('/api/log_alert/<string:env>', methods=['POST'])
def log_alert(env):
    headers = {'Content-Type': 'application/json'}
    webhook = dingtalk.get_webhook(1,env)  # 主要模式有 0 ： 敏感字 1：# 敏感字 +加签 3：敏感字+加签+IP
    data = request.get_json()

    msg = {
        "name": data['name'],
        "hostip": data['hostip'],
        "msg": data['msg'],
        "appname": data['appname'],
        "start_time": data['timestamp']
    }
    send_msg_tpl = {
        "msgtype": "text",
        "text": {
            "content": "**告警名称**：{name} \n**应用名称**：{appname} \n**告警地址**：{hostip} \n**开始时间**：{start_time} \n**告警内容**：{msg} ".format(**msg)
        },
        "at": {
            "atUserIds": [
                "manager5345"
            ],
            "isAtAll": False
        }
    }
    requests.post(webhook, data=json.dumps(send_msg_tpl), headers=headers)
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
