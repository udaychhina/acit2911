import pytest
from models.homework import Homework


def test_homework():
    hw = Homework(Id=123690, Course="ACIT 2515", Name="Python Exam", Type="Exam",
                  Description="Study pytesting", DueDate="April 25th, 2022", Completed="Yes")
    assert hw.id == 123690
    assert hw.course == "ACIT 2515"
    assert hw.name == "Python Exam"
    assert hw.typehw == "Exam"
    assert hw.description == "Study pytesting"
    assert hw.duedate == "April 25th, 2022"
    assert hw.completed == "Yes"


def test_homework_failure():
    with pytest.raises(ValueError):
        Homework(Id=123432, Course=2515, Name="Python Exam", Type="Exam",
                 Description="Study pytesting", DueDate="April 25th, 2022", Completed="Yes")

    with pytest.raises(ValueError):
        Homework(Id=123123, Course="ACIT 2515", Name="Python Exam", Type=1,
                 Description="Study pytesting", DueDate="April 25th, 2022", Completed="Yes")

    with pytest.raises(ValueError):
        Homework(Id=656443, Course="ACIT 2515", Name="Python Exam", Type="Exam",
                 Description=4.0, DueDate="April 25th, 2022", Completed="Yes")

    with pytest.raises(ValueError):
        Homework(Id=999999, Course="ACIT 2515", Name="Python Exam", Type="Exam",
                 Description="Study pytesting", DueDate=27, Completed="Yes")

    # with pytest.raises(ValueError):
        #Homework(Course="ACIT 2515", Name="Python Exam", Type="Exam", Description="Study pytesting", DueDate="April 25th, 2022", Completed="Maybe")


def test_to_dict():
    hw = Homework(Id=123543, Course="ACIT 2515", Name="Python Exam", Type="Exam",
                  Description="Study pytesting", DueDate="April 25th, 2022", Completed="Yes")
    assert type(hw.to_dict()) == dict
