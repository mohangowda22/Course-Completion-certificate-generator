import sqlite3 as sql
import add
import display
import printTopdf
user_name=None
password=None
cur=None
flag=None
def sql_conn():
    try:
        conn=sql.connect("course_db.db")
        cur=conn.cursor()
    except Exception as e:
        print(e)
        print("Error")
    query="create table if not exists admin(user_name char(100), pass char(20),primary key(user_name));"
    cur.execute(query)
sql_conn()
def displayChoice():
    print("\n"*10)
    c="""
                $
              $   $
            $       $
          $           $
        $    welcome    $
          $           $
            $       $
              $   $
                $

                """
    print(c)
    print()
    x="""*********************************
*       1: Add Details          *
*       2: Display              *
*       3: Print to pdf         *
*       0: Exit                 *
*********************************
"""
    print(x)

    ch=int(input("\nEnter your choice:"))
    if (ch==1):
        add.insertDetails()
        input()
        displayChoice()
    elif (ch==2):
        display.display()
        input()
        displayChoice()
    elif (ch==3):
        printTopdf.savePdf()
        displayChoice()
    elif (ch==0):
        exit()
    else:
        print("Please enter valid option")
        displayChoice()

def loginUser():
    flag=False
    conn=sql.connect("course_db.db")
    cur=conn.cursor()
    user_name=input("Uername:")
    password=input("Password:")
    if (user_name=="" and password==""):
        print("Please check username and password")
    else :
        query_1="select * from admin"
        cur.execute(query_1)
        rows=cur.fetchall()
        #op in tuple
        for row in rows:
            if (row[0]==user_name and  row[1]==password):
                flag=True
                #print("User valid")
                break
            else:
                flag=False

        if(flag==True):
            print("\n"*4)
            displayChoice()
        else:
            loginUser()

if __name__ == '__main__':
    main()
