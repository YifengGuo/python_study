import numpy as np
class Point(object):
    def __init__(self, x, y):
    	self.x = x
    	self.y = y

    def __str__(self):
        return '(%d, %d)' %(self.x, self.y)


a1 = Point(3, 4)
a2 = Point(-2, -1)

def calc_distance(a1, a2):
    res = np.sqrt((a2.x- a1.x)**2 + (a2.y - a1.y)**2)
    return res

print 'distance between a1 and a2 is %f: ' %(calc_distance(a1, a2))

