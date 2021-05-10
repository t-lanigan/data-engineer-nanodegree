# data-engineer-nanodegree


## PostgresSQL Commands

To start and set up locally (not in docker):

Start postgres:
```

pg_ctl -D /usr/local/var/postgres start (or stop)

```

* Create a user: 
```
sudo -u postgres psql
postgres=# create database studentdb;
postgres=# create user student with encrypted password 'student';
postgres=# grant all privileges on database studentdb to student;
```

Creating a super user is important for being able to drop tables
* `CREATE ROLE student LOGIN SUPERUSER PASSWORD 'student';` (using the psql tool)


This can also be done using the  createuser binaries
* Create a super user: `createuser --interactive student`
* Delete a user: `dropuser username -i`

Handy for creating and deleting databases.
* Database commands: `createdb`, `dropdb`


[More commands](https://www.a2hosting.ca/kb/developer-corner/postgresql/managing-postgresql-databases-and-users-from-the-command-line)



## Running Postgres with in Docker (preferred)


To Start it up:

`make run-postgres-in-docker`

To cleanit up:

`make clean-up-postgres`

to load pagila data:

`make load-pagila-data`



To connect with a postgres db running in docker:

by terminal:
`docker exec -it postgres psql -U postgres`

with Python:

```

DB_ENDPOINT = "0.0.0.0"
DB = 'pagila'
DB_USER = 'postgres'
DB_PASSWORD = 'secret'
DB_PORT = '5432'

conn_string = "postgresql://{}:{}@{}:{}/{}" \
                        .format(DB_USER, DB_PASSWORD, DB_ENDPOINT, DB_PORT, DB)

conn = psycopg2.connect(conn_string)
```

To connect to a database that is running in docker:

```
docker exec -it postgres psql -U student pagila
```


## Cassandra Commands


* [Instructions to download and run Cassandra](https://cassandra.apache.org/doc/latest/getting_started/installing.html)
* `make start-cassandra`
* `make stop-cassandra`
