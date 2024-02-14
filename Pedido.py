import sqlite3

def listaPedidos():
    
    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM PEDIDO")

    resultados = cur.fetchall()

    con.close()

    return resultados

def crearPedido(OperarioID, TotalPedido, Pagado):
    
    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute("INSERT INTO PEDIDO (OperarioID, TotalPedido, Pagado) VALUES (?,?,)", (OperarioID, TotalPedido, Pagado))

    con.commit()

    con.close()

def pedidoDetalle(PedidoID):
    
    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM PEDIDO WHERE PedidoID = ?", str(PedidoID))

    resultados = cur.fetchall()

    con.close()

    return resultados

def modificarPedido(PedidoID, nuevoOperarioID, nuevoTotalPedido, nuevoPagado):

    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute("UPDATE Pedido SET OperarioID = ?, TotalPedido = ?, Pagado = ? WHERE PedidoID = ?", (nuevoOperarioID, nuevoTotalPedido, nuevoPagado, PedidoID))

    con.commit()

    con.close()

def borrarPedido(PedidoID):

    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute("DELETE FROM Pedido WHERE PedidoID = ?", str(PedidoID))

    con.commit()

    con.close()