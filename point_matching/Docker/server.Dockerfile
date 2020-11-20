FROM python:3.8-slim

WORKDIR /point_matching

COPY server.py .

ENTRYPOINT [ "python","-u","server.py" ]

