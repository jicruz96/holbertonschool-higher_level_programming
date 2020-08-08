#!/usr/bin/python3
""" lists all cities belonging to a state from db """

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
        QUERY = """
                    SELECT cities.name
                    FROM cities
                    LEFT JOIN states
                    ON cities.state_id = states.id
                    WHERE BINARY(states.name) = %(state)s
                """

        # Connect to database, execute QUERY
        db_connection = MySQLdb.connect(**args)
        cursor = db_connection.cursor()
        cursor.execute(QUERY, {"state": state})
        cities = cursor.fetchall()

        # Clean up
        cursor.close()
        db_connection.close()

        # Print result
        num_cities = len(cities)

        for i in range(num_cities):
            str = cities[i][0]
            if i == num_cities - 1:
                print(str)
            else:
                print(str + ', ', end='')
    except:
        pass
