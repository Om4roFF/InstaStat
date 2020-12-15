FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y python3-pip

RUN mkdir -p /home/user/
WORKDIR /home/user/

COPY . /home/user/

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD ["main.py"]

