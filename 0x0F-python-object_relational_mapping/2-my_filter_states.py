#!/usr/bin/python3
""" lists state from db """

from sys import argv
import MySQLdb

if __name__ == "__main__":
    try:
        args = {
            "user": argv[1],
            "passwd": argv[2],
            "db": argv[3],
            "host": "localhost",  # This is default MySQLdb value
            "port": 3306        # This is default MySQLdb value
        }
        state = argv[4]
        QUERY = "SELECT * FROM states WHERE name = '{}' ORDER BY id"
        QUERY = QUERY.format(state)

        # Connect to database, execute QUERY
        db_connection = MySQLdb.connect(**args)
        cursor = db_connection.cursor()
        cursor.execute(QUERY)
        tuples = cursor.fetchall()

        # Clean up
        cursor.close()
        db_connection.close()

        # Print result
        for tuple in tuples:
            print(tuple)
    except:
        pass
