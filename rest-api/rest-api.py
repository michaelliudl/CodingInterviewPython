from flask import  Flask, jsonify, request
from http import HTTPStatus, HTTPMethod

app = Flask(__name__)

tasks = []

taskId = 1

@app.route('/tasks', methods=[HTTPMethod.GET])
def getTasks():
    return jsonify(tasks)

@app.route('/tasks', methods=[HTTPMethod.POST])
def addTask():
    global taskId
    newTask = {'id': taskId, 'task': request.json['task']}
    tasks.append(newTask)
    taskId += 1
    return jsonify(newTask), HTTPStatus.CREATED

@app.route('/tasks/<int:id>', methods=[HTTPMethod.PUT])
def updateTask(id):
    task = next((item for item in tasks if item['id'] == id), None)
    if not task:
        return jsonify({'error': 'Task not found for id {id}'.format(id)}), HTTPStatus.NOT_FOUND
    task['task'] = request.json['task']
    return jsonify(task)

@app.route('/tasks/<int:id>', methods=[HTTPMethod.DELETE])
def deleteTask(id):
    global tasks
    tasks = [task for task in tasks if task['id'] != id]
    return jsonify({'result': 'Task {id} delete'.format(id)})
