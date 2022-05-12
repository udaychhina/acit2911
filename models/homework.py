import uuid

class Homework:
    def __init__(self, Course, Name, Type, Description, DueDate, Completed="no"):

        if type(Course) != str:
            raise ValueError("Must be string.")
        if type(Type) != str:
            raise ValueError("Must be string.")
        if type(Description) != str:
            raise ValueError("Must be a string.")
        if type(DueDate) != str:
            raise ValueError("Must be a string.")
        self.id = uuid.uuid4().hex
        self.course = Course
        self.name = Name
        self.typehw = Type
        self.description = Description
        self.duedate = DueDate
        self.completed = Completed


        

    def to_dict(self):
        thing = vars(self)
        return thing