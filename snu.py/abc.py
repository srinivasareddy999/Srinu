import mysql.connector
con=mysql.connector.connect(user="root",host="localhost",password="Venna@1999",database="room")
cursor=con.cursor()
sql="insert into stadi(sid,sname,location), values=(%i,%s,%s)"
values=(101,'chinnaswamy','hyd')
cursor.execute(sql,values)
con.commit()
print('values are inserted successfully')