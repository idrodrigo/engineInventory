from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexionDB()
    query = """
        CREATE TABLE IF NOT EXISTS engines(
            id_engine INTEGER PRIMARY KEY AUTOINCREMENT,
            marca VARCHAR(100) NOT NULL,
            tipo VARCHARA(100) NOT NULL,
            hp INTEGER NOT NULL
        );
    """
    try:
        conexion.cursor.execute(query)
        conexion.cerrar_conexion()
        messagebox.showinfo('Database', 'Tabla creada con exito')
    except:
        messagebox.showwarning('Database', 'Error al crear la tabla')

def borrar_tabla():
    conexion = ConexionDB()
    try:
        conexion.cursor.execute("""
        DROP TABLE IF EXISTS engines;
        """)
        conexion.cerrar_conexion()
        messagebox.showinfo('Database', 'Tabla borrada con exito')
    except:
        messagebox.showerror('Database', 'Error al borrar la tabla')

class Engine:
    def __init__(self, marca, tipo, hp):
        self.id_engine = None
        self.marca = marca
        self.tipo = tipo
        self.hp = hp        
    
    def __str__(self):
        return f'Engine[marca={self.marca}, tipo={self.tipo}, hp={self.hp}]'
    
def guardar(engine):
    Conexion = ConexionDB()
    query = f"""
            INSERT INTO engines(marca, tipo, hp)
            VALUES('{engine.marca}', '{engine.tipo}', {engine.hp});
        """
    try:
            Conexion.cursor.execute(query)
            Conexion.cerrar_conexion()
            messagebox.showinfo('Database', 'Registro guardado con exito')
    except:
            messagebox.showerror('Database', 'Error al guardar el registro')

def consultar():
    conexion = ConexionDB()
    registros = []
    query = """
            SELECT * FROM engines;
        """
    try:
        conexion.cursor.execute(query)
        registros = conexion.cursor.fetchall()
        conexion.cerrar_conexion()
    except:
        messagebox.showwarning('Database', 'Error al consultar la tabla o tabla vacia')

    return registros    

def editar(engine, id_engine):

    conexion = ConexionDB()
    query = f"""
            UPDATE engines SET marca = '{engine.marca}', tipo = '{engine.tipo}', hp = {engine.hp}
            WHERE id_engine = {id_engine};
        """
    try:
        conexion.cursor.execute(query)
        conexion.cerrar_conexion()
        messagebox.showinfo('Database', 'Registro actualizado con exito')
    except:
        messagebox.showerror('Database', 'Error al actualizar el registro')

def eliminar(id_engine):
    conexion = ConexionDB()
    query = f"""
            DELETE FROM engines WHERE id_engine = {id_engine};
        """
    try:
        conexion.cursor.execute(query)
        conexion.cerrar_conexion()
        messagebox.showinfo('Database', 'Registro eliminado con exito')
    except:
        messagebox.showerror('Database', 'Error al eliminar el registro')