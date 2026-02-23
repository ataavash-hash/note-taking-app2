from connection import cursor,connection
delete_query = """
   DELETE FROM students WHERE name =?;
"""
try:
   cursor.execute(delete_query,['bob'])
   connection.commit()
   print('record deleted  successfully ')
except Exception as e:
   print('Error deleting record:')
   print(e)
