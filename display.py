import sqlite3 as sql
try:
    conn=sql.connect("course_db.db")
    cur=conn.cursor()
except Exception as e:
    print(e)
    print("Error")
def display():
    course_name=input("Entert the course name:")
    batch=input("Enter the batch id:")

    sqlQuery="select name from studentDetails where course='{}' and batch='{}'".format(course_name,batch)
    #print(sqlQuery)
    cur.execute(sqlQuery)
    data=cur.fetchall()
    print("\nList of the students who attended {} course in {} batch:".format(course_name,batch))
    print("\n")
    for i in data:
        print(i[0])
if __name__ == '__main__':
    main()
