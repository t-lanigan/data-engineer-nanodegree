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

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    curr = conn.cursor()
    
    run_validation(curr, conn)

    conn.close()


if __name__ == "__main__":
    main()