# pull official base image
FROM python:3.9.7-buster

ENV DJANGO_DB_NAME=ffs
ENV DJANGO_SU_NAME=admin
ENV DJANGO_SU_EMAIL=admin@my.company
ENV DJANGO_SU_PASSWORD=pass12345
#maintainer
LABEL Author="Francis Ngari"

# These two environment variables prevent __pycache__/ files.
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# RUN apt-get update \
#     && apt-get -y install libpq-dev gcc \
#     && pip install psycopg2
# Make a new directory to put our code in.
RUN mkdir /code

# Change the working directory. 
# Every command after this will be run from the /code directory.
WORKDIR /code

# Copy the requirements.txt file.
COPY ./requirements.txt /code/



# Upgrade pip
RUN pip install --upgrade pip

# Install the requirements.
RUN pip install -r requirements.txt



# COPY manage.py gunicorn-cfg.py requirements.txt .env ./
# COPY app app
# COPY authentication authentication
# COPY core core

# RUN pip install -r requirements.txt

# RUN python manage.py makemigrations
# 

COPY . /code/code

# EXPOSE 4301
# CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]



