FROM python:3.9.19-slim

# solve please select the geographic area in which you live problems
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Shanghai

ADD sources.list /etc/apt/sources.list
ADD pip.conf /root/.pip/pip.conf
ADD docker-entrypoint.sh /tmp/docker-entrypoint.sh

RUN apt update && apt install -y git && \
    apt install -y gcc && apt install -y python3-dev &&  \
    pip install uwsgi && \
    apt clean

RUN cd /opt && git clone https://gitee.com/tod-yangyd/Operation-site.git && cd Operation-site && \
    pip install -r requirements.txt && \
    mv /tmp/docker-entrypoint.sh /opt/Operation-site/docker-entrypoint.sh && chmod +x /opt/Operation-site/docker-entrypoint.sh 


WORKDIR /opt/Operation-site
ENTRYPOINT ["sh", "docker-entrypoint.sh"]    