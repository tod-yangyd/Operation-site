#FROM 172.17.200.84:80/yyd/py-uwsgi:3.9.19-slim
FROM 172.17.200.84:80/yyd/py-waitress:3.9.19-slim


# 如需完整镜像文件，选择Dockerfile_FULL


ADD docker-entrypoint.sh /tmp/docker-entrypoint.sh


RUN cd /opt && git clone https://gitee.com/tod-yangyd/Operation-site.git && cd Operation-site && \
    pip install -r requirements.txt && \
    mv /tmp/docker-entrypoint.sh /opt/Operation-site/docker-entrypoint.sh && chmod +x /opt/Operation-site/docker-entrypoint.sh


WORKDIR /opt/Operation-site
ENTRYPOINT ["sh", "docker-entrypoint.sh"]    