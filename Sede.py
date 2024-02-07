import sqlite3

con = sqlite3.connect("funkos.db")
cur = con.cursor()

def listaSedesMurcia():
# Ejecutar la consulta
    cur.execute("SELECT * FROM SEDE WHERE direccion = 'Murcia'" )
    # Obtener todos los resultados
    resultados = cur.fetchall()
    return resultados
con.close()

def añadirSede(direccion, Nif):
    cur.execute("INSERT INTO SEDE(Dirección,NIF)VALUES(?,?)",(direccion,Nif))
    con.commit()

def eliminarSede(sedeId):
    cur.execute("DELETE FROM SEDE WHERE SedeID = ?",(sedeId) )
    con.commit()    

def mostrarSede(sedeId):
    cur.execute("SELECT * FROM SEDE WHERE SedeId = ?",(sedeId) )
    resultados = cur.fetchall()
    return resultados 

def modificarSede(sedeId,direccion,NIF):
    cur.execute("SELECT * FROM SEDE WHERE SedeId = ?",(sedeId) ) 