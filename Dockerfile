FROM python:3

RUN mkdir /home/test

COPY *test*.* /home/test

WORKDIR /home/test

CMD ["bash"]

