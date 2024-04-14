
FROM python:alpine3.19


WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8081

ENV UVICORN_PORT=8081

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]




