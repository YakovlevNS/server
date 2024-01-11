FROM ubuntu

RUN apt update
RUN apt install python3 python3-pip -y
RUN pip3 install flask

COPY . /server

CMD python3 /server/pyserver.py

