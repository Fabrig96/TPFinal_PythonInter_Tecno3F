from .connection import Conneccion

class Productos():

    def __init__(self,nombre,tipo,proveedor,precio,cantidad):
       self.nombre = nombre
       self.tipo = tipo
       self.proveedor = proveedor
       self.precio = precio
       self.cantidad = cantidad


    def __str__(self):
        return f'Producto[{self.nombre},{self.tipo},{self.proveedor},{self.precio},{self.cantidad}]'

def guardar_producto(producto):
    conn = Conneccion()

    sql= f'''
        INSERT INTO Producto(nombre,id_tipo,id_proveedor,precio_venta,stock_actual)
        VALUES('{producto.nombre}','{producto.tipo}','{producto.proveedor}','{producto.precio}','{producto.cantidad}');
        '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass


def listar_prod():
    conn = Conneccion()
    listar_productos = []

    sql= f'''
        SELECT p.id_producto, p.nombre, t.nombre, pv.nombre, precio_venta, stock_actual FROM Producto as p
        INNER JOIN Proveedor as pv
        ON p.id_proveedor = pv.id_proveedor
        INNER JOIN Tipo as t
        ON p.id_tipo = t.id_tipo;
    '''
    try:
        conn.cursor.execute(sql)
        listar_productos = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_productos
    except:
        pass

def listar_tipos():
    conn = Conneccion()
    listar_tipos = []

    sql= f'''
        SELECT * FROM Tipo;
    '''
    try:
        conn.cursor.execute(sql)
        listar_tipos = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_tipos
    except:
        pass

def listar_proveedores():
    conn = Conneccion()
    listar_proveedores = []

    sql= f'''
        SELECT * FROM Proveedor;
    '''
    try:
        conn.cursor.execute(sql)
        listar_proveedores = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_proveedores
    except:
        pass


def editar_producto(producto, id):
    conn = Conneccion()

    sql= f'''
        UPDATE Producto
        SET nombre = '{producto.nombre}', id_tipo = '{producto.tipo}', id_proveedor = '{producto.proveedor}', precio_venta = '{producto.precio}', stock_actual = '{producto.cantidad}'
        WHERE id_producto = {id}
        ;
    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass


def buscar_producto(nombre):
    conn = Conneccion()

    sql = '''
        SELECT * FROM Producto
        WHERE nombre = ?
    '''
    try:
        conn.cursor.execute(sql, (nombre,))
        resultados = conn.cursor.fetchall()  # Obtener los resultados
        conn.cerrar_con()
        return resultados  # Retornar los resultados al llamador
    except:
        pass

def eliminar_producto(id):
    conn = Conneccion()

    sql= f'''
        DELETE FROM Producto
        WHERE id_producto = {id}
        ;
    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass

def reducir_stock(nombre,cantidad):
    conn = Conneccion()

    sql= f'''
        UPDATE Producto
        SET stock_actual = stock_actual - {cantidad}
        WHERE nombre = '{nombre}'
        ;
    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass


def reponer_stock(nombre,cantidad):
    conn = Conneccion()

    sql= f'''
        UPDATE Producto
        SET stock_actual = stock_actual + {cantidad}
        WHERE nombre = '{nombre}'
        ;
    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass