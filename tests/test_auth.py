import pytest
from flask import g, session
from hw_tracker.db import get_db

# https://flask.palletsprojects.com/en/2.1.x/tutorial/tests/
def test_register(client, app):
    assert client.get('/auth/register').status_code == 200
    response = client.post(
        '/auth/register', data={'username': 'testuser', 'password': 'TestP@a5s'}
    )
    assert response.headers["Location"] == "/auth/login"

    with app.app_context():
        assert get_db().execute(
            "SELECT * FROM user WHERE username = 'testuser'",
        ).fetchone() is not None


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('', '', b'Username is required.'),
    ('testuser', '', b'Password is required.'),
    ('test', 'TestP@a5s', b'8 characters or longer'),
))
def test_register_validate_input(client, username, password, message):
    response = client.post(
        '/auth/register',
        data={'username': username, 'password': password}
    )
    assert message in response.data


def test_login(client, auth):
    assert client.get('/auth/login').status_code == 200
    response = auth.login()
    assert response.headers["Location"] == "/index"

    with client:
        client.get('/index')
        assert session['user_id'] == 1
        assert g.user['username'] == 'test'


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('', 'TestP@a5s', b'Incorrect username.'),
    ('test', 'TESTPASS', b'Incorrect password.'),
))
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    print(response)
    assert message in response.data


def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert 'user_id' not in session