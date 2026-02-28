from connection import cursor
select_all_query = """
  SELECT* FROM students;
"""
try:
   cursor.execute(select_all_query)
   all_students = cursor.fetchall()
   print('all students: ')
   for student in all_students:
       print(student)
except Exception as e:
   print('Error selecting all records:')
   print(e)
