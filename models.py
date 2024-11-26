"""
This file defines the database models
"""

from .common import db, Field
from pydal.validators import *
from .settings import DB_HOST, DB_USER, DB_USER_PASSWORD, DB_NAME, DB_CHARSET
from mysql.connector import Error
import mysql.connector as myconnect
### Define your table below
#
# db.define_table('thing', Field('name'))
#
## always commit your models to avoid problems later
#
# db.commit()
#

class Persistencia:
    def __init__(self):
        """
        Constructor para inicializar la conexión con la base de datos MySQL.
        """
        self.conn = None
        self.cursor = None

    def connect(self, host=DB_HOST, user=DB_USER, password=DB_USER_PASSWORD, database=DB_NAME, charset=DB_CHARSET):
        """Establece la conexión a la base de datos."""
        try:
            self.conn = myconnect(
                host=host,
                user=user,
                password=password,
                database=database,
                charset=charset
            )
            self.cursor = self.conn.cursor(dictionary=True)
            print(f"Conexión exitosa a la base de datos {database}")
        except Error as err:
            print(f"Error de conexión: {err}")

    def disconnect(self):
        """Cierra la conexión a la base de datos."""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("Conexión cerrada.")
        

    """
    Las columns son una lista con las columnas y conditions son un diccionario clave valor con la condicion del where
    """
    def select(self, columns=tuple, table='', conditions=dict(), operator=None):
        """Obtiene registros de la base de datos según condiciones."""
        self.connect()
        if len(columns) > 1: 
            columns = ', '.join(str(col) for col in columns)
        else:
            columns = columns[0]
            
        query = f"SELECT {columns} FROM {table}"
        if len(conditions) != 0:
            condition_str = [f"{k} = '{v}'" for k, v in conditions.items()]
            if len(conditions) == 1:
                operator = ""
                condition_str = operator.join(condition_str)
            elif bool(operator):
                condition_str = f" {operator} ".join(condition_str)
            query += f" WHERE {condition_str}"
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall() # Devuelve una lista de diccionarios
            if result == None or len(result) == 0:
                print(f'La tabla {table} no contiene ningún registro')
            self.disconnect()
            return result  
        except Error as err:
            print(f"Error al leer los registros: {err}")
            return []
            

    def insert(self, table, fields=[]):
        """Inserta un nuevo registro en la base de datos."""
        self.connect('localhost','admin')
        values = (', ' if len(fields) > 1 else '').join(str(v) for v in fields)
        query = f"INSERT INTO {table} VALUES ({values})"
        print(query)
        try:
            self.cursor.execute(query)
            self.conn.commit()
            print(f"Registro insertado en la tabla {table}.")
        except Error as err:
            print(f"Error al insertar el registro: {err}")
        self.disconnect()
    
    def update(self, table, set_values, operator, **conditions):
        """Actualiza registros en la base de datos según condiciones."""
        operator = ""
        if len(conditions) > 1:
            operator = f" {operator} "
            
        set_str = ", ".join([f"{k} = '{v}'" for k, v in set_values.items()])
        condition_str = operator.join([f"{k} = '{v}'" for k, v in conditions.items()])
        query = f"UPDATE {table} SET {set_str} WHERE {condition_str}"
        try:
            self.cursor.execute(query)
            self.conn.commit()
            print(f"Registros actualizados en la tabla {table}.")
        except Error as err:
            print(f"Error al actualizar los registros: {err}")


    def delete(self, table, operator, **conditions):
        """Elimina registros de la base de datos según condiciones."""
        operator = ""
        if len(conditions) > 1:
            operator = f" {operator} "
            
        condition_str = operator.join([f"{k} = '{v}'" for k, v in conditions.items()])
        query = f"DELETE FROM {table} WHERE {condition_str}"
        try:
            self.cursor.execute(query)
            self.conn.commit()
            print(f"Registros eliminados de la tabla {table}.")
        except Error as err:
            print(f"Error al eliminar los registros: {err}")


