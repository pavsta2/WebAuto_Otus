FROM python:3.11.13-alpine3.22

USER root

RUN mkdir -p /root/WebAuto_Otus

WORKDIR /root/WebAuto_Otus

COPY . /root/WebAuto_Otus

RUN pip install --no-cache uv && \
    uv venv && \
    . .venv/bin/activate && \
    uv pip install -r requirements.txt

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]