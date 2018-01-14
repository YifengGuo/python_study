from Point import Point
import copy
class Rectangle(object):
    def __init__(self, height, width, corner):
        self.height = height
        self.width = width
        self.corner = corner

    def find_center(self):
        center_x = self.corner.x + 0.5 * self.width
        center_y = self.corner.y + 0.5 * self.height
        center = Point(center_x, center_y)
        return center

    def move_rectangle(self, dx, dy):
        self.corner.x += dx
        self.corner.y += dy

# Write a version of move_rectangle that creates and returns a new Rectangle instead
# of modifying the old one.

def move_rectangle_2(rec, dx, dy):
    '''
    use deep copy
    '''
    cp = copy.deepcopy(rec)
    cp.corner.x += dx
    cp.corner.y += dy
    return cp
    

corner = Point(0, 0)
box = Rectangle(100,200,corner)
print box.find_center()
box.move_rectangle(50, 50)
print box.corner # print coordinate of corner

cp = move_rectangle_2(box, 50, 50)
print cp.corner 
print cp.corner is box.corner # False
print cp.corner == box.corner # False
