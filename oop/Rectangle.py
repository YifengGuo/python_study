from Point import Point
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

corner = Point(0, 0)
box = Rectangle(100,200,corner)
print box.find_center()
box.move_rectangle(50, 50)
print box.corner # print coordinate of corner