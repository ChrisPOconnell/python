__author__ = 'chris'

'''
Intent: define a triangle with (2 sufficient) angles and 3 vertex points (denoted by an integer)
Precondition: a_point1, a_point2, and a_point3 are distinct non-negative integers

Postcondition 1: triangle_number = available_triangle_number
AND available_triangle_number = old(available_triangle_number) + 1

Postcondition 2: point1 = a_point1, point2 = a_point2, and point3 = a_point3

Postcondition 3:
an_angle1 > 0 AND an_angle2 > 0 AND an_angle1 + an_angle2 < 180
--OR--
Above not all true, AND an equilateral triangle created AND notice is on monitor
'''

class Triangle:
    available_triangle_number = 0
    def __init__(self, a_point1, a_point2, a_point3, an_angle1, an_angle2):
        # Postcondition 2 fulfilled:
        self.point1, self.point2, self.point3 = a_point1, a_point2, a_point3
        self.angle1, self.angle2 = an_angle1, an_angle2
        # Postcondition 3 fulfilled:
        if an_angle1 <= 0 or an_angle2 <= 0 or an_angle1 + an_angle2 >= 180:
            print("\nBad angles supplied; equilateral triangle created instead")
            self.angle1, self.angle2 = 60, 60  # default

    def get_third_angle(self):  # Returns angle other than angle1 and angle2
        return 180 - self.angle1 - self.angle2

    def has_point(self, a_point):
        # Intent: whether or not a_point is a vertex of this triangle
        return a_point == self.point1 or a_point == self.point2 or a_point == self.point3

    def to_string(self):  # pedagogical: standard name for "this object in the form of a string"
        # Postcondition 1 fulfilled:
        self.triangle_number = Triangle.available_triangle_number
        Triangle.available_triangle_number += 1
        return "\nTriangle {0}: Angles {1}, {2}, {3}; Vertices {4}, {5}, {6}".format \
        (self.triangle_number, self.angle1, self.angle2, self.get_third_angle(), \
        self.point1, self.point2, self.point3)




