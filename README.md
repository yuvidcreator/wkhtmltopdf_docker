


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