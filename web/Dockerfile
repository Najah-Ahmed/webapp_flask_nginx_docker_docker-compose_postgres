FROM python:3
ENV PYTHONUNBUFFERED 1 
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY . /app
CMD gunicorn --bind 0.0.0.0:5000 -w 3 app:app

