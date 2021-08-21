login:
	docker-compose build
	docker-compose run get_session

run:
	docker-compose build
	docker-compose run updater

stop:
	docker-compose stop updater

down:
	docker-compose down --rmi all --remove-orphans
