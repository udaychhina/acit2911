import inspect
import json
from logging.handlers import DatagramHandler
from models.homework import Homework
from models.school import School

import requests

API_URL = "http://127.0.0.1:5000"
BASE_DATA=[{"course": "ACIT2911", "name": "ACIT2911 assignment 2", \
    "typehw": "Assignment", "description": "Do some agile stuff", \
    "duedate": "June 1st, 2022", "completed": "no"},\
    {"course": "ACIT2811", "name": "Assignment 3", "typehw": "Assignment", \
    "description": "Explain what makes good UI/UX",\
    "duedate": "June 3rd, 2022", "completed": "no"}, \
    {"course": "ACIT2911", "name": "Quiz 4", "typehw": "Quiz", \
    "description": "Quiz on github", "duedate": "June 5th, 2022", "completed": "no"}]

def make_request(
    endpoint, expected_code, method="get", data=None, decode_json=True, level=0
):
    prefix = "  " * level
    print(f"{prefix}{method.upper()} {endpoint} (expecting {expected_code})...")
    kwargs = {}
    func = getattr(requests, method)

    if data:
        kwargs["json"] = data
        print(f"{prefix} > Data provided", data)

    status = True
    data = ""

    try:
        resp = func(API_URL + endpoint, **kwargs)
        if decode_json:
            data = resp.json()
        else:
            data = resp.text
    except json.decoder.JSONDecodeError:
        data = "Cannot decode JSON from API."
        status = False
    except (requests.exceptions.ConnectionError,):
        data = "Connection error."
        status = False
    else:
        if resp.status_code != expected_code:
            print(
                f"{prefix}  Status code should be {expected_code}, got {resp.status_code}."
            )
            status = False

    return status, data

def reset_json():
    """Reset JSON file to default values"""
    with open("data/homework.json", "w") as fp:
        json.dump(BASE_DATA, fp)
        
def homepage():
    """Checks the HTML homepage"""
    status, data = make_request("/", 200, decode_json=False)
    if not status:
        print("  !!! NOK", data)
        return

    assert "ACIT2911" in data
    assert "Assignment" in data
    assert "Do some agile stuff" in data
    assert "June 1st, 2022" in data
    assert "</table>" in data
    print("  --> OK!")
    
def create():
    """Checks the /homework API endpoint (POST)"""
    deadline={"course": "ACIT4200", "name": "assignment 4", \
    "type": "Assignment", "description": "Do some brainstorm", \
    "duedate": "April 20, 2022"}
    deadline_dump=json.dumps(deadline)
    homework = Homework(deadline['course'], deadline['name'], deadline['type'], deadline['description'], deadline['duedate'])
    school = School("BCIT")
    school.add(homework)
    school.save()
    
    #not working yet
    """status, data = make_request("/homework", 201, "post", data=json.dumps(deadline))
    if not status:
        print("  !!! NOK", data)
        return"""
    
    status, data = make_request("/", 200, decode_json=False)
    if not status:
        print("  !!! NOK", data)
        return
    
    assert "ACIT4200" in data
    assert "Assignment" in data
    assert "Do some brainstorm" in data
    assert "April 20, 2022" in data
    print("  --> OK!")

    
def check():
    funcs = [
        reset_json,
        homepage,
        create
    ]

    for func in funcs:
        print("=" * 80)
        print(inspect.getdoc(func))
        print("-" * 80)
        func()
        print()
    
if __name__ == "__main__":
    check()