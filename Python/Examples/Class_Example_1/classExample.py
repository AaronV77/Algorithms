#!/usr/bin/Python

#An example of a class
class Shape:

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.description = "This shape has not been described yet."
    self.author = "Nobody has claimed to make this shape yet."

  def area(self):
    return self.x * self.y

  def perimeter(self):
    return 2 * self.x + 2 * self.y

  def describe(self, text):
    self.describe = text

  def authorName(self, text):
    self.author = text

  def scaleSize(self, scale):
    self.x = self.x * scale
    self.y = self.y * scale

rectangle = Shape(100, 20)
square = Shape(20, 20)

print("Rectangle primeter is: " + str(rectangle.perimeter()) + " Square primeter is: " + str(square.perimeter()) + ".")
