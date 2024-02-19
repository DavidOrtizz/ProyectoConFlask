import sqlite3
import json


def selectListaProductoPedidos():

    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute(
        "SELECT * FROM LISTA_PRODUCTO_PEDIDO JOIN PEDIDO ON PEDIDO.PedidoID = PRODUCTO.ProductoID")

    resultados = cur.fetchall()

    con.close()

    return resultados


def crearListaProductoPedido(ProductoID, PedidoID, Cantidad):

    con = sqlite3.connect("funkos.db")
    cur = con.cursor()
    TotalProductoEUR = calculaTotalProductoEUR(ProductoID, Cantidad)

    cur.execute("INSERT INTO LISTA_PRODUCTO_PEDIDO (ProductoID, PedidoID, Cantidad, TotalProductoEUR) VALUES (?,?,?,?)",
                (ProductoID, PedidoID, Cantidad, TotalProductoEUR))

    con.commit()

    con.close()


def calculaTotalProductoEUR(ProductoID, Cantidad):
    con = sqlite3.connect("funkos.db")
    cur = con.cursor()
    cur.execute("SELECT PrecioEUR FROM PRODUCTO WHERE ProductoID = ProductoID")

    precioEUR = cur.fetchall()
    precioEUR *= Cantidad

    con.commit()

    con.close()

    return precioEUR


def listaProductoPedidoDetalle(PedidoProductoID):

    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute(
        "SELECT * FROM LISTA_PRODUCTO_PEDIDO WHERE PedidoProductoID = ?", str(PedidoProductoID))

    resultados = cur.fetchall()

    con.close()

    return resultados


def modificarLISTA_PRODUCTO_PEDIDO(ProductoPedidoID, nuevoProductoID, nuevoPedidoID, nuevoCantidad, nuevoTotalProductoEUR):

    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute("UPDATE LISTA_PRODUCTO_PEDIDO SET ProductoID = ?, PedidoID = ?, Cantidad = ?, TotalProductoEUR = ? WHERE PedidoProductoID = ?",
                (nuevoProductoID, nuevoPedidoID, nuevoCantidad, nuevoTotalProductoEUR, ProductoPedidoID))

    con.commit()

    con.close()


def borrarlistaProductoPedido(ProductoPedidoID):

    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute("DELETE FROM LISTA_PRODUCTO_PEDIDO WHERE PedidoProductoID = ?", str(
        ProductoPedidoID))

    con.commit()

    con.close()


def mapearListaProductoPedidos(selectListaProductoPedidos):
    pedidos_mapeados = []
    for item in selectListaProductoPedidos:
        item = {
            "PedidoProductoID": item[0],
            "ProductoID": item[1],
            "PedidoID": item[2],
            "Cantidad": item[3],
            "TotalProductoEUR": item[4]
        }
        pedidos_mapeados.append(item)

    return json.dumps(pedidos_mapeados, indent=2)


def mapearListaProductoPedido(ProductoPedidoID):
    pedidoMapeado = {
        "PedidoProductoID": ProductoPedidoID[0][0],
        "ProductoID": ProductoPedidoID[0][1],
        "PedidoID": ProductoPedidoID[0][2],
        "Cantidad": ProductoPedidoID[0][3],
        "TotalProductoEUR": ProductoPedidoID[4]
    }
    return pedidoMapeado
