from flask import Flask
import Producto

app = Flask(__name__)

# EndPoints de productos

@app.route("/productos")
def mostrarProductos():
  return Producto.mostrarDatosProductos()

@app.route("/mostrarProducto/<productoID>")
def mostrarProducto(productoID):
  return Producto.mostrarUnProducto(productoID)

@app.route("/modificarProducto", methods=['POST'])
def modificarProducto(productoID, nuevo_nombre, nuevo_precio, nueva_descripcion, nuevo_stock):
    Producto.modificarProducto(productoID, nuevo_nombre, nuevo_precio, nueva_descripcion, nuevo_stock)
    return "Producto modificado"

@app.route("/eliminarProducto", methods=['POST'])
def eliminarProducto(productoID):
   Producto.eliminarProducto(productoID)
   return "Producto eliminado"

@app.route("/añadirProducto", methods=['POST'])
def añadirProducto(nombre, precio, descripcion, stock):
    Producto.añadirProducto(nombre, precio, descripcion, stock)
    return "Producto añadido"