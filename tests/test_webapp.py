import pytest
import flask
from webapp import create_app


def test_app(client):
    flask_app = create_app()
    assert isinstance(flask_app, flask.app.Flask)


def test_homepage(client):
    response = client.get("/")

    assert b"ACIT2911" in response.data
    assert b"Assignment" in response.data
    assert b"Do some agile stuff" in response.data
    assert b"June 1st, 2022" in response.data
    assert b"</table>" in response.data


def test_create_feature(client):
    response = client.post("/homework", data={
        "course": "ACIT4200", "name": "assignment 4",
        "type": "Assignment", "description": "Do some brainstorm",
        "duedate": "April 20, 2022"
    })
    assert response.status_code == 201
    response = client.get("/")
    assert b"ACIT4200" in response.data
    assert b"Assignment" in response.data
    assert b"Do some brainstorm" in response.data
    assert b"April 20, 2022" in response.data

    response = client.post("/homework", data={
        "course": "", "name": "assignment 4",
        "type": "Assignment", "description": "Do some brainstorm",
        "duedate": "April 20, 2022"
    })
    assert response.status_code == 400


"""def test_edit_feature(client):
    response = client.post("/edit", data={
        "course": "ACIT0777", "name": "assignment 7.77",
        "type": "Assignment", "description": "Do some luck",
        "duedate": "April 7, 2077"
    })
    assert response.status_code == 201
    response = client.get("/")
    assert b"ACIT4200" in response.data
    assert b"Assignment" in response.data
    assert b"Do some brainstorm" in response.data
    assert b"April 20, 2022" in response.data

    response = client.post("/homework", data={
        "course": "", "name": "assignment 7.77",
        "type": "Assignment", "description": "Do some luck",
        "duedate": "April 7, 2077"
    })
    assert response.status_code == 400
"""


def test_create_route(client):
    response = client.get("/create")
    assert response.status_code == 200


def test_homework_route(client):
    response = client.get("/homework")
    assert response.status_code == 200


def test_delete_route(client):
    response = client.get("/delete/5a396992050a4429af34687040bc5fd3")
    assert response.status_code == 200
