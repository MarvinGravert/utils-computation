FROM python:3.8-slim

WORKDIR /point_matching
ADD config ./config
COPY requirements requirements
COPY server.py .

ENTRYPOINT [ "python","-u","server.py" ]

