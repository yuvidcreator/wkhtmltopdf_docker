#! bin/bash

### Development Mode
# For development, set `.env.development` and run:
docker-compose up --build -d


### Production Mode
# For production, set `.env.production` and run:
docker-compose --env-file .env.production up --build -d


### Stopping Services
docker-compose down