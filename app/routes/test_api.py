
from flask import jsonify, request
import time
import json
import requests
from ..models import dingtalk
from ..base import base

debug = True

@base.route('/test_api/log_alert/<string:env>', methods=['POST'])
def log_alert(env):
    headers = {'Content-Type': 'application/json'}
    webhook = dingtalk.get_webhook(1,env)  # 主要模式有 0 ： 敏感字 1：# 敏感字 +加签 3：敏感字+加签+IP
    data = request.get_json()
    if debug:
        print(data)

    msg = {
        "name": data['name'],
        "hostip": data['hostip'],
        "msg": data['msg'],
        "start_time": data['timestamp']
    }
    send_msg_tpl = {
        "msgtype": "text",
        "text": {
            "content": "告警名称：{name} \n告警地址：{hostip} \n开始时间：{start_time} \n告警内容：{msg} ".format(**msg)
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