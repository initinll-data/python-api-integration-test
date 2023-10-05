
import uuid

import requests

DOCS = "https://todo.pixegami.io/docs"

ENDPOINT = "https://todo.pixegami.io"


# helper functions to remove duplication
def new_task_payload():
    user_id = f"test_user_{uuid.uuid4().hex}"
    content = f"test_content_{uuid.uuid4().hex}"

    return {
        "content": content,
        "user_id": user_id,
        "is_done": False
    }


def get():
    return requests.get(url=f"{ENDPOINT}")


def create_task(payload):
    return requests.put(url=f"{ENDPOINT}/create-task", json=payload)


def update_task(payload):
    return requests.put(url=f"{ENDPOINT}/update-task", json=payload)


def get_task(task_id):
    return requests.get(url=f"{ENDPOINT}/get-task/{task_id}")


def list_tasks(user_id):
    return requests.get(url=f"{ENDPOINT}/list-tasks/{user_id}")


def delete_task(task_id):
    return requests.delete(url=f"{ENDPOINT}/delete-task/{task_id}")
