# Telegram profileless

This utility allows you to update your profile information, photo, name, surname at a specified interval.

# Requirements

- make ~4.3
- docker ~20.10
- docker-compose ~1.29

## Usage

### Copy env

```bash
cp .env.example .env
```

### Create Telegram Application

Follow the [instructions](https://core.telegram.org/api/obtaining_api_id#obtaining-api-id) of the telegrams

### Set env variables

Received ```api_id``` and ```api_hash``` set match ```TELEGRAM_PROFILELESS_API_ID``` and ```TELEGRAM_PROFILELESS_API_HASH``` in ```.env```

### Get session

```bash
make login
```

Insert the resulting string in ```TELEGRAM_PROFILELESS_API_SESSION``` in ```.env```

### Set other env variables

Provider | Source
--- | ---
art-fake | https://thisartworkdoesnotexist.com
cat-fake | https://thiscatdoesnotexist.com
human-fake | https://thispersondoesnotexist.com/image
random | random from above

```dotenv
TELEGRAM_PROFILELESS_PROVIDER=<provider>
```

Recommended minimum interval 60 seconds

```dotenv
TELEGRAM_PROFILELESS_INTERVAL=<interval>
```

### Run

```bash
make run
```

### Stop

```bash
make stop
```

### Down

Remove container

```bash
make down
```
