from database import get_connection

try:
    conn = get_connection()
    print("Postgresql connected Successfully")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM CUSTOMERS LIMIT 5")

    records = cursor.fetchall()

    for record in records:
        print(record)


    cursor.close()
    conn.close()
    print("connection closed")

except Exception as e:
    print('Error',e)

    

    