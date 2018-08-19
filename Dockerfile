FROM python:3.6-stretch

RUN easy_install pyzmq
RUN easy_install locustio

WORKDIR /test

EXPOSE 8089
EXPOSE 5557
EXPOSE 5558

ENTRYPOINT ["locust"]