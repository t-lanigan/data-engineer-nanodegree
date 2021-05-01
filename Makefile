start-cassandra:
	data-modeling/apache-cassandra-4.0-beta4/bin/cassandra

stop-cassandra:
	pgrep -u tyler -f cassandra | xargs kill -9


start-postgres:
	pg_ctl -D /usr/local/var/postgres start


