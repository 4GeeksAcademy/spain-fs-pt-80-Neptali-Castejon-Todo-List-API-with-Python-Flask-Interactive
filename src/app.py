from flask import Flask, jsonify, request

# Crear una nueva aplicación Flask
app = Flask(__name__)

# variable global
todos = [ 
    { "label": "My first task", "done": False }
]

# Definir el primer endpoint
@app.route('/myroute', methods=['GET'])
def hello_world():
    return 'Hello World!'

# Definir el nuevo endpoint '/todos'
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# Endpoint para agregar un nuevo todo
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)

    todos.append(request_body)

    return jsonify(todos), 200

# Endpoint para eliminar un todo
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    
    if 0 <= position < len(todos):
        todos.pop(position)  # Eliminar la tarea por posición
        return jsonify(todos), 200  # Retornar la lista actualizada
    else:
        return jsonify({ "error": "Position out of range" }), 400
    

# Estas dos líneas siempre deben estar al final de tu archivo app.py
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

