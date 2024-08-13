# 运维接口平台

## 接口
### /api/alert
可以推送告警给钉钉指定的webhook

### /api/comm（待完善）
可以接受来自指定钉钉机器人的请求

## 配置
修改config.py里钉钉的配置

## 启动
```
uwsgi --ini start.ini 

```
