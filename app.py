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
    control_task_id +=1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa foi adicionada com sucesso!"})

@app.route("/tasks", methods=["GET"])
def get_tasks():
    task_list = []
    for task in tasks:
        task_list.append(task.to_dict())

    output = {
                "task": task_list,
                "total": len(task_list)
    }

    return jsonify(output)

@app.route("/tasks/<int:id>", methods=["GET"])
def get_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
        
    
    return jsonify({"message": "Nao foi possivell encontrar a atividade"}, 404)
    
        
@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t

    if task == None:   
        return jsonify({"message": "Nao foi possivell encontrar a atividade"}, 404)

    data = request.get_json()
    task.title = data["title"]
    task.description = data["description"]
    task.completed = data["completed"] 

    return jsonify({"message": "Tarefa atualizada com sucesso"}, 200)

@app.route('/tasks/<int:id>', methods=["DELETE"])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
            
    if not task:
        return jsonify({"message": "Nao foi possivell encontrar a atividade"}, 404)

    tasks.remove(task)
    return jsonify("Tarefa deletada com sucesso")


if __name__ == "__main__":
    app.run(debug=True)

