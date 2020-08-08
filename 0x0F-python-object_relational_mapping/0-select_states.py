#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """

from sys import argv

if __name__ == "__main__" and len(argv) is 4:

    import MySQLdb

    args = {
        "user": argv[1],
        "passwd": argv[2],
        "db": argv[3],
        "host": "localhost",  # This is default MySQLdb value
        "port": 3306        # This is default MySQLdb value
    }
    QUERY = "SELECT * FROM states ORDER BY states.id"

    # Connect to database, execute QUERY
    try:
        db_connection = MySQLdb.connect(**args)
        cursor = db_connection.cursor()
        cursor.execute(QUERY)

        # Print result
        tuples = cursor.fetchall()
        for tuple in tuples:
            print(tuple)

        # Clean up
        cursor.close()
        db_connection.close()
    except:
        pass
