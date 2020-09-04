FROM python:3.8.5-alpine

WORKDIR /src

COPY requirements.txt ./

RUN pip --no-cache-dir install -r requirements.txt

COPY app.py ./

EXPOSE 5000

ENTRYPOINT ["python", "app.py"]
