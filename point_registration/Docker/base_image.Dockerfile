
FROM python:3.8-slim

WORKDIR /point_matching

COPY requirements .

COPY config .

ENTRYPOINT [ "python","-u","server.py" ]
