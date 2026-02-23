from connection import cursor
alter_table_query = """
    ALTER TABLE users ADD COLUMN phone_number TEXT;
"""
try:
   cursor.execute(alter_table_query)
   print('Table altered successfully')
except Exception as e:
   print('Error creating table:')
   print(e)
