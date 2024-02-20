import json
import sqlite3

con = sqlite3.connect("funkos.db")
cur = con.cursor()

def listaSedesMurcia():
# Ejecutar la consulta
    
    con = sqlite3.connect("funkos.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM SEDE" )
    # Obtener todos los resultados
    resultados = cur.fetchall()
    return mapearSedes(resultados)
con.close()

def anadirSede(direccion, Nif):
    con = sqlite3.connect("funkos.db")
    cur = con.cursor()
    cur.execute("INSERT INTO SEDE (Direccion, NIF) VALUES (?,?)", (direccion, Nif))

    con.commit()

    con.close()

def eliminarSede(sedeId):
    con = sqlite3.connect("funkos.db")
    cur = con.cursor()
    cur.execute("DELETE FROM SEDE WHERE SedeID = ?", (sedeId,))
    con.commit()
    con.close()

def mostrarSede(sedeId):
    con = sqlite3.connect("funkos.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM SEDE WHERE SedeID = ?", (sedeId,))
    resultados = cur.fetchall()
    con.close()
    return mapearSede(resultados)

def modificarSede(sedeId, direccion, NIF):
    con = sqlite3.connect("funkos.db")
    cur = con.cursor()
    cur.execute("UPDATE SEDE SET Direccion = ?, NIF = ? WHERE SedeID = ?", (direccion, NIF, sedeId))
    con.commit()
    con.close()

def mapearSedes(listaSedes):
    sedes_mapeadas = []
    for item in listaSedes:
        sede = {
            "ID": item[0],
            "Direccion": item[1],
            "Nif": item[2],
        }
        sedes_mapeadas.append(sede)

    return json.dumps(sedes_mapeadas, indent=2)

def mapearSede(sede):
    sedeMapeada = {
        "ID": sede[0][0],
        "Direccion": sede[0][1],
        "Nif": sede[0][2],
    }

    return sedeMapeada