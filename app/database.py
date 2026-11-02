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

