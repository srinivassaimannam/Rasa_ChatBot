import pandas as pd
import pymysql

def DatabaseAPI(book_id, mobile, pick_up, destination):
    db=pymysql.connect(host="database-1.ciz6hepwqan2.us-east-2.rds.amazonaws.com",user="admin",password="password")
    cursor=db.cursor()
    query = "use rasa"
    cursor.execute(query)
    query = "insert into cab_book (bookid,address,dest,mobile) values (book_id,pick_up,destination,mobile) "
    cursor.execute(query)
    db.close()
    return


#def CancelAPI(book_id):
#    db=pymysql.connect(host="database-1.ciz6hepwqan2.us-east-2.rds.amazonaws.com",user="admin",password="password")
#   cursor=db.cursor()


    #query="delete from BOOKING_DETAILS where BOOK_ID={};".format(book_id)
    #statement=ibm_db.exec_immediate(connection,query)

#    db.close()
#    return


def DetailsAPI(book_id):
    db=pymysql.connect(host="database-1.ciz6hepwqan2.us-east-2.rds.amazonaws.com",user="admin",password="password")
    cursor=db.cursor()
    query = "use rasa"
    cursor.execute(query)
    query = "select * from cab_book"
    cursor.execute(query)
    res = cursor.fetchone()
     
    db.close()
    return result

if __name__=="__main__":
    #DatabaseAPI(94851,'7989078662','Maharashtra','Bombay')
    result=DetailsAPI(94851)
    print(result)
