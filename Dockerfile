FROM python:latest

WORKDIR /app

COPY . .
RUN pip install -r requirement.txt

ENTRYPOINT ["sh", "-c", "python app.py"]

