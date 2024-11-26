import mysql.connector as conector
from mysql.connector import Error

def getConexionDB(host=None, user=None, password=None, database=None):
    try:
        conexion = conector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if conexion.is_connected():
            print(f'Conectado a la Base de Datos {database}')
            return conexion
    except Error as e:
        print(f'Error al conectarse a la Base de Datos {database}\n{e}')

def insertar_un_registro(conexion, tabla, datos):
    try:
        cursor = conexion.cursor()
        valores = tuple(datos.values())

        # Añade los la cantidad de paramtros que tiene la tupla
        parametros = ', '.join(['%s'] * len(valores))
        sql = f"INSERT INTO {tabla} VALUES({parametros})"
        cursor.execute(sql, (valores))
        conexion.commit()
    except Error as e:
        print(f'Error al ejecutar la consulta de inserción\n{e}')
        conexion.rollback()
    cursor.close()
    

def select(conexion, tabla, columnas, condicion=None, valores=()):
    try:
        cursor = conexion.cursor()
        parametros = columnas
        if type(columnas) is tuple:
            parametros = ', '.join([*columnas])
        sql = f"SELECT {parametros} FROM {tabla} WHERE {condicion}"
        cursor.execute(sql, (valores))
        resultados = cursor.fetchall()
        return resultados
    except Error as e:
        print(f'Error al ejecutar la consulta de la consulta\n{e}')
        conexion.rollback()
    cursor.close()

def update_un_registro(conexion, tabla, campo, condicion, valores=()):
    try:
        cursor = conexion.cursor()
        sql = f"UPDATE {tabla} SET {campo}=%s {condicion}"
        cursor.execute(sql, (valores))
        conexion.commit()
        return cursor.rowcount
    except Error as e:
        print(f'Error al ejecutar la consulta de actualización\n{e}')
        conexion.rollback()
    cursor.close()