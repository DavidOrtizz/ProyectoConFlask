from flask import Flask
import Operario

app = Flask(__name__)

# ENDPOINT LANDING

@app.route('/')
def landing():
    return "<h1>FLASK API</h1>"

# ENDPOINTS OPERARIO

@app.route('/operario')
def listaOperarios():
    return Operario.listaOperarios()

@app.route('/operario', methods=['POST'])
def crearOperario():
    Operario.crearOperario("Pablo","Calle2","Usuario","1")
    return "Ok"

""" 
@app.route('/operario/<OperarioID>')
def operarioDetalle():

    return "<p>Hello, World!</p>"

@app.route('/operario/<OperarioID>', methods=['PUT'])
def modificaroOperario():

    return "<p>Hello, World!</p>"

@app.route('/operario/<OperarioID>', methods=['DELETE'])
def borrarOperario():

    return "<p>Hello, World!</p>" 
"""

if __name__ == "__main__":
    app.run()