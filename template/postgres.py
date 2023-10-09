import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres-test",
    user="postgres",
    password="123456",
)

cur = conn.cursor()

cur.execute("SELECT * FROM users WHERE name = 'John Doe'")

# Prepare the statement
stmt = cur.prepare("INSERT INTO users (name) VALUES (%s)")

# Execute the statement with parameters
stmt.execute(["John Doe"])

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()