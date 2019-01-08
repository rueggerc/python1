
import sys
import pypyodbc

def read1():
    conn = None
    try :
        conn = pypyodbc.connect("Driver={SQL Server Native Client 11.0};"
                                "Server=captain;"
                                "Database=rueggerllc;"
                                "uid=sa;pwd=Dakota123%")
        print("Got Connection")
        cursor = conn.cursor()
        cursor.execute("select * from readings")
        resultSet = cursor.fetchall()
      
        for row in resultSet:
            print("sensor={} temperature={}".format(row[1],row[4]))
     
        cursor.close()
          
        
    except (Exception, pypyodbc.DatabaseError) as error:
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