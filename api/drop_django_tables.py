import psycopg2
from psycopg2 import sql
import sys

def drop_django_tables():
    try:
        # Configuración de la conexión
        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres.wtkekvfbxtnqybcuvqmd',
            password='Robinzon984548931',
            host='aws-0-us-east-2.pooler.supabase.com',
            port='5432',
            sslmode='require'
        )
        conn.autocommit = True
        cursor = conn.cursor()
        
        print("Conexión exitosa a la base de datos")
        
        # Lista de tablas de Django a eliminar
        django_tables = [
            'auth_group',
            'auth_group_permissions',
            'auth_permission',
            'auth_user',
            'auth_user_groups',
            'auth_user_user_permissions',
            'django_admin_log',
            'django_content_type',
            'django_migrations',
            'django_session'
        ]
        
        # Deshabilitar restricciones de clave foránea temporalmente
        print("Deshabilitando restricciones de clave foránea...")
        cursor.execute("SET session_replication_role = 'replica';")
        
        # Eliminar cada tabla si existe
        for table in django_tables:
            try:
                drop_query = sql.SQL("DROP TABLE IF EXISTS {} CASCADE").format(
                    sql.Identifier(table)
                )
                cursor.execute(drop_query)
                print(f"Tabla {table} eliminada exitosamente")
            except Exception as e:
                print(f"Error al eliminar la tabla {table}: {e}")
        
        # Volver a habilitar restricciones de clave foránea
        print("Habilitando restricciones de clave foránea...")
        cursor.execute("SET session_replication_role = 'origin';")
        
        print("\n¡Proceso completado! Las tablas de Django han sido eliminadas.")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'conn' in locals():
            cursor.close()
            conn.close()
            print("Conexión cerrada")

if __name__ == "__main__":
    drop_django_tables()
