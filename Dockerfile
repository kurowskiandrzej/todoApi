FROM python:3.10-rc-buster

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

COPY ./requirements.txt /requirements.txt
WORKDIR /app

RUN pip install -r /app/requirements.txt

COPY . /app

ENTRYPOINT ["python3"]

CMD ["app.py"]