FROM ubuntu

RUN apt-get update -y && apt-get install -y python-pip python-dev build-essential

COPY ./source/python /python
WORKDIR /python
RUN pip install -r requirements.txt

CMD python /python/d4d/flask_app.py
