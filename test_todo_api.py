from helpers_todo_api import (
    create_task,
    delete_task,
    get,
    get_task,
    list_tasks,
    new_task_payload,
    update_task,
)


def test_can_call_endpoint():
    response = get()
    assert response.status_code == 200


def test_can_create_task():
    # create a task
    payload = new_task_payload()

    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200

    data = create_task_response.json()
    task_id = data["task"]["task_id"]
    # get the task and validate
    get_task_response = get_task(task_id)

    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]


def test_can_update_task():
    # create a task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200

    task_id = create_task_response.json()["task"]["task_id"]

    # update the task
    new_payload = {
        "content": "my updated content",
        "user_id": payload["user_id"],
        "task_id": task_id,
        "is_done": True
    }
    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200

    # get and validate the change
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == new_payload["content"]
    assert get_task_data["is_done"] == new_payload["is_done"]


def test_can_list_tasks():
    # create N tasks
    n = 3
    payload = new_task_payload()
    for _ in range(n):
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200

    # list tasks and check that there are N items
    user_id = payload["user_id"]
    list_task_response = list_tasks(user_id)
    assert list_task_response.status_code == 200
    data = list_task_response.json()

    tasks = data["tasks"]
    assert len(tasks) == n


def test_can_delete_task():
    # create the task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200

    task_id = create_task_response.json()["task"]["task_id"]

    # delete the task
    delete_task_reponse = delete_task(task_id)
    assert delete_task_reponse.status_code == 200

    # get the task, and check it's not found
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 404
