FROM python:3.9-buster
WORKDIR /app/django

RUN python -m pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

# EXPOSE 8000
CMD ["gunicorn","mysite.wsgi:application","--bind","0.0.0.0"]