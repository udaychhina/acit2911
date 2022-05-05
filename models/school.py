import json
from models.homework import Homework
class School:
    def __init__(self, name):
        self.name = name
        self.hwlist = []
        with open("data/homework.json", 'r') as fp:
            data = json.load(fp)
            for homework in data:
                self.hwlist.append(Homework(homework["course"],\
                homework["name"], homework["typehw"], homework["description"],\
                homework["duedate"],homework["completed"]))

    def __len__(self):
        return len(self.hwlist)

    def add(self, hwinstance):
        if type(hwinstance) == Homework:
            self.hwlist.append(hwinstance)

    def save(self):    
        holder = []
        for i in range(len(self.hwlist)):
            thing = self.hwlist[i].to_dict()
            holder.append(thing)
        with open(r"data/homework.json", 'w') as fp:
            json.dump(holder, fp)