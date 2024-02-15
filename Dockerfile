# Dockerfile, Image, Container
FROM python:3.8-slim

COPY main.py .

RUN mkdir -p /home/data
RUN mkdir -p /home/output

COPY ./text-files/IF.txt /home/data/IF.txt
COPY ./text-files/Limerick-1.txt /home/data/Limerick-1.txt

CMD [ "python", "./main.py"]