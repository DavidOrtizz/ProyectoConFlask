import sqlite3
import json
import ListaProductoPedido


def listaPedidos():

    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute(
        "SELECT P.PedidoID, O.OperarioID, O.Nombre, P.TotalPedidoEUR, P.Pagado FROM PEDIDO P JOIN OPERARIO O ON P.OperarioID = O.OperarioID")

    resultados = cur.fetchall()

    con.close()

    return mapearPedidos(resultados)


def crearPedido(OperarioID, TotalPedidoEUR, Pagado):

    con = sqlite3.connect("funkos.db")
    cur = con.cursor()
    cur.execute("INSERT INTO PEDIDO (OperarioID, TotalPedidoEUR, Pagado) VALUES (?,?,?)",
                (OperarioID, TotalPedidoEUR, Pagado))

    con.commit()
    con.close()


def pedidoDetalle(PedidoID):

    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute("SELECT P.PedidoID, O.OperarioID, O.Nombre, P.TotalPedidoEUR, P.Pagado FROM PEDIDO P JOIN OPERARIO O ON P.OperarioID = O.OperarioID WHERE P.PedidoID = (?)", (str(PedidoID)))

    resultado = cur.fetchall()
    print(resultado)
    con.close()

    return mapearPedido(resultado)


def modificarPedido(PedidoID, nuevoOperarioID, nuevoTotalPedidoEUR, nuevoPagado):

    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute("UPDATE Pedido SET OperarioID = ?, TotalPedidoEUR = ?, Pagado = ? WHERE PedidoID = ?",
                (nuevoOperarioID, nuevoTotalPedidoEUR, nuevoPagado, PedidoID))

    con.commit()

    con.close()


def borrarPedido(PedidoID):

    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute("DELETE FROM Pedido WHERE PedidoID = ?", str(PedidoID))

    con.commit()

    con.close()


def mapearPedidos(listaPedido):
    pedidos_mapeados = []
    for item in listaPedido:
        pedido = {
            "PedidoID": item[0],
            "OperarioID": item[1],
            "OperarioNombre": item[2],
            "TotalPedidoEUR": item[3],
            "Pagado": item[4]
        }
        pedidos_mapeados.append(pedido)

    return json.dumps(pedidos_mapeados, indent=4)


def mapearPedido(pedido):
    pedidoMapeado = {
        "PedidoID": pedido[0][0],
        "OperarioID": pedido[0][1],
        "OperarioNombre": pedido[0][2],
        "TotalPedidoEUR": pedido[0][3],
        "Pagado": pedido[0][4]
    }
    return pedidoMapeado
