# Telegram fake avatar and name
The script at a certain interval changes in your account the avatar from a non-existent person and a random name.
## Install
```bash
cp .env.example .env
# don't forget to set variables in .env
touch telegram.session
docker-compose build --no-cache
docker-compose run amkearame python auth.py
# follow the instructions in the terminal
# go out with the container 
docker-compose up -d
```