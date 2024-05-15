FROM python:3.11.3-slim-buster

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

RUN chmod u+x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
