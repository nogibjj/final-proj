FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip

# RUN apt-get update && apt-get install -y apt-utils && apt-get upgrade -y && apt-get install -y python3-pip

RUN pip install -r requirements.txt  --no-cache-dir

COPY spam.csv .

COPY my_util.py .

COPY app.py .

EXPOSE 80

# ENTRYPOINT [ "python3" ]

CMD ["gunicorn"  , "-b", "0.0.0.0:80", "app:app"]