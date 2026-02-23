from connection import cursor,connection
insert_multiple_query = """
   INSERT INTO students 
   (name,age,email,phone_number)
   VALUES(?,?,?,?);
"""
students_date = [
   ['john',22,'john@example.com','555-333'],
   ['mary',21,'mary@gmail.com','111-222'],
   ['bob',23,'bob@gmail.com','444-555']
]
try:
   cursor.executemany(insert_multiple_query,students_date)
   connection.commit()
   print('multiple record inserted successfully ')
except Exception as e:
   print('Error inserting multiple record:')
   print(e)