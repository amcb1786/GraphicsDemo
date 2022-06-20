from graphics import *
# Begin by calling for attributes that will define shape
# Name the class
class Point:
    def __init__(self, x,y):
       self.x = x
       self.y = y
    def __str__(self):
     return "({},{})".format( self.x, self.y)

class Rectangle:
    def __init__(self, posn, w, h):
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
     return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

 def create_rectangle(x,y,width,height):
    posn = Point(x ,y)
    rect = Rectangle(posn,width,height)
    return rect
 def str_rectangle(rect):
    return str(rect)

def shift_rectangle(rect, dx,dy):
    xx, yy = rect.corner.x + rect.corner.y
    rect.corner.x = xx + dx
    rect.corner.y = yy + dy

def offset_rectangle(rect, dx,dy):
    return create_rectangle(xx +dx, yy +dy,rect.width , rect.height)
#Testing the code

r1 = create_rectangle(10, 20, 30, 40)
print(str_rectangle(r1))
shift_rectangle(r1, -10, -20)
print(str_rectangle(r1))

r2 = offset_rectangle(r1, 100, 100)
print(str_rectangle(r1)) # should be same as previous
print(str_rectangle(r2))
