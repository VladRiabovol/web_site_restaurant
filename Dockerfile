FROM python:3.8

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r /app/requirements.txt

COPY . .


#FROM python:3.8
#
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#
#WORKDIR /src
#
#COPY requirements.txt /src/requirements.txt
#RUN pip install -r /src/requirements.txt
#
#COPY . /src/

#EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

