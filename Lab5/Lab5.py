__author__ = 'chris'
import unittest
from labs.lab1.triangle import Triangle

class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.triangle0 = Triangle(1, 2, 3, 20, 30)
        print("In TestTriangle.setUp():" + self.triangle0.to_string())
        self.triangle1 = Triangle(1, 2, 77, 20, 230)
        print("In TestTriangle.setUp():" + self.triangle1.to_string())

    def test_get_third_angle(self):
        self.assertEqual(130, self.triangle0.get_third_angle())
        self.assertEqual(60, self.triangle1.get_third_angle())

    def test_has_point(self):
        self.assertTrue(self.triangle0.has_point(1))
        self.assertTrue(self.triangle0.has_point(3))
        self.assertFalse(self.triangle0.has_point(4))
        self.assertTrue(self.triangle1.has_point(77))

