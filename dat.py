import sqlite3 as sq
conn = sq.connect('dat.db')
cursor=conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS maildat( 
                U_Name text PRIMARY KEY,
                email_id text,
                password text);''')

cursor.execute('''INSERT INTO maildat VALUES
('USER','USEREMAIL@gmail.com','YOUR_PASSWORD')''')
#a=cursor.execute('''SELECT * FROM maildat;''')

a=str(cursor.fetchone())
b=str(a)
print(a)
print(type(a))
print(b)
# cursor.execute('DELETE FROM maildat')


conn.commit()


conn.close()
