from app.db import get_connection

conn = get_connection()
cursor = conn.cursor()

print(cursor)

cursor.execute("Select * from Customers")

#data = [row for row in cursor.fetchall()]

for row in cursor.fetchall():
    # print(row[1])
    print(row)
    data = row
    print(type(data))

conn.close()

# print(data)
# print(type(data))