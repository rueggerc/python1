
import sys
import psycopg2
from _sqlite3 import Row

def read1():
    conn = None
    try :
        conn = psycopg2.connect(host="localhost", database="rueggerllc", user="chris", password="dakota")
        print("Got Connection")
        cursor = conn.cursor()
        cursor.execute("select * from readings")
        resultSet = cursor.fetchall()
      
        for row in resultSet:
            print("sensor={} temperature={}".format(row[1],row[4]))
     
        cursor.close()
          
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if (conn != None):
            conn.close()
            print("Connection Closed")


def main():
    print("BEGIN")
    read1()

if __name__ == '__main__':
    main()