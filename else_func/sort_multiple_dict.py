orders = [
  {'id': 1, 'name': 'Ashley', 'date': '2020-05-20'},
  {'id': 2, 'name': 'Peter' , 'date': '2020-05-20'},
  {'id': 3, 'name': 'Ashley', 'date': '2020-05-05'},
  {'id': 4, 'name': 'John'  , 'date': '2020-05-05'},
  {'id': 5, 'name': 'Peter' , 'date': '2020-05-05'},
]

def orderBy(by, ascending=[]):
    class K:
        def __init__(self, o, *args):
            self.o = o

        def __lt__(self, other):
            for i, key in enumerate(by):
                asc = ascending[i] if i < len(ascending) else True
            if self.o[key] < other.o[key]: return asc
            if self.o[key] > other.o[key]: return not asc

    return K

print( sorted(orders, key=orderBy(['name'])) )
