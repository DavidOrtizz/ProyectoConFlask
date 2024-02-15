import sqlite3
import json

def listaPedidos():
    
    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute("SELECT PedidoID, Operario.Nombre, TotalPedidoEUR, Pagado FROM PEDIDO JOIN OPERARIO ON PEDIDO.OperarioID = OPERARIO.OperarioID")

    resultados = cur.fetchall()

    con.close()

    return resultados

def crearPedido(OperarioID, TotalPedidoEUR, Pagado):
    
    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute("INSERT INTO PEDIDO (OperarioID, TotalPedidoEUR, Pagado) VALUES (?,?,)", (OperarioID, TotalPedidoEUR, Pagado))

    con.commit()

    con.close()

def pedidoDetalle(PedidoID):
    
    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM PEDIDO WHERE PedidoID = ?", str(PedidoID))

    resultados = cur.fetchall()

    con.close()

    return resultados

def modificarPedido(PedidoID, nuevoOperarioID, nuevoTotalPedidoEUR, nuevoPagado):

    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute("UPDATE Pedido SET OperarioID = ?, TotalPedidoEUR = ?, Pagado = ? WHERE PedidoID = ?", (nuevoOperarioID, nuevoTotalPedidoEUR, nuevoPagado, PedidoID))

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
    for item in listaPedidos:
        pedido = {
            "PedidoID": item[0],
            "OperarioNombre": item[1],
            "TotalPagadoEUR": item[2],
            "Pagado": item[3]
        }
        pedidos_mapeados.append(pedido)

    return json.dumps(pedidos_mapeados, indent=2)

def mapearPedido(pedido):
    pedidoMapeado = {
        "PedidoID": pedido[0][0],
        "OperarioNombre": pedido[0][1],
        "TotalPagadoEUR": pedido[0][2],
        "Pagado": pedido[0][3]
    }
    return pedidoMapeado