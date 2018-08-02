import sqlite3 as sql
try:
    conn=sql.connect("course_db.db")
    #cur=conn.cursor()
except Exception as e:
    print(e)
    print("Error")
query="create table if not exists studentDetails(name char(50),batch char(10),course char(10),phone char(12));"
res=conn.execute(query)
def insertDetails():
    names=[]
    contactNumber=[]
    courseName=input("\nEnter the course name:")
    batch=input("Enter the batch code:")
    for i in range(int(input("\nEnter the number of student:"))):
        names.append(input("Enter the Full name:"))
        contactNumber.append(input("Enter the Phone Number:"))
        print()
    print("\n"*4)
    #print(names)
    #insert all name into db
    count=0
    for name in names:
        try:
            qvalues=tuple()
            sqlQuery="insert into studentDetails values(?,?,?,?)"
            qvalues=(name,batch,courseName,contactNumber[count])
            conn.execute(sqlQuery,qvalues)
            conn.commit()
            count+=1
        except Exception as e:
            print("")
if __name__ == '__main__':
    main()
