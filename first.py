from operator import  attrgetter
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def __repr__(self):
        return self.name + ":" + str(self.id)

users = [
    User('huang', 43),
    User('Bang', 5),
    User('www', 6),
    User('oxox', 8),
    User('work', 23),
]
for u in sorted(users, key = attrgetter("id")):
    print(u)