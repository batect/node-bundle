FROM docker:19.03.12-dind

RUN apk add --no-cache \
    bash=5.0.17-r0 \
    curl=7.69.1-r0 \
    openjdk11-jre-headless=11.0.7_p10-r1 \
    python3=3.8.5-r0

COPY entrypoint.sh /usr/local/bin/

ENV DOCKER_HOST=unix:///var/run/docker.sock
ENV DOCKER_TLS_CERTDIR=""

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
