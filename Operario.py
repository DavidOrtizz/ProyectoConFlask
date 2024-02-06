import sqlite3

con = sqlite3.connect("funkos.db")
cur = con.cursor()

# Ejecutar la consulta
cur.execute("SELECT * FROM OPERARIO WHERE Rol = 'Usuario'")

# Obtener todos los resultados
resultados = cur.fetchall()

# Imprimir los resultados
for resultado in resultados:
    print(resultado)

# Cerrar la conexión
con.close()