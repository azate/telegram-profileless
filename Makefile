login:
	docker-compose build
	docker-compose run get_session

run:
	docker-compose up -d --build updater

stop:
	docker-compose stop updater

down:
	docker-compose down --rmi all --remove-orphans
