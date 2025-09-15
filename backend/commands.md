# Backend Commands

1. [Virtual environment](#virtual-environment)  
   1.1 [Create a new virtual environment](#create-a-new-virtual-environment)  
   1.2 [Activate virtual environment](#activate-virtual-environment)  
2. [GitHub](#github)  
   2.1 [Configure Global Identity](#configure-global-identity)  
   2.2 [Check Configuration](#check-configuration)  
   2.3 [Repository Basics](#repository-basics)  
   2.4 [Branch Management](#branch-management)  
   2.5 [Remote Management](#remote-management)  
   2.6 [Staging & Committing](#staging--committing)  
   2.7 [Pushing & Pulling](#pushing--pulling)  
   2.8 [Safety & Cleanup](#safety--cleanup)  
3. [Docker](#docker)  
   3.1 [Run a new postgres container](#run-a-new-postgres-container)  
   3.2 [Show all containers](#show-all-containers)  
   3.3 [Start / stop / remove container](#start--stop--remove-container)  
   3.4 [Base commands](#base-commands)  
   3.5 [Clean all containers](#clean-all-containers)  
   3.6 [Restart and run docker compose](#restart-and-run-docker-compose)  
4. [Backend](#backend)  
   4.1 [Back up Database](#back-up-database)
   4.2 [Celery](#celery)  
   4.3 [Pytest](#pytest)  
   4.4 [Pip install commands](#pip-install-commands)  

## Virtual environment

### Create a new virtual environment

```bash
python3 -m venv venv
```

### Activate virtual environment

```bash
source venv/bin/activate
```

## GitHub

### Configure Global Identity

```bash
git config --global user.name "<USERNAME>"   # Set global username for all repos
git config --global user.email "<EMAIL>"     # Set global email for all repos

# Or using token:

git config --global github.token <TOKEN>     # Store GitHub personal access token
```

### Check Configuration

```bash
git config --list        # Show all Git config settings
git config user.name     # Show configured Git username
git config user.email    # Show configured Git email
```

### Repository Basics

```bash
git init                                    # Initialize a new Git repository
git clone <URL>                             # Clone a remote repo locally
git status                                  # Show working directory and staging state
git log --oneline --graph --decorate --all  # Compact history with branch graph
```

### Branch Management

```bash
git branch                   # List all branches
git branch <name>            # Create a new branch
git checkout <name>          # Switch to an existing branch
git checkout -b <name>       # Create and switch to a new branch
git merge <branch>           # Merge another branch into current one
git branch -d <name>         # Delete branch (safe, only if merged)
git branch -D <name>         # Delete branch forcefully
```

### Remote Management

```bash
git remote -v                      # Show all remote repositories
git remote add origin <URL>        # Add a new remote named 'origin'
git remote set-url origin <URL>    # Change remote URL for 'origin'
```

### Staging & Committing

```bash
git add <file>               # Stage a single file
git add .                    # Stage all modified/new files
git commit -m "Message"      # Commit staged changes with a message
git commit --amend           # Modify the last commit (message or content)
```

### Pushing & Pulling

```bash
git push origin main         # Push current branch to 'main'
git push -u origin main      # Push and set upstream tracking
git pull                     # Fetch + merge changes from remote
git fetch                    # Fetch changes without merging
git pull --rebase            # Fetch + reapply commits on top of remote
```

### Safety & Cleanup

```bash
git stash                # Save uncommitted changes temporarily
git stash pop            # Restore latest stashed changes
git clean -fd            # Remove untracked files and directories
git reset --hard HEAD    # Reset working dir to last commit (dangerous!)
```

## Docker

### Run a new postgres container

```bash
sudo docker run --name alpenwegs-postgres -e POSTGRES_USER=postgres_admin -e POSTGRES_DB=alpenwegs -e POSTGRES_PASSWORD='jt3g339d25rg0ea24' -p 5432:5432 -d postgres:latest
sudo docker run --name alpenwegs-redis -d -p 6379:6379 redis

# With network:

sudo docker network create alpenwegs_network
sudo docker run --name alpenwegs-postgres -e POSTGRES_USER=postgres_admin -e POSTGRES_DB=alpenwegs -e POSTGRES_PASSWORD='jt3g339d25rg0ea24' -p 5432:5432 --network alpenwegs_network -d postgres:latest
sudo docker run --name alpenwegs-redis --network alpenwegs_network  -d -p 6379:6379 redis
```

### Show all containers

```bash
sudo docker ps -a
```

### Start / stop / remove container

```bash
sudo docker start <NAME>   # Start an existing container
sudo docker stop <NAME>    # Stop a running container
sudo docker rm <NAME>      # Remove a stopped container
```

### Base commands

```bash
sudo docker-compose build                        # Build or rebuild services from docker-compose.yml
sudo docker-compose up                           # Start containers defined in docker-compose.yml
sudo docker-compose run --rm app sh -c <CMD>     # Run one-off command in 'app' container and remove it after
```

### Clean all containers

```bash
docker system prune -a --volumes   # Remove all stopped containers, images, networks, and volumes
```

### Restart and run docker compose

```bash
docker-compose down          # Stop and remove all running containers defined in compose
docker-compose up --build    # Build images and start containers again
```

## Backend

### Back up Database

**Backup data:**

```bash
python manage.py dumpdata > backup_data.json
python manage.py dumpdata inventory connections.Template connections.Policy management.Administrator management.GlobalSettings > backup_data.json
```

**Load backup:**

```bash
python manage.py loaddata backup_data.json
```

### Celery

```bash
celery -A alpenwegs worker -Q collect_hosts -l INFO
celery -A alpenwegs worker --loglevel=info
celery -A alpenwegs beat --loglevel=info
```

### Pytest

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
