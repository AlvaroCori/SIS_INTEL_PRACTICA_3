#A class with table and a father
class  State:
    def __init__(self, table, father=None):
        self.father = father
        self.table = table
        self.h = 0
        self.g = 0
        self.f = 0
    #When we use PriorityQueue we need a function that order the elements by f.
    def __lt__(self, other):
        return self.f < other.f
