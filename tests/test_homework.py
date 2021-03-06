from urllib import response
import pytest
import flask
import sqlite3
from flask import Blueprint
import hw_tracker
from hw_tracker.db import get_db


def test_app(client):
    bp = Blueprint('homework', __name__)
    print(type(bp))
    assert isinstance(bp, flask.blueprints.Blueprint)


def test_index(client, auth):
    response = client.get('/index')
    assert b"Log In" in response.data
    assert b"Register" in response.data


def test_settings(client):
    response = client.get('/settings')
    assert b'Toggle Theme' in response.data


def test_confirmation(client):
    response = client.get('/confirmation')
    assert b'added' in response.data


def test_deleteconfirm(client):
    response = client.get('/deleteconfirm')
    assert b'deleted' in response.data


def test_emailconfirm(client):
    response = client.get('/emailconfirm')
    assert b'Email' in response.data


def test_about(client):
    response = client.get('/about')
    assert b'settings' in response.data


def test_welcome(client):
    response = client.get('/')
    assert b'settings' in response.data


def test_toggle_theme(client):
    response = client.get('toggle_theme')
    assert response.status_code == 302


def test_delete(client, app):
    assert client.get('/auth/login').status_code == 200
    response = client.post(
        '/auth/login', data={'username': 'testuser', 'password': 'T#stpass'}
    )
    assert response.headers['Location'] == '/index'
    assert client.get('/1/delete').status_code == 302

    with app.app_context():
        db = get_db()
        hw = db.execute('SELECT * FROM hw WHERE id = 1').fetchone()
        assert hw is None


@pytest.mark.parametrize('path', (
    '/create',
    '/1/update',
))
def test_login_required(client, path):
    response = client.post(path)
    assert response.headers['Location'] == '/auth/login'


def test_update(client, auth, app):
    # response = client.post(
    #     '/auth/login', data={'username': 'testuser', 'password': 'T#stpass'}
    # )
    auth.login()
    assert client.post('/1/update', data={}).status_code == 200
    assert client.post('/1/update', data={'course': 'updated', 'name': 'test', 'type': 'assignment',
                       'description': 'testtheassignment', 'duedate': '2022-05-05'}).status_code == 302


def test_email(client, auth, app):
    auth.login()
    assert client.post('/1/email', data={}).status_code == 200
    assert client.post(
        "/1/email", data={"email_address": "tannedstone@gmail.com"}).status_code == 302


def test_search(client, auth, app):
    auth.login()
    assert client.get('/search').status_code == 200
    assert client.post('/search', data={"search": ""}).status_code == 200
    assert client.post('/search', data={"search": "test"}).status_code == 200


@pytest.mark.parametrize(('path', 'code'), (
    ('/2/update', 404),
    ('/2/delete', 405),
))
def test_does_not_exist(client, auth, path, code):
    auth.login()
    assert client.post(path).status_code == code


def test_create(auth, client, app):
    auth.login()
    assert client.post('/create').status_code == 200
    assert client.post('/create', data={
        'course': 'test',
        'name': 'test',
        'type': 'assignment',
        'description': 'testtheassignment',
        'duedate': '2022-05-05'
    }).status_code == 302
