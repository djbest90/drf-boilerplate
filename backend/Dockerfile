FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
# COPY .env /app/.env
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/


# RUN python manage.py collectstatic --noinput
#RUN python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic
EXPOSE 8000

# RUN python manage.py collectstatic --noinput


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]