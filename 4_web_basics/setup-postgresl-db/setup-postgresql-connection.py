# pip install psycopg2
# pip install psycopg2-binary

import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="1123QwER"
)

# execute postgresql queries from Python
cur = conn.cursor()
cur.execute('''
            SELECT * 
            FROM pet_hotel.pet_owner
            ''')

for row in cur.fetchall():
    print(row)

# don't forget to close connection
cur.close()
