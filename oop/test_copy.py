import copy
from Point import Point
p1 = Point(1, 2)
p2 = copy.copy(p1) # shallow copy
# shallow copy copies the object and any references it contains
# but not the embedded objects

print p1 == p2 # False
print p1 is p2 # False, for we have not overrided yet


# deep copy
# copy the object and the objects it contains
# so all the copied objects are new