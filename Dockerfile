FROM ubuntu:latest
LABEL authors="asupr"

ENTRYPOINT ["top", "-b"]