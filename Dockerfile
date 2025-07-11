FROM python:3.12-alpine

COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt
#RUN pip install --upgrade pip

COPY src /src

CMD [python /src/app.py,"start"]