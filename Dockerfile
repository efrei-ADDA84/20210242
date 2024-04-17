
FROM python:alpine3.19


WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8081

ENV UVICORN_PORT=8081

CMD ["python3", "wrapper.py"]




