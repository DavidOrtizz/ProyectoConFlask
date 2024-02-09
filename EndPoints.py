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

    Operario.crearOperario(Nombre,Direccion,Rol,SedeId)
    return "Operario Creado"

@app.route('/operario/<int:OperarioID>')
def operarioDetalle(OperarioID):
    return Operario.operarioDetalle(OperarioID)

@app.route('/operario/<int:OperarioID>', methods=['PUT'])
def modificaroOperario(OperarioID):

    datos_json = request.json
    nuevoNombre = datos_json['Nombre']
    nuevaDireccion = datos_json['Direccion']
    nuevoRol = datos_json['Rol']
    nuevaSedeID = datos_json['SedeID']

    Operario.modificarOperario(OperarioID, nuevoNombre, nuevaDireccion, nuevoRol, nuevaSedeID)
    return "Operario modificado"

@app.route('/operario/<int:OperarioID>', methods=['DELETE'])
def borrarOperario(OperarioID):
    Operario.borrarOperario(OperarioID)
    return "Operario borrado" 

""" 
ESTRUCTURA JSON OPERARIO:

{
    "Nombre": "Pablo",
    "Direccion": "Calle 2",
    "Rol": "Usuario",
    "SedeID": 1
}
"""

# EndPoints de productos

@app.route("/productos")
def mostrarProductos():
  return Producto.mostrarDatosProductos()

@app.route("/mostrarProducto/<int:productoID>")
def mostrarProducto(productoID):
  return Producto.mostrarUnProducto(productoID)

@app.route("/modificarProducto/<int:productoID>", methods=['POST'])
def modificarProducto(productoID):
    
    datos_json = request.json
    nuevoNombre = datos_json['Nombre']
    nuevoPrecio = datos_json['PrecioEUR']
    nuevaDescripcion = datos_json['Descripcion']
    nuevoStock = datos_json['StockDisponible']

    Producto.modificarProducto(productoID, nuevoNombre, nuevoPrecio, nuevaDescripcion, nuevoStock)
    return "Producto modificado"

@app.route("/eliminarProducto/<int:productoID>", methods=['DELETE'])
def eliminarProducto(productoID):
   Producto.eliminarProducto(productoID)
   return "Producto eliminado"

@app.route("/añadirProducto", methods=['PUT'])
def añadirProducto(nombre, precio, descripcion, stock):
    Producto.añadirProducto(nombre, precio, descripcion, stock)
    return "Producto añadido"



if __name__ == "__main__":
    app.run()


