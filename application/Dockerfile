FROM ubuntu
COPY ./app.py app.py
RUN apt-get update
RUN apt-get install -y mysql-client python3-pip
RUN pip install mysql-connector-python Flask
