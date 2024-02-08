import sqlite3

con = sqlite3.connect("funkos.db")
cur = con.cursor()

#Muestra todos los productos de la base de datos
def mostrarDatosProductos():
    # Ejecutar la consulta
    cur.execute("SELECT * FROM PRODUCTO")

    # Obtener todos los resultados
    resultados = cur.fetchall()

    return resultados

# Muestra solo un producto pasandole su id
def mostrarUnProducto(id_producto):
    # Ejecutar la consulta
    cur.execute("SELECT * FROM PRODUCTO WHERE ProductoID = ?", (id_producto,))
    
    # Obtener todos los resultados
    resultado = cur.fetchall()

    return resultado

# Modifica los datos del producto pasando su id
def modificarProducto(id_producto, nuevo_nombre, nuevo_precio, nueva_descripcion, nuevo_stock):
    # Ejecutar la consulta
    cur.execute("UPDATE PRODUCTO SET Nombre = ?, PrecioEUR = ?, Descripcion = ?, StockDisponible = ? WHERE ProductoID = ?", (nuevo_nombre, nuevo_precio, nueva_descripcion, nuevo_stock, id_producto))

    # Confirmar los cambios
    con.commit()

# Elimina un producto pasando su id
def eliminarProducto(id_producto):
    # Ejecutar la consulta
    cur.execute("DELETE FROM PRODUCTO WHERE ProductoID = ?", (id_producto,))

    # Confirmar los cambios
    con.commit()

# Añade un producto
def añadirProducto(nombre, precio, descripcion, stock):
    # Ejecutar la consulta 
    cur.execute("INSERT INTO PRODUCTO (Nombre, PrecioEUR, Descripcion, StockDisponible) VALUES (?, ?, ?, ?)", (nombre, precio, descripcion, stock))

    # Confirmar los cambios
    con.commit()