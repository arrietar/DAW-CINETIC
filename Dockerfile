ARG VERSION=3
FROM python:${VERSION}

#USER root
RUN mkdir -p /usr/app/cinetic_api
WORKDIR /usr/app/cinetic_api
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000

