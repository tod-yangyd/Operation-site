FROM 172.17.200.84:80/yyd/py-uwsgi:3.9.19-slim

# 如需完整镜像文件，选择Dockerfile_FULL

RUN useradd yyd -u 5000 -ms /bin/bash && echo "yyd:yyd" | chpasswd && adduser yyd sudo

USER yyd

ADD docker-entrypoint.sh /tmp/docker-entrypoint.sh


RUN cd /home/yyd && git clone https://gitee.com/tod-yangyd/Operation-site.git && cd Operation-site && \
    sudo pip install -r requirements.txt && \
    mv /tmp/docker-entrypoint.sh /home/yyd/docker-entrypoint.sh && chmod +x /home/yyd/docker-entrypoint.sh


WORKDIR /home/yyd/Operation-site
ENTRYPOINT ["sh", "docker-entrypoint.sh"]    