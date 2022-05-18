import pytest
import flask
from hw_tracker.__init__ import create_app


def test_app(client):
    flask_app = create_app()
    assert isinstance(flask_app, flask.app.Flask)


def test_welcome_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_index_page(client):
    response = client.get("/index")

    assert b"acit2911" in response.data
    assert b"Test" in response.data
    assert b"Test if this work" in response.data
    assert b"2022-05-17" in response.data
    assert b"</table>" in response.data
    assert response.status_code == 200


def test_create_feature(client):
    response = client.post("/create", data={
        "course": "ACIT4200", "name": "assignment 4",
        "type": "Assignment", "description": "Do some brainstorm",
        "duedate": "2022-04-20"
    })
    assert response.status_code == 201
    response = client.get("/index")
    assert b"ACIT4200" in response.data
    assert b"Assignment" in response.data
    assert b"Do some brainstorm" in response.data
    assert b"2022-04-20" in response.data


def test_edit_feature(client):
    response = client.post("/2/update", data={
        "course": "ACIT0777", "name": "assignment 7.77",
        "type": "Assignment", "description": "Do some luck",
        "duedate": "2077-07-02"
    })
    assert response.status_code == 200
    response = client.get("/index")
    assert b"ACIT0777" in response.data
    assert b"Assignment" in response.data
    assert b"Do some luck" in response.data
    assert b"2077-07-02" in response.data


def test_delete_route(client):
    response = client.get("/2/delete/4dc58e94dd6e48048bb773582ea3eb08")
    assert response.status_code == 200


def test_get_hw_route(client):
    response = client.get("/create")
    assert response.status_code == 200


def test_homework_route(client):
    response = client.get("/homework")
    assert response.status_code == 200
