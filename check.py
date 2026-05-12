import psycopg2

try:
    connection = psycopg2.connect(
        dbname="library_db",
        user="postgres",
        password="Masters@2024",
        host="localhost",
        port="5432"
    )
    print("Connection successful!")
    connection.close()
except Exception as e:
    print(f"Error: {e}")

