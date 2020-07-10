build:
	 docker build -t python:3.7-alpine .
run:
	docker run --publish 8100:8100 --detach --name dynamo-api python:3.7-alpine