from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Setup getDone Workspace", "status": "Complete"},
    {"id": 2, "title": "Configure CI/CD", "status": "In Progress"}
]

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

@app.route('/')
def index():
    return " Backend API is Running!"

if __name__ == '__main__':
  
    app.run(host='0.0.0.0', port=5000)