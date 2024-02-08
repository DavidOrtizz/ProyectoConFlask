import sqlite3

def listaOperarios():
    
    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM OPERARIO WHERE Rol = 'Usuario'")

    resultados = cur.fetchall()

    con.close()

    return resultados

def crearOperario(Nombre, Direccion, Rol, SedeID):
    
    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute("INSERT INTO OPERARIO (Nombre, Direccion, Rol, SedeID) VALUES (?,?,?,?)", (Nombre, Direccion, Rol, SedeID))

    con.commit()

    con.close()

def operarioDetalle(OperarioID):
    
    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM OPERARIO WHERE OperarioID = ?", str(OperarioID))

    resultados = cur.fetchall()

    con.close()

    return resultados

def modificarOperario(OperarioID, nuevoNombre, nuevaDireccion, nuevoRol, nuevaSedeID):

    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute("UPDATE OPERARIO SET Nombre = ?, Direccion = ?, Rol = ?, SedeID = ? WHERE OperarioID = ?", (nuevoNombre, nuevaDireccion, nuevoRol, nuevaSedeID, OperarioID))

    con.commit()

    con.close()

def borrarOperario(OperarioID):

    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute("DELETE FROM OPERARIO WHERE OperarioID = ?", str(OperarioID))

    con.commit()

    con.close()