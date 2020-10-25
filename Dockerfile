FROM ubuntu:20.04

WORKDIR /home/test

RUN apt-get update && apt-get -y upgrade && apt-get -y install git python3
RUN git clone https://github.com/lotek93/test_task2 /home/test

CMD ["bash"]
