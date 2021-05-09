start-cassandra:
	./lessons/data-modeling/apache-cassandra-4.0-beta4/bin/cassandra

stop-cassandra:
	pgrep -u tyler -f cassandra | xargs kill -9

# run-postgres:
# 	pg_ctl -D /usr/local/var/postgres start

# stop-postgres:
# 	pg_ctl -D /usr/local/var/postgres stop

run-postgres-in-docker:
	docker pull postgres
	docker run -p 5432:5432 -d \
	-e POSTGRES_PASSWORD="secret" \
	--name postgres \
	postgres
	docker exec -it postgres psql -U postgres -c "CREATE ROLE student LOGIN SUPERUSER PASSWORD 'student'"

load-pagila-data:
	docker exec -it postgres createdb -U postgres pagila
	cat ./lessons/data-warehouses/data/pagila-schema.sql | docker exec -i postgres psql -U postgres -d pagila
	cat ./lessons/data-warehouses/data/pagila-data.sql | docker exec -i postgres psql -U postgres -d pagila

clean-up-postgres:
	docker kill postgres
	docker container rm postgres


