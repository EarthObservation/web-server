# Install for development

Install python requirements:

```
pip install -r requirements.txt
```

We suggest running PostgreSQL database in a Docker container in
development environment. Install Docker and docker-compose from
www.docker.com. Start PostgreSQL Docker container:

```
docker-compose up
```

Initialize Django project:

```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
