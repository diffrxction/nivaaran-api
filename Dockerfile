FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /nivaaransite

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        python3-dev \
        libpq-dev \
        && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /nivaaransite/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /nivaaransite/

ENV DJANGO_SETTINGS_MODULE=nivaaransite.settings

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
