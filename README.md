# data-engineer-nanodegree


## PostgresSQL Commands

* Create a user: 
```
sudo -u postgres psql
postgres=# create database mydb;
postgres=# create user myuser with encrypted password 'mypass';
postgres=# grant all privileges on database mydb to myuser;
```
* Create a super user: `createuser --interactive student` (nessesary for dropDB)
* Delete a user: `dropuser username -i`
* Database commands: `createdb`, `dropdb`




[More commands](https://www.a2hosting.ca/kb/developer-corner/postgresql/managing-postgresql-databases-and-users-from-the-command-line)





## Cassandra Commands


* [Instructions to download and run Cassandra](https://cassandra.apache.org/doc/latest/getting_started/installing.html)
