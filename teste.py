import pytest
import requests

#CRUD

BASE_URL = 'http://127.0.0.1:5000'
tasks = []

def test_create_task():
    new_data_task = {
                "title": "Criar nova task text",
                "description": "Essa e uma nova task de text"
        }

    response = requests.post(f"{BASE_URL}/tasks", json=new_data_task)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    response_json["id"] == 1

def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total" in response_json

def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json["id"]

def test_update_task():
    if tasks:
        task_id = tasks[0]
        pay_load = {
            "title": "MEU TESTE COM PUT",
            "description": "FAZENDO O UPDATE COM PUT",
            "completed": "COMPLETED",
        } 

        response = requests.put(f'{BASE_URL}/tasks/{task_id}', json=pay_load)
        assert response.status_code == 200
        response_json = response.json()
        assert "message" in response_json

        #fazendo a validação do dados do meu update
        response = requests.get(f'{BASE_URL}/tasks/{task_id}')
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["title"] == pay_load["title"]
        assert response_json["description"] == pay_load["description"]
        assert response_json["completed"] == pay_load["completed"]

def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f'{BASE_URL}/tasks/{task_id}')

        assert response.status_code == 200
        response_json = response.json()
        assert "message" in response_json

        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 404

        