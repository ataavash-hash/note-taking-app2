from connection import cursor,connection
insert_single_query = """
   INSERT INTO students
   (name,age,email,phone_number)
   VALUES(?,?,?,?);
"""
try:
   cursor.execute(insert_single_query,['aawaj',18,'aawaj@gmail.com','123-456'])
   connection.commit()
   print('single record inserted successfully ')
except Exception as e:
   print('Error inserting single record:')
   print(e)
