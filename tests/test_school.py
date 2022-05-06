from models.school import School
from models.homework import Homework
from unittest.mock import patch, mock_open
import pytest



TEST_JSON = """
[
    {
        "course": "ACIT2911",
        "name": "assignment 2",
        "typehw": "Assignment",
        "description": "Do some agile stuff",
        "duedate": "June 1st, 2022",
        "completed": "no"
    },
    {
        "course": "ACIT2811",
        "name": "Quiz 2",
        "typehw": "Quiz",
        "description": "Quiz on the design thinking process",
        "duedate": "June 3rd, 2022",
        "completed": "no"
    },
    {
        "course": "ACIT4770",
        "name": "Assignment 3",
        "typehw": "Assignment",
        "description": "Make your personal code of ethics",
        "duedate": "June 5th, 2022",
        "completed": "no"
    },
    {
        "course": "ACIT2911",
        "name": "Quiz 4",
        "typehw": "Quiz",
        "description": "Quiz on CI/CD",
        "duedate": "June 6th, 2022",
        "completed": "no"
    }
]
"""

@pytest.fixture
@patch('builtins.open',new_callable=mock_open, read_data=TEST_JSON)
def bcit(mock_file):
    school = School("BCIT")
    return school


def test_school(bcit):
    assert bcit.name == "BCIT"

def test_school_len(bcit):
    assert len(bcit) == 4


def test_add_success(bcit):
    assignment = Homework("ACIT2911","Assignment 3","Assignment","New Assignment","April 1st, 2022")
    bcit.add(assignment)
    assert assignment in bcit.hwlist


@patch("builtins.open", new_callable=mock_open)
def test_save(mock_file, bcit):
    bcit.save()
    mock_file.assert_called_once_with("data/homework.json", "w")