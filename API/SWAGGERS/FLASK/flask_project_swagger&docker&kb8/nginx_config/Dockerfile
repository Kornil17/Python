FROM ubuntu:latest
LABEL authors="d-kornilov"
RUN apt update
RUN   apt install python3 python3-pip -y
RUN pip3 install flask
RUN pip3 install flask_restful
RUN pip3 install flask_swagger_ui
COPY . /FLASK_SWAGGER
CMD python3 /FLASK_SWAGGER/swagger_flask.py
