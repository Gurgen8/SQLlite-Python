import sqlite3
connection=sqlite3.connect("mydb.db")
c=connection.cursor()

#  CRUD in Python



# get all information in db 
def get_all_info () :
    c.execute("SELECT * FROM users")
    for user in c.fetchall() :
        print(user)
        print("---------")


# insert-new-info
def insert_user (name,lastName,age,salory):
    c.execute('INSERT INTO users VALUES (?,?,?,?)',(name,lastName,age,salory)),
    connection.commit()


# update-info
def update_salory (name,salory) :
    c.execute("""UPDATE users SET salory =:salory
      WHERE name =:name
    """,{'name':name,'salory':salory})
    connection.commit()


# delete info
def delete_user (name,lastName) :
    c.execute("DELETE FROM users WHERE name = :name AND lastName= :lastName",{'name':name,'lastName':lastName})
    connection.commit()



connection.close()