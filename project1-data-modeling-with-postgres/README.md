# Project 1 - Data Modeling with Postgres

The first project of the Data Engineering Nanodegree by Udacity. The task is to design a star shaped databased for a startup called sparkify.

## Instructions

Follow these steps to run the project:

* To set up the database you need a instance of postgres running. See the [website](https://www.postgresql.org/download/) for instructions.
* Then a super user named `student` with password 'student' must be created. This is becuase some of the sripts required that databases be dropped. To do this run `createuser --interactive student` and select `y` for superuser.
* To set up the database run: `make reset-db`. This runs the `create_tables.py` script.
* To run the etl run: `make run-etl`. This runs the `etl.py` script.
* Run the jupyter notebook `test.ipynb` to see what is in the databased, or connect to it using the commandline tool `psql sparkifydb `.
* You can then run `\dt` to see the tables and a command like `SELECT * FROM artists;` to see whats in the tables.

## Schema

The data structure is designed in a star pattern including the following tables:

### Fact Table
* `songplays` - records in log data associated with song plays i.e. records with page NextSong
`songplay_id`, `start_time`, `user_id`, `level`, `song_id`, `artist_id`, `session_id`, `location`, `user_agent`

### Dimension Tables
* `users` - users in the app
`user_id`, `first_name`, `last_name`, `gender`, `level`
* `songs` - songs in music database
`song_id`, `title`, `artist_id`, `year`, `duration`
* `artists` - artists in music database
`artist_id`, `name`, `location`, `latitude`, `longitude`
* `time` - timestamps of records in songplays broken down into specific units
`start_time`, `hour`, `day`, `week`, `month`, `year`, `weekday`