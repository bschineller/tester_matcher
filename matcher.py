import csv, sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        print("SQLLite version:", sqlite3.version)
        return conn
    except Error as e:
        print(e)
 
    return None


def execute_sql(conn, sql):
    """ execute sql statement given database connection
    :param conn: Connection object
    :param sql:  SQL statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)



def reload_testers(conn):

	execute_sql(conn, 'DROP TABLE IF EXISTS testers')

	sql_create_testers_table = """CREATE TABLE IF NOT EXISTS testers (
                                    testerid integer PRIMARY KEY,
                                    firstname text NOT NULL,
                                    lastname text NOT NULL,
                                    country text NOT NULL,
                                    lastlogin text NOT NULL
                                );"""

	execute_sql(conn, sql_create_testers_table)

	c = conn.cursor()

	csv_data = csv.reader(open('testers.csv'))
	next(csv_data, None)  # skip the headers

	for row in csv_data:
#		print(row)

		c.execute('INSERT INTO testers(testerid, firstname, lastname, country,lastlogin ) VALUES(?, ?, ?, ?, ?)', row)

	conn.commit()


def reload_devices(conn):

	execute_sql(conn, 'DROP TABLE IF EXISTS devices')

	sql_create_devices_table = """CREATE TABLE IF NOT EXISTS devices (
                                    deviceid integer PRIMARY KEY,
                                    description text NOT NULL
                                );"""

	execute_sql(conn, sql_create_devices_table)


	c = conn.cursor()

	csv_data = csv.reader(open('devices.csv'))
	next(csv_data, None)  # skip the headers

	for row in csv_data:
#		print(row)

		c.execute('INSERT INTO devices(deviceid, description ) VALUES(?, ?)', row)

	conn.commit()

def reload_tester_device(conn):

	execute_sql(conn, 'DROP TABLE IF EXISTS tester_device')

	sql_create_tester_device_table = """CREATE TABLE IF NOT EXISTS tester_device (
                                    testerid integer NOT NULL,
                                    deviceid integer NOT NULL,
                                    FOREIGN KEY (testerid) REFERENCES testers (testerid)
                                    FOREIGN KEY (deviceid) REFERENCES devices (deviceid)
                                );"""

	execute_sql(conn, sql_create_tester_device_table)


	c = conn.cursor()

	csv_data = csv.reader(open('tester_device.csv'))
	next(csv_data, None)  # skip the headers

	for row in csv_data:
#		print(row)

		c.execute('INSERT INTO tester_device(testerid, deviceid) VALUES(?, ?)', row)

	conn.commit()

def reload_bugs(conn):

	execute_sql(conn, 'DROP TABLE IF EXISTS bugs')

	sql_create_bugs_table = """CREATE TABLE IF NOT EXISTS bugs (
                                    bugid integer PRIMARY KEY,
                                    deviceid integer NOT NULL,
                                    testerid integer NOT NULL,
                                    FOREIGN KEY (testerid) REFERENCES testers (testerid)
                                    FOREIGN KEY (deviceid) REFERENCES devices (deviceid)
                                );"""

	execute_sql(conn, sql_create_bugs_table)

	c = conn.cursor()

	csv_data = csv.reader(open('bugs.csv'))
	next(csv_data, None)  # skip the headers

	for row in csv_data:
#		print(row)

		c.execute('INSERT INTO bugs(bugid, deviceid, testerid) VALUES(?, ?, ?)', row)

	conn.commit()


def get_matches(conn, countries, devices):

    try:
        cur = conn.cursor()
        sql_selectfrom = "select t.testerid, t.firstname, t.lastname, t.country, d.deviceid, d.description as devicetype, count(distinct bugid) as experience from testers as t left join tester_device as td on (t.testerid = td.testerid) left join devices as d on (td.deviceid = d.deviceid) left join bugs b on (b.deviceid = d.deviceid and b.testerid = t.testerid) "
        sql_group_order = " group by t.testerid, t.firstname, t.lastname, t.country, d.deviceid, d.description order by count(distinct bugid) desc;"

        if (countries.upper() == "ALL"):
        	country_clause = " (1=1)  "
        else:
        	country_clause = " t.country in (" + countries + ") "

        if (devices.upper() == "ALL"):
        	device_clause = " (1=1)  "
        else:
        	device_clause = " d.description in (" + devices + ") "


        where_clause = "WHERE " + country_clause + " AND " + device_clause
#        print(where_clause)	

        sql = sql_selectfrom + " " + where_clause + " " + sql_group_order

        cur.execute(sql)



    except Error as e:
        print(e)

    return cur

 
def main(db_file):


   # create a database connection
    conn = create_connection(db_file)
    if conn is not None:

        reload_testers(conn)
        reload_devices(conn)
        reload_tester_device(conn)
        reload_bugs(conn)


        cur = conn.cursor()
        cur.execute('SELECT DISTINCT country from testers order by country;')

       	print("Available countries are:")
       	rows = cur.fetchall()
       	for row in rows:
       		print(row)

       	countryCriteria = input("What Countries? ('ALL' or a comma-separated list of single-quoted country codes) : ")
        print("You entered: " + countryCriteria)

        cur.execute('SELECT DISTINCT description from devices order by description;')

       	print("Available devices are:")
       	rows = cur.fetchall()
       	for row in rows:
       		print(row)


       	deviceCriteria = input("What Devices? ('ALL' or a comma-separated list of single-quoted device names) : ")
        print("You entered: " + deviceCriteria)

        matchResultCur = get_matches(conn, countryCriteria, deviceCriteria)
        rows = matchResultCur.fetchall()
       	for row in rows:
       		print(row)
       


    else:
        print("Error! cannot create the database connection.")	



if __name__ == '__main__':
	main('applause.db')