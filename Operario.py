import sqlite3
import json

def listaOperarios():
    
    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM OPERARIO WHERE Rol = 'Usuario'")

    resultados = cur.fetchall()

    con.close()

    return mapearOperarios(resultados)

def crearOperario(Nombre, Direccion, Rol, SedeID):
    
    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute("INSERT INTO OPERARIO (Nombre, Direccion, Rol, SedeID) VALUES (?,?,?,?)", (Nombre, Direccion, Rol, SedeID))

    con.commit()

    con.close()

def operarioDetalle(OperarioID):
    
    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM OPERARIO WHERE OperarioID = ?", (str(OperarioID),))

    resultados = cur.fetchall()

    con.close()

    print(str(resultados))

    return mapearOperario(resultados)

def modificarOperario(OperarioID, nuevoNombre, nuevaDireccion, nuevoRol, nuevaSedeID):

    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute("UPDATE OPERARIO SET Nombre = ?, Direccion = ?, Rol = ?, SedeID = ? WHERE OperarioID = ?", (nuevoNombre, nuevaDireccion, nuevoRol, nuevaSedeID, OperarioID))

    con.commit()

    con.close()

def borrarOperario(OperarioID):

    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute("DELETE FROM OPERARIO WHERE OperarioID = ?", (str(OperarioID),))

    con.commit()

    con.close()

def mapearOperarios(listaOperarios):
    operarios_mapeados = []
    for item in listaOperarios:
        operario = {
            "ID": item[0],
            "Nombre": item[1],
            "Direccion": item[2],
            "Rol": item[3],
            "SedeID": item[4]
        }
        operarios_mapeados.append(operario)

    return json.dumps(operarios_mapeados, indent=2)

def mapearOperario(operario):
    operarioMapeado = {
        "ID": operario[0][0],
        "Nombre": operario[0][1],
        "Direccion": operario[0][2],
        "Rol": operario[0][3],
        "SedeID": operario[0][4]
    }

    return operarioMapeado