setup:
	docker-compose -f docker-compose.yaml build
	docker-compose -f docker-compose-test.yaml build

start-server:
	docker-compose -f docker-compose.yaml up -d

watch-logs:
	docker-compose -f docker-compose.yaml logs -f

stop-server:
	docker-compose down -v

clean-up:
	docker-compose down -v

start-test:
	docker-compose -f docker-compose-test.yaml run --rm tests
