import psycopg

def get_connection():
    connection = psycopg.connect(
        host = 'localhost',
        port = 5432,
        dbname = 'Customer_Support_db',
        user = 'postgres',
        password = 'Hassan07ansari@'
    )

    return connection

def get_order_details(order_number):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("select * from orders where order_number=%s",(order_number,))

    order = cursor.fetchone()

    cursor.close()

    conn.close()

    return order
