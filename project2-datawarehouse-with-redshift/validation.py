import configparser
import psycopg2
from sql_queries import validation_queries


def run_validation(curr, conn):
    """Run the validation queries

    Args:
        curr (psycopg2 cursor): [description]
        conn (psycopg2 connection to db): [description]
    """
    for query in validation_queries:
        print('Query: {}'.format(query))
        curr.execute(query)
        res = curr.fetchone()
        [print("   ", row) for row in res]


def main():
    """The main for running the validation
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    host = config['CLUSTER']['HOST']
    db_name = config['CLUSTER']['DB_NAME']
    user = config['CLUSTER']['DB_USER']
    password = config['CLUSTER']['DB_PASSWORD']
    port = config['CLUSTER']['DB_PORT']

    conn = psycopg2.connect(f"host={host} dbname={db_name} user={user} password={password} port={port}")
    curr = conn.cursor()
    
    run_validation(curr, conn)

    conn.close()


if __name__ == "__main__":
    main()