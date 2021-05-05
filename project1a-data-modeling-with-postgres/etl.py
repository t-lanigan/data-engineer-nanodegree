import os
import glob
import psycopg2
import pandas as pd
from sql_queries import (song_table_insert,
                         artist_table_insert,
                         time_table_insert,
                         user_table_insert,
                         song_select,
                         songplay_table_insert)


def process_song_file(cur, filepath):
    """Processed one song file

    Args:
        cur (psycopg2 cursor): The cursor for access to the database
        filepath (str): The path to the file.
    """
    # open song file
    df = pd.read_json(filepath, lines=True)
    song_cols = ['song_id', 'title', 'artist_id','year', 'duration']

    # insert song record
    song_data = df[song_cols].values.tolist()[0]
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_cols = ['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']
    artist_data = df[artist_cols].values.tolist()[0]
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """Processed a single log file and adds it to the db.

    Args:
        cur (psycopg2 cursor): The cursor for access to the database
        filepath (str): The path the file.
    """
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df['page'] == "NextSong"]


    # Convert to dateTime
    df['ts'] = pd.to_datetime(df.ts, unit='ms')
    time_cols = ['ts','hour', 'day', 'week', 'month', 'year', 'weekday']
    df['hour'] = df['ts'].dt.hour
    df['day'] = df['ts'].dt.day
    df['week'] = df['ts'].dt.week
    df['month'] = df['ts'].dt.month
    df['year'] = df['ts'].dt.year
    df['weekday'] = df['ts'].dt.weekday

    time_df = df[time_cols]

    for _, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_cols = ['userId', 'firstName', 'lastName', 'gender', 'level']
    user_df = df[user_cols] 

    # insert user records
    for _, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for _, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record

        songplay_data = (row['ts'],
                        int(row['userId']),
                        row['level'],
                        songid,
                        artistid,
                        row['sessionId'],
                        row['location'],
                        row['userAgent'])

        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """A general function that processes data.

    Args:
        cur (psycopg2 cursor): The cursor for access to the database
        conn (psycopg2 cursor): A single connection
        filepath (str): The path the the file
        func (func): The function used to process the file.
    """
    # get all files matching extension from directory
    all_files = []
    for root, _, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()