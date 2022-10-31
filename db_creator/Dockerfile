FROM ubuntu
COPY ./creator.py creator.py
RUN apt-get update
RUN apt-get install -y mysql-client python3-pip
RUN pip install mysql-connector-python pandas
