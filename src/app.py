from flask import Flask, jsonify, request
import json

app = Flask(__name__)

todos = [
     { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_todos = jsonify(todos)
    return json_todos
    

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = json.loads(request.data)
    todos.append(request_body)
    #print("Incoming request with the following body", decoded_object)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    remove = todos.pop(0)
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)