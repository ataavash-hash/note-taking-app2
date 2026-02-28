from connection import cursor
rename_table_query = """
    ALTER TABLE  users RENAME TO students;
"""
try:
   cursor.execute(rename_table_query)
   print('Table rename successfully')
except Exception as e:
   print('Error renaming table:')
   print(e)
