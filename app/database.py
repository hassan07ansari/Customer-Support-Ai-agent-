import psycopg
from psycopg.rows import dict_row


def get_connection():
    connection = psycopg.connect(
        host = 'localhost',
        port = 5432,
        dbname = 'Customer_Support_db',
        user = 'postgres',
        password = 'Hassan07ansari@',
        row_factory= dict_row
    )

    return connection

def get_order_details(order_number):

    with get_connection() as conn:
        with conn.cursor() as cursor:

            cursor.execute("select * from orders where order_number=%s",(order_number,))

            order = cursor.fetchone()
            return order

def get_shipment_details(order_number):
    with get_connection() as conn:
        with conn.cursor() as cursor:

            cursor.execute(
                """
                SELECT 
                    s.carrier,
                    s.tracking_number,
                    s.status,
                    s.estimated_delivery_date,
                    s.last_known_location
                From orders o 
                join shipments s
                    ON o.order_id = s.order_id
                Where o.order_number = %s
                """,
                (order_number,) 
                 
            )

            shipment = cursor.fetchone()
            return shipment

if __name__ == "__main__":
    order = get_order_details("ORD-100001")
    print(order)