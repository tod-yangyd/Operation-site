
from flask import jsonify, request
import time
import json
import requests
from ..models import dingtalk
from ..base import base

@base.route('/test_api/alert', methods=['POST'])
def test_alert():
    headers = {'Content-Type': 'application/json'}
    webhook = dingtalk.get_webhook(1,'test')  # 主要模式有 0 ： 敏感字 1：# 敏感字 +加签 3：敏感字+加签+IP
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


@base.route('/test_api/alert/<string:env>', methods=['POST'])
def test_alert_env(env):
    headers = {'Content-Type': 'application/json'}
    webhook = dingtalk.get_webhook(1,env)  # 主要模式有 0 ： 敏感字 1：# 敏感字 +加签 3：敏感字+加签+IP
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