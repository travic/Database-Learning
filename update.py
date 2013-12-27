#!/usr/bin/python

import psycopg2
import sys

con = None

uID = 1
uPrice = 62300

try:

    con = psycopg2.connect(database='testdb', user='travic')
    
    cur = con.cursor()
 
    cur.execute("UPDATE cars SET price=%s WHERE id=%s", (uPrice, uID))
    con.commit()

    print "Number of rows updated: %d" % cur.rowcount

except psycopg2.DatabaseError, e:

    if con:
        con.rollback()


    print 'Error %s' % e
    sys.exit(1)
    
