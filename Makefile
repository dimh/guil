build:
	docker compose build

up:
	docker compose up

test:
	docker compose run web pytest
