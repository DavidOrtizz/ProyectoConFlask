import sqlite3

def listaOperarios():
    
    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM OPERARIO WHERE Rol = 'Usuario'")

    resultados = cur.fetchall()

    con.close()

    return resultados;

def crearOperario(Nombre, Direccion, Rol, SedeID):
    
    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute("INSERT INTO OPERARIO (Nombre, Direccion, Rol, SedeID) VALUES (?,?,?,?)", Nombre, Direccion, Rol, SedeID)

    con.commit()

    con.close()