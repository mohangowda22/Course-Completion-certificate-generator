import print_pdf
import sqlite3 as sql

def savePdf():
    conn=sql.connect("course_db.db")
    cur=conn.cursor()
    course_name=input("Entert the course name:")
    batch=input("Enter the batch id:")
    sqlQuery="select name from studentDetails where course='{}' and batch='{}'".format(course_name,batch)
    #print(sqlQuery)
    cur.execute(sqlQuery)
    data=cur.fetchall()
    print("\n")
    for i in data:
        print_pdf.printTopdf(i[0],course_name)
if __name__ == '__main__':
    main()
