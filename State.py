#A class with table and a father
class  State:
    def __init__(self, table, level=0, father=None):
        self.father = father
        self.table = table
        self.level = level
        self.h = 0
        self.g = 0
        self.f = 0
    def __lt__(self, other):
        return self.f < other.f
