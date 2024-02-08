from flask import Flask, request
import sys

import Operario
import Producto

log_file = open('log.txt', 'w')

print("Escribiendo resultados en log.txt")
sys.stdout = log_file
sys.stderr = log_file

app = Flask(__name__)

# ENDPOINT LANDING

@app.route('/')
def landing():
    return "<h1>FLASK API</h1>"

# ENDPOINTS OPERARIO

@app.route('/operario')
def listaOperarios():
    return Operario.listaOperarios()

@app.route('/operario', methods=['POST'])
def crearOperario():

    datos_json = request.json
    Nombre = datos_json['Nombre']
    Direccion = datos_json['Direccion']
    Rol = datos_json['Rol']
    SedeId = datos_json['SedeID']

    return Operario.crearOperario(Nombre,Direccion,Rol,SedeId)

@app.route('/operario/<int:OperarioID>')
def operarioDetalle(OperarioID):
    return Operario.operarioDetalle(OperarioID)

""" 
JSON:

{
    "Nombre": "Pablo",
    "Direccion": "Calle 2",
    "Rol": "Usuario",
    "SedeID": 1
}

@app.route('/operario/<OperarioID>', methods=['PUT'])
def modificaroOperario():

    return "<p>Hello, World!</p>"

@app.route('/operario/<OperarioID>', methods=['DELETE'])
def borrarOperario():

    return "<p>Hello, World!</p>" 
"""

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



if __name__ == "__main__":
    app.run()


