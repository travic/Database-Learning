#!/usr/bin/python


import psycopg2
import psycopg2.extras
import sys

con = None

try:

    con = psycopg2.connect(database='testdb', user='travic')
 
    cursor = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT * FROM cars")

    rows = cursor.fetchall()

    for row in rows:
        print "%s %s %s" % (row["id"], row["name"], row["price"])


except psycopg2.DatabaseError, e:
    print 'Error %s' % e
    sys.exit(1)


finally:

   if con:
       con.close()
