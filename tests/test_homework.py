import pytest
from hw_tracker.db import get_db


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


def test_about(client):
    response = client.get('/about')
    assert b'settings' in response.data


def test_welcome(client):
    response = client.get('/')
    assert b'settings' in response.data


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


@pytest.mark.parametrize('path',(
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
    assert client.get('/1/update').status_code == 200
    assert client.post('/1/update', data={'course': 'updated', 'name': 'test', 'typehw': 'assignment', 'desc': 'testtheassignment', 'duedate': '2022-05-05'}).status_code == 200

    
@pytest.mark.parametrize(('path', 'code'), (
    ('/2/update', 404),
    ('/2/delete', 405),
))
def test_does_not_exist(client, auth, path, code):
    auth.login()
    assert client.post(path).status_code == code

def test_create(auth, client, app):
    auth.login()
    assert client.get('/create').status_code == 200
    response = client.post('/create', data={
        'course': 'test', 
        'name': 'test', 
        'typehw': 'assignment', 
        'desc': 'testtheassignment', 
        'duedate': '2022-05-05'
    })

    assert response.headers['Location'] == '/homework/confirm'

    # with app.app_context():
    #     db = get_db()
    #     count = db.execute('SELECT COUNT(id) FROM hw').fetchone()[0]
    #     assert count == 2