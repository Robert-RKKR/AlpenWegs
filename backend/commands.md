## Backend - server configuration
### Python - virtual environment
**Create a new virtual environment:**
```bash
python3 -m venv venv
```
**Activate virtual environment:**
```bash
source venv/bin/activate
```

### GitHub - base account configuration
```bash
git config --global user.name <USERNAME>
git config --global github.token <TOKEN>
```

### Docker

**Run a new postgres container**
```bash
sudo docker run --name alpenwegs-postgres -e POSTGRES_USER=postgres_admin -e POSTGRES_DB=alpenwegs -e POSTGRES_PASSWORD='jt3g339d25rg0ea24' -p 5432:5432 -d postgres:latest
sudo docker run --name alpenwegs-redis -d -p 6379:6379 redis
# With network:
sudo docker network create alpenwegs_network
sudo docker run --name alpenwegs-postgres -e POSTGRES_USER=postgres_admin -e POSTGRES_DB=alpenwegs -e POSTGRES_PASSWORD='jt3g339d25rg0ea24' -p 5432:5432 --network alpenwegs_network -d postgres:latest
sudo docker run --name alpenwegs-redis --network alpenwegs_network  -d -p 6379:6379 redis
```
**Show all containers**
```bash
sudo docker ps -a
```
**Start / stop / remove container**
```bash
sudo docker start <NAME>
sudo docker stop <NAME>
sudo docker rm <NAME>
```
**Base commands**
```bash
sudo docker-compose build
sudo docker-compose up
sudo docker-compose run -rm app sh -c <NAME>
```
**Clean all containers**
```bash
docker system prune -a --volumes
```
**Restart and run docker compose**
```bash
docker-compose down
docker-compose up --build
```

## Backend - app configuration

### Back up - database
**Backup data:**
```bash
python manage.py dumpdata inventory connections.Template connections.Policy management.Administrator management.GlobalSettings > backup_data.json
```
**Load backup:**
```bash
python manage.py loaddata backup_data.json
```

### celery - commands
```bash
celery -A alpenwegs worker -Q collect_hosts -l INFO
celery -A alpenwegs worker --loglevel=info
celery -A alpenwegs beat --loglevel=info
```

### Pytest  - commands
```bash
export DJANGO_SETTINGS_MODULE=alpenwegs.settings
```

### Pip install commands
```bash
pip install django
pip install django-jazzmin
pip install django-json-widget
pip install django-jsonform
pip install django-channels
pip install channels_redis
pip install django-celery-beat
pip install psycopg2-binary
pip install colorama
pip install pytest-django
pip install djangorestframework
pip install django-filter
pip install drf-spectacular
pip install djangorestframework-extensions
pip install pyyaml
pip install cryptography
pip install xmltodict
pip install jinja2
pip install pdfkit
pip install matplotlib
pip install whitenoise
pip install psutil
pip install weasyprint
pip install mkdocs mkdocs-material
```

## Other information

### Open APIs
[All open APIs forum](https://rapidapi.com/collection/list-of-free-apis)

### Links to use
[Bootstrap tables 1] https://flatlogic.com/blog/bootstrap-table-guide-and-best-bootstrap-table-examples/
[Bootstrap tables 2] https://www.google.com/search?safe=active&sca_esv=d9880e105989b578&sxsrf=ADLYWIK8OQRQ6akCIjW_io_VJpaVSCCXaQ:1728916981450&q=best+Bootstrap+5+Tables&udm=2&fbs=AEQNm0Aa4sjWe7Rqy32pFwRj0UkWd8nbOJfsBGGB5IQQO6L3J_86uWOeqwdnV0yaSF-x2jopn8p7xL4A1Dm_DA2mNSwQLS8ggX90aupvmBKa3yzs191_zJWU73pwz19nrOVTbtdHtKQc1WdF5oo_Pyj_TZfl95KRn6NlIsWF0qMfWztX3LO1yDsv0yyJSJWNaFJlSeWegu-B&sa=X&ved=2ahUKEwjg4pnUjY6JAxXFgP0HHTx7JnIQtKgLegQIExAB&biw=2040&bih=990&dpr=1.25#vhid=Pp-Y5K-3SMJADM&vssid=mosaic
