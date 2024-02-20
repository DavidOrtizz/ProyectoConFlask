import json
import sqlite3

def listaProducto():
    
    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM PRODUCTO")

    resultados = cur.fetchall()

    con.close()

    return mapearProductos(resultados)

# Añade un producto
def añadirProducto(nombre, precio, descripcion, stock):
    con = sqlite3.connect("funkos.db")
    cur = con.cursor()
    # Ejecutar la consulta 
    cur.execute("INSERT INTO PRODUCTO (Nombre, PrecioEUR, Descripcion, StockDisponible) VALUES (?, ?, ?, ?)", (nombre, precio, descripcion, stock))

    # Confirmar los cambios
    con.commit()

    con.close()

    # Elimina un producto pasando su id
def eliminarProducto(id_producto):
    con = sqlite3.connect("funkos.db")
    cur = con.cursor()
    # Ejecutar la consulta
    cur.execute("DELETE FROM PRODUCTO WHERE ProductoID = ?", (str(id_producto),))

    # Confirmar los cambios
    con.commit()

    con.close()

# Muestra solo un producto pasandole su id
def mostrarProducto(id_producto):
    con = sqlite3.connect("funkos.db")
    cur = con.cursor()
    # Ejecutar la consulta
    cur.execute("SELECT * FROM PRODUCTO WHERE ProductoID = ?", (id_producto,))
    
    # Obtener todos los resultados
    resultado = cur.fetchall()

    con.close()

    return mapearProducto(resultado)

# Modifica los datos del producto pasando su id
def modificarProducto(id_producto, nuevo_nombre, nuevo_precio, nueva_descripcion, nuevo_stock):
    con = sqlite3.connect("funkos.db")
    cur = con.cursor()
    # Ejecutar la consulta
    cur.execute("UPDATE PRODUCTO SET Nombre = ?, PrecioEUR = ?, Descripcion = ?, StockDisponible = ? WHERE ProductoID = ?", (nuevo_nombre, nuevo_precio, nueva_descripcion, nuevo_stock, id_producto))

    # Confirmar los cambios
    con.commit()

    con.close()

def mapearProductos(listaProductos):
    productos_mapeados = []
    for item in listaProductos:
        producto = {
            "ID": item[0],
            "Nombre": item[1],
            "PrecioEUR": item[2],
            "Descripcion": item[3],
            "StockDisponible": item[4]
        }
        productos_mapeados.append(producto)

    return json.dumps(productos_mapeados, indent=2)

def mapearProducto(producto):
    productoMapeado = {
        "ID": producto[0][0],
        "Nombre": producto[0][1],
        "PrecioEUR": producto[0][2],
        "Descripcion": producto[0][3],
        "StockDisponible": producto[0][4]
    }

    return productoMapeado