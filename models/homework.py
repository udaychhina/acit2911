class Homework:
    def __init__(self, Course, Type, Description, DueDate):

        if type(Course) != str:
            raise ValueError("Must be string.")
        if type(Type) != str:
            raise ValueError("Must be string.")
        if type(Description) != str:
            raise ValueError("Must be a string.")
        if type(DueDate) != str:
            raise ValueError("Must be a string.")
        self.course = Course
        self.typehw = Type
        self.description = Description
        self.duedate = DueDate

        

    def to_dict(self):
        thing = vars(self)
        return thing