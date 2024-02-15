from flask import Flask, request
import sys
from flask_cors import CORS

import Operario
import Producto
import Pedido
import Sede

app = Flask(__name__)

CORS(app)

log_file = open('log.txt', 'w')

print("Escribiendo resultados en log.txt")
sys.stdout = log_file
sys.stderr = log_file

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


# ENDPOINTS PEDIDO

@app.route('/pedido')
def listaPedidos():
    return Pedido.listaPedidos()

@app.route('/pedido', methods=['POST'])
def crearPedido():

    datos_json = request.json
    OperarioID = datos_json['OperarioID']
    TotalPedidoEUR = datos_json['TotalPedidoEUR']
    Pagado = datos_json['Pagado']

    Pedido.crearPedido(OperarioID, TotalPedidoEUR, Pagado)
    return "Pedido Creado"

@app.route('/pedido/<int:pedidoID>')
def pedidoDetalle(PedidoID):
    return Pedido.pedidoDetalle(PedidoID)

@app.route('/pedido/<int:pedidoID>', methods=['PUT'])
def modificarPedido(PedidoID):

    datos_json = request.json
    nuevoOperarioID = datos_json['OperarioID']
    nuevoTotalPedidoEUR = datos_json['TotalPedidoEUR']
    nuevoPagado = datos_json['Pagado']

    Pedido.modificarPedido(PedidoID, nuevoOperarioID, nuevoTotalPedidoEUR, nuevoPagado)
    return "Pedido modificado"

@app.route('/pedido/<int:PedidoID>', methods=['DELETE'])
def borrarPedido(PedidoID):
    Pedido.borrarPedido(PedidoID)
    return "Pedido borrado" 



if __name__ == "__main__":
    app.run()