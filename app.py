from flask import Flask,request,jsonify
from models.task import Task

app = Flask(__name__)


tasks = []
control_task_id = 1
@app.route("/tasks", methods=['POST'])
def create_task():
    global control_task_id
    data = request.get_json()
    new_task = Task(id=control_task_id, title=data['title'], description=data['description'])
    control_task_id +1
    tasks.append(new_task)
    print(tasks)
    return "TEST API"

if __name__ == "__main__":
    app.run(debug=True)

