FROM python:3.7.4-stretch

LABEL maintainer="radzikowskikacper@gmail.com"
LABEL VERSION="0.1"

ADD . /server
ADD manage.py /server
WORKDIR /server

# RUN apt-get update && apt-get install -y postgresql-client
RUN groupadd -g 999 appuser && useradd -r -u 999 -g appuser appuser && chmod -R 777 /server

RUN pip install --upgrade pip && pip install -r requirements.txt
# RUN conda env create -f=environment.yml

USER appuser
# SHELL ["conda", "run", "-n", "speedlearning", "/bin/bash", "-c"]

EXPOSE 8000

# CMD ['gunicorn', 'speedlearning:asgi']
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "speedlearning.wsgi:application"]