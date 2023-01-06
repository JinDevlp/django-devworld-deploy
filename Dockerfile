FROM python:3.11.1-slim-buster
WORKDIR /app
COPY ./devworld ./

RUN pip install --upgrade pip --no-cache-dir

RUN pip install -r /app/requirements.txt --no-cache-dir

CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
# CMD ["gunicorn","portfoliowebsite.wsgi:application","--bind", "0.0.0.0:8000"]
