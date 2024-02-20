from flask import Flask, request
import sys
from flask_cors import CORS

import Operario
import Producto
import Pedido
import Sede
import ListaProductoPedido

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
    SedeId = datos_json['SedeDireccion']

    Operario.crearOperario(Nombre, Direccion, Rol, SedeId)
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
    nuevaSedeID = datos_json['SedeDireccion']

    Operario.modificarOperario(
        OperarioID, nuevoNombre, nuevaDireccion, nuevoRol, nuevaSedeID)
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


@app.route('/producto')
def listaProducto():
    return Producto.listaProducto()

@app.route('/producto', methods=['POST'])
def añadirProducto():

    datos_json = request.json
    nombre = datos_json['Nombre']
    precio = datos_json['PrecioEUR']
    descripcion = datos_json['Descripcion']
    stock = datos_json['StockDisponible']

    Producto.añadirProducto(nombre, precio, descripcion, stock)
    return "Producto añadido"

@app.route('/producto/<int:productoID>')
def mostrarProducto(productoID):
    return Producto.mostrarProducto(productoID)


@app.route('/producto/<int:productoID>', methods=['PUT'])
def modificarProducto(productoID):

    datos_json = request.json
    nuevoNombre = datos_json['Nombre']
    nuevoPrecio = datos_json['PrecioEUR']
    nuevaDescripcion = datos_json['Descripcion']
    nuevoStock = datos_json['StockDisponible']

    Producto.modificarProducto(
        productoID, nuevoNombre, nuevoPrecio, nuevaDescripcion, nuevoStock)
    return "Producto modificado"


@app.route('/producto/<int:productoID>', methods=['DELETE'])
def eliminarProducto(productoID):
    Producto.eliminarProducto(productoID)
    return "Producto eliminado"


# ENDPOINTS PEDIDO
""" 
{
    "OperarioID": "1",
    "TotalPedidoEUR": "20",
    "Pagado": true
} 
"""


@app.route('/pedidos')
def listaPedidos():
    return Pedido.listaPedidos()


@app.route('/crearPedido', methods=['POST'])
def crearPedido():

    datos_json = request.json
    OperarioID = datos_json['OperarioID']
    TotalPedidoEUR = datos_json['TotalPedidoEUR']
    Pagado = datos_json['Pagado']

    Pedido.crearPedido(OperarioID, TotalPedidoEUR, Pagado)
    return "Pedido Creado"


@app.route('/pedido/<int:PedidoID>')
def pedidoDetalle(PedidoID):
    return Pedido.pedidoDetalle(PedidoID)


@app.route('/modificaPedido/<int:PedidoID>', methods=['PUT'])
def modificarPedido(PedidoID):

    datos_json = request.json
    nuevoOperarioID = datos_json['OperarioID']
    nuevoTotalPedidoEUR = datos_json['TotalPedidoEUR']
    nuevoPagado = datos_json['Pagado']

    Pedido.modificarPedido(PedidoID, nuevoOperarioID,
                           nuevoTotalPedidoEUR, nuevoPagado)
    return "Pedido modificado"


@app.route('/borrarPedido/<int:PedidoID>', methods=['DELETE'])
def borrarPedido(PedidoID):
    Pedido.borrarPedido(PedidoID)
    return "Pedido borrado"


#  ENDPOINTS SEDE


@app.route('/sede')
def listaSedesMurcia():
    return Sede.listaSedesMurcia()

@app.route('/sede', methods=['POST'])
def anadirSede():

    datos_json = request.json
    direccion = datos_json['Direccion']
    Nif = datos_json['Nif']

    Sede.anadirSede(direccion,Nif)
    return "Sede creada"

@app.route('/sede/<int:ID>')
def mostrarSede(ID):
    return Sede.mostrarSede(ID)

@app.route('/sede/<int:ID>', methods=['PUT'])
def modificarSede(ID):

    datos_json = request.json
    ID = datos_json['ID']
    direccion = datos_json['Direccion']
    Nif = datos_json['Nif']

    Sede.modificarSede(ID,direccion,Nif)
    return "Sede modificada"

@app.route('/sede/<int:ID>', methods=['DELETE'])
def eliminarSede(ID):
    Sede.eliminarSede(ID)
    return "Sede borrada" 



if __name__ == "__main__":
    app.run()
