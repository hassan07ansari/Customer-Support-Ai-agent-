import psycopg
from psycopg.rows import dict_row


def get_connection():
    connection = psycopg.connect(
        host = 'localhost',
        port = 5432,
        dbname = 'Customer_Support_db',
        user = 'postgres',
        password = '*******',
        row_factory= dict_row
    )

    return connection

def get_order_details(order_number):

    with get_connection() as conn:
        with conn.cursor() as cursor:

            cursor.execute("select * from orders where order_number=%s",(order_number,))

            order = cursor.fetchone()
            return order


if __name__ == "__main__":
    order = get_order_details("ORD-100001")
    print(order)