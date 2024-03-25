import psycopg2
from psycopg2 import Error

# Función para conectar a la base de datos PostgreSQL
def conectar_a_bd():
    try:
        # Conectarse a tu base de datos PostgreSQL
        conn = psycopg2.connect(
            host=config('PosgreSQL_HOST'),
            user=config('PosgreSQL_USER'),
            password=config('PosgreSQL_PASSWORD'),
            dbname=config('PosgreSQL_DB'),
            port=config('PosgreSQL_PORT'),
        )
        print("Conexión a la base de datos establecida correctamente")
        return conn
    except Error as e:
        print(f"Error al conectar a la base de datos PostgreSQL: {e}")
        return None

def ejecutar_consulta(conn, consulta):
    try:
        cursor = conn.cursor()
        
        # Ejecutar el comando SQL
        cursor.execute(consulta)
        
        # Obtener todas las filas
        filas = cursor.fetchall()
        # Cerrar la comunicación con la base de datos PostgreSQL
        cursor.close()

        return filas
            
    except Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        return None