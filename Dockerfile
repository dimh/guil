from python:3-alpine

RUN mkdir -p /opt/app
WORKDIR /opt/app
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY ./src/ /opt/app/

CMD [ "fastapi", "dev", "--host", "0.0.0.0", "main.py" ]