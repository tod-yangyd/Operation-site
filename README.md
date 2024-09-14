# 运维平台

------------------
## 接口

### 告警接口

1. /api/alert/&lt;env&gt;

接受来自***skywalking***以及***supervisord***的webhook数据，处理数据后推送给钉钉。


参数名 | 是否必填 | 默认值 | 说明
-----| ----- |----- |-----
env| 是 | null | production(不区分大小写)推送到dingtalkConfig，否则推送到dingtalkConfig_test

2. /api/log_alert/&lt;env&gt;

接受来自***logstash***的webhook数据,处理数据后推送给钉钉

参数名 | 是否必填 | 默认值  | 说明
-----| ----- |------|-----
env| 是 | null | production(不区分大小写)推送到dingtalkConfig，否则推送到dingtalkConfig_test

3. /api/comm

(失效，机器人outsourcing被封禁了)可以接受来自指定钉钉机器人的请求



------------------------
## 配置文件
修改config.py里钉钉的配置

----------------------
## 启动
### 本地启动
服务器启动建议用守护进程比如supervisord

```
uwsgi --ini start.ini 

```

### 容器启动
```
cd docker
# 构建容器
./build.sh
# 启动容器
./run.sh
```

### K8S启动
```
参考k8s_helm内容
```
