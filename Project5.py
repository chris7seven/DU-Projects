# Christopher Seven
# Python Software Development Project 5

import math

# Beginning with a general class for all shapes. This only contains the color of the shape.
class shape:
    def __init__(self, color):
        self.color = color
    # The area and the perimeter are unable to be calculated without additional information.
    def area(self):
        return NotImplemented
    def perimeter(self):
        return NotImplemented
    def __str__(self):
        return f'This shape is color {self.color}'

# Building the polygon class, which introduces a number of additional properties such as the number of sides and sidelength. Note, we are assuming the polygons are regular.
class polygon(shape):
    def __init__(self, color, numsides, sidelength, regular = True):
        super(polygon, self).__init__(color)
        self.numsides = numsides
        self.sidelength = sidelength
    # The area calculation can now be implemented, assuming polygon is normal.
    def area(self):
        area = (self.numsides * self.sidelength * (1/math.tan(math.pi/self.sidelength))/4)
        self.area = area
    # Perimeter calculation can be conducted as well.
    def perimeter(self):
        perimeter = (self.numsides * self.sidelength)
        self.perimeter = perimeter
    def __str__(self):
        return f'This polygon is color {self.color} with {self.numsides} sides of length {self.sidelength}.'

# Moving on to shapes that have 4 sides with angle restrictions. Only 2 angles are requested, since the other 2 must be equal.
class parallelogram(polygon):
    def __init__(self, color, sidelength, slantlength, angle1, angle2, numsides = 4):
        super(parallelogram, self).__init__(color, numsides, sidelength)
        self.slantlength = slantlength
        self.angle1 = angle1
        self.angle2 = angle2
    # Accounting for multiple area scenarios based on the angles given.
    def area(self):
        if self.angle1 < 90:
            height = math.sin(self.angle1 * math.pi / 180) * self.slantlength
            return self.sidelength * height
        elif self.angle1 == 90:
            return self.sidelength * self.slantlength
        else:
            height = math.sin(self.angle2 * math.pi / 180) * self.slantlength
            return self.sidelength * height
    # The perimeter is relatively easy to calculate.
    def perimeter(self):
        perimeter = 2*self.slantlength + 2*self.sidelength
        return perimeter
    def __str__(self):
        return f'This parallelogram is color {self.color} with a sidelength of {self.sidelength} and a slantlength of {self.slantlength}.'

# The rectangle class restricts the parallelogram class even more by supplying more values (such as the angles).
class rectangle(parallelogram):
    def __init__(self, color, length, width, angle=90, angle2=90, numsides = 4):
        super(rectangle, self).__init__(color, length, width, angle1 = 90, angle2 = 90)
        self.length = length
        self.width = width
    # Area and perimeter are both very simple here.
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2*self.length + 2 * self.width
    def __str__(self):
        return f'This rectangle is color {self.color} with a length of {self.length} and a width of {self.width}.'

# The rhombus class also pulls from parallelograms, but simply needs 1 length input.
class rhombus(parallelogram):
    def __init__(self, color, length, angle1, angle2, numsides = 4):
        super(rhombus, self).__init__(color, length, length, angle1, angle2)
        self.length = length
    # Just as in the parallelogram class, the area calculation requires switching from radians to degrees.
    def area(self):
        return self.length * self.length * math.sin(self.angle1 * math.pi / 180)
    # Perimeter is straightforward.
    def perimeter(self):
        return 4 * self.length
    def __str__(self):
        return f'This rhombus is color {self.color} with a length of {self.length} and angles of {self.angle1} and {self.angle2}.'

# Square inherits from rectangle, and thus inherits more than any other class in the program.
class square(rectangle):
    def __init__(self, color, length, angle1 = 90, angle2 = 90, numsides = 4):
        super(square, self).__init__(color, length, length)
        self.length = length
    # The area and perimeter are easy to find.
    def area(self):
        return self.length * self.length
    def perimeter(self):
        return 4 * self.length
    def __str__(self):
        return f'This square is color {self.color} with a length of {self.length}.'

# Pentagon takes a step back and inherits from polygon.
class pentagon(polygon):
    def __init__(self, color, sidelength, numsides = 5):
        super(pentagon, self).__init__(color, sidelength, numsides)
    # Using the formula for pentagon area, we don't need to know any angles since they are all the same (360/5).
    def area(self):
        return (1/4)*math.sqrt(5*(5 + 2*math.sqrt(5)))*self.sidelength*self.sidelength
    def perimeter(self):
        return 5 * self.sidelength
    def __str__(self):
        return f'This pentagon is color {self.color} with a sidelength of {self.sidelength}.'

# Triangle takes in 3 lengths, so as to account for more than just equilateral triangles.
class triangle(polygon):
    def __init__(self, color, length1, length2, length3, numsides = 3):
        super(triangle, self).__init__(color, length1, numsides)
        self.length1 = length1
        self.length2 = length2
        self.length3 = length3
    # Finding the height, and then using it to find the area.
    def area(self):
        s = (self.length1 + self.length2 + self.length3)/2
        return math.sqrt(s*(s-self.length1)*(s-self.length2)*(s-self.length3))
    def perimeter(self):
        return self.length1 + self.length2 + self.length3
    def __str__(self):
        return f'This triangle is color {self.color} with sidelengths of {self.length1},{self.length2},{self.length3}.'

# Circle inherits from shape, and thus just takes in the color.
class circle(shape):
    def __init__(self, color, radius):
        super(circle, self).__init__(color)
        self.radius = radius
    # The area and perimeter calculations are straightforward, simply relying on the radius.
    def area(self):
        return math.pi * self.radius * self.radius
    def perimeter(self):
        return 2 * self.radius * math.pi
    def __str__(self):
        return f'This circle is color {self.color} with a radius of {self.radius}.'

# Oval also inherits from shape, but needs 2 inputs for the 2 different radii.
class oval(shape):
    def __init__(self, color, lengthradius, heightradius):
        super(oval, self).__init__(color)
        self.lengthradius = lengthradius
        self.heightradius = heightradius
    # Area is easy to find, but perimeter is actually tricky.
    def area(self):
        return self.lengthradius * self.heightradius * math.pi
    # This is simply an estimate of the perimeter of the oval.
    def perimeter(self):
        return 2 * math.pi * math.sqrt((self.heightradius*self.heightradius + self.lengthradius*self.lengthradius)/2)
    def __str__(self):
        return f'This oval is color {self.color} with a radii of {self.lengthradius} and {self.heightradius}.'

