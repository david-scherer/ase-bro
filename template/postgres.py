import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="my_database",
    user="my_username",
    password="my_password",
)

cur = conn.cursor()

cur.execute("SELECT * FROM users WHERE name = 'John Doe'")

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()