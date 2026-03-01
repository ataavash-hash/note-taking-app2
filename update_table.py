from connection import cursor,connection
update_query = """
   UPDATE students SET age =? WHERE name=?;
"""
try:
   cursor.execute(update_query,[18,'john'])
   connection.commit()
   print(' Record updated successfully')
except Exception as e:
   print('Error updating  record:')
   print(e)