from rit_lib import *

class LRUEntry(struct):
    _slots = ((str,'Page'),(int,'Time'))

P1 = LRUEntry("a",100)
P2 = LRUEntry("b",100)

class cake(struct):
    _slots = ((str, 'Page'),(int,'Time'))

x = cake("why", 0)
print(x)