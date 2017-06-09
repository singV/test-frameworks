import math

class Square(object):
     def __init__(self, radius):
         self.radius = radius

     def calculate_area(self):
         return math.sqrt(self.radius) * math.pi
