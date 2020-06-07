
FROM python:3.7

WORKDIR /app
COPY . .

RUN pip install -r requirement.txt

ENTRYPOINT ["sh", "-c", "python main.py"]
