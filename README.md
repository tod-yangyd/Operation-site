# 运维接口平台

## 接口
### /api/alert/<env>
可以推送告警给钉钉指定的webhook,Production推送到dingtalkConfig，否则推送到dingtalkConfig_test


### /api/comm（待完善）
可以接受来自指定钉钉机器人的请求

## 配置
修改config.py里钉钉的配置

## 启动
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
