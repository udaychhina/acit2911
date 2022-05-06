import pytest

def test_homepage(client):
    response = client.get("/")
    
    assert b"ACIT2911" in response.data
    assert b"Assignment" in response.data
    assert b"Do some agile stuff" in response.data
    assert b"June 1st, 2022" in response.data
    assert b"</table>" in response.data
    
def test_homework_post(client):
    response = client.post("/homework", data={
        "course": "ACIT4200", "name": "assignment 4", \
    "type": "Assignment", "description": "Do some brainstorm", \
    "duedate": "April 20, 2022"
    })
    assert response.status_code == 201
    response = client.get("/")
    assert b"ACIT4200" in response.data
    assert b"Assignment" in response.data
    assert b"Do some brainstorm" in response.data
    assert b"April 20, 2022" in response.data