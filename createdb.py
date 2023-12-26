import psycopg2

# admin_conn = psycopg2.connect(
#     host='localhost',
#     port=5432,
#     user='postgres',
#     password='12345678'
# )

# admin_cursor = admin_conn.cursor()

# admin_cursor.execute("CREATE USER ashot WITH PASSWORD '12345678'")
# admin_conn.commit()

# admin_cursor.close()
# admin_conn.close()

user_conn = psycopg2.connect(
    host='localhost',
    port=5432,
    user='postgres',
    password='12345678'
)

user_cursor = user_conn.cursor()
user_cursor.execute("COMMIT")

user_cursor.execute("CREATE DATABASE Moduldb OWNER ashot")

user_conn.commit()
user_cursor.close()
user_conn.close()
