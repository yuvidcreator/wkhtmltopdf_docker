


## 6. Running the Containers
### Development Mode
```bash
docker-compose up --build -d
```
### Stopping Services
```bash
docker-compose down
```
### Production Mode
For production, set `.env.production` and run:
```bash
docker-compose --env-file .env.production up --build -d
```

MYSQL_ROOT_PASSWORD=
MYSQL_ALLOW_EMPTY_PASSWORD=True
MYSQL_RANDOM_ROOT_PASSWORD=

# MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
# MYSQL_ALLOW_EMPTY_PASSWORD: ${MYSQL_ALLOW_EMPTY_PASSWORD}
# MYSQL_RANDOM_ROOT_PASSWORD: ${MYSQL_RANDOM_ROOT_PASSWORD}
MYSQL_DATABASE: ${MYSQL_DATABASE}
MYSQL_USER: ${MYSQL_USER}
MYSQL_PASSWORD: ${MYSQL_PASSWORD}