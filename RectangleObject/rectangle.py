"""
The following tasks deal with creating data structures and using them.
I would like for you to create a data structure that holds a description of
(or defines) a rectangle.  We will then compute simple things with this 
data structure.

Tasks:

1) Create a data structure (or an object) for a rectangle in the
2-dimensional plane.  The data structure should have the location of 
the rectangle (in the plane) and the size.  Note that for these tasks
the rectangle will not be rotated (it will always be "upright" and never
tilted).  So you can define the rectangle with only four numbers.

2) Create a function (or method, etc) that takes in the rectangle 
data structure and computes the area (size).  Note that you don't need to make
any other functions for other attributes of the rectangle (like perimeter).

3) Create a function that takes in two rectangles and returns a rectangle
that is the intersection (overlap).

4) Call the function that computes the size on the return value of the 
intersection function.  Make sure that it can handle all cases.

"""

import unittest

# 1)
class rectangle:

    def __init__(self, point, height, width):
        '''
        point -> tuple
            Point will be the bottom left point stored in (x, y) format.

        hight -> int or float
            Will be the height of the rectangle being made
        
        width -> int or float
            will the the width of the rectangle
        '''
        assert isinstance(point, tuple), "Incorrect type for point"
        assert len(point) == 2, "Point should be (x, y) IE 2-dim"
        assert isinstance(height, float) or isinstance(height, int), "improper type for height"
        assert isinstance(width, float) or isinstance(width, int), "improper type for height"
        assert height > 0, "Height must be positive and greater than zero"
        assert width > 0, "Width must be positive and greater than zero"

        self.height = height
        self.width = width

        self.set_points(point, height, width)

    def set_points(self, point, height, width):
        '''
        Method constructs all the square points from initial points
            and the length and width components.
        
        point -> tuple
            Point will be the bottom left point stored in (x, y) format.

        hight -> int or float
            Will be the height of the rectangle being made
        
        width -> int or float
            will the the width of the rectangle
        '''

        self.p1 = point # Bottom left
        self.p2 = point[0], point[1] + height # Top left
        self.p3 = point[0] + width, point[1] + height # Top right
        self.p4 = point[0] + width, point[1] # Bottom right
    
    def shift_x(self, x_shift):
        '''
        Method shifts the rectangle by some amount on the x axis

        x_shift -> (int, float)
            The amount to shift the x components by
        '''

        assert isinstance(x_shift, int) or isinstance(x_shift, float), "Improper type for shift"
        self.p1 = self.p1[0] + x_shift, self.p1[1]
        self.p2 = self.p2[0] + x_shift, self.p2[1]
        self.p3 = self.p3[0] + x_shift, self.p3[1]
        self.p4 = self.p4[0] + x_shift, self.p4[1]
    
    def shift_y(self, y_shift):
        '''
        Method shifts the rectangle by some amount on the y axis

        y_shift -> (int, float)
            The amount to shift the y components by
        '''

        assert isinstance(y_shift, int) or isinstance(y_shift, float), "Improper type for shift"
        self.p1 = self.p1[0], self.p1[1] + y_shift
        self.p2 = self.p2[0], self.p2[1] + y_shift
        self.p3 = self.p3[0], self.p3[1] + y_shift
        self.p4 = self.p4[0], self.p4[1] + y_shift
    
    def __str__(self):
        '''
        Defined the print output
        '''
        output = f"p1 = {self.p1} \np2 = {self.p2} \np3 = {self.p3} \np4 = {self.p4} \nheight = {self.height} \nwidth = {self.width}"
        return output 
    
    def __eq__(self, rec):
        '''
        Set the rules for equality operatation
        '''
        rtn_val = self.p1 == rec.p1 and self.p2 == rec.p2 and self.p3 == rec.p3 and self.p4 == rec.p4
        return rtn_val

# 2)
def calc_area(rec):
    '''
    Take in a rectangle and returns the area

    Parameters:
    rec -> rectangle
        The rectangle where the area is going to be calculated
    
    Returns:
    area -> (float, int)
        The area of the rectangle
    '''
    assert isinstance(rec, rectangle), "Must be a rectangle!"
    return rec.height * rec.width

# 3)
def find_new_square(rec1, rec2):
    '''
    Takes in two rectangle objects, find the overlap, and returns a new 
        rectangle is there is an overlap. If no overlap returns 'None'.
    
    Parameters:
    rec1 -> rectangle
        The first rectangle to be used
    
    rec2 -> rectangle
        The second rectangle to be used
    
    Returns:
    new_rec -> rectangle
        The new rectangle the is created from the overlap of the two passed in
        rectangles.
    '''
    
    assert isinstance(rec1, rectangle), "Rec1 must be a rectangle"
    assert isinstance(rec2, rectangle), "Rec2 must be a rectangle"
    if rec1 == rec2:
        return rectangle(rec1.p1, rec1.height, rec2.width)
    elif rec1.p4[0] <= rec2.p1[0] or rec2.p4[0] <= rec1.p1[0]:
        return None
    elif rec1.p1[1] >= rec2.p2[1] or rec2.p1[1] >= rec1.p2[1]:
        return None
    else:
        p1x = max(rec1.p1[0], rec2.p1[0])
        p1y = max(rec1.p1[1], rec2.p1[1])

        p2x = max(rec1.p2[0], rec2.p2[0])
        p2y = min(rec1.p2[1], rec2.p2[1])

        p3x = min(rec1.p3[0], rec2.p3[0])
        p3y = min(rec1.p3[1], rec2.p3[1])

        p4x = min(rec1.p4[0], rec2.p4[0])
        p4y = max(rec1.p4[1], rec2.p4[1])

        return rectangle((p1x, p1y), p2y - p1y, p4x - p1x)

# 4) 
class TestRectangle(unittest.TestCase):

    def test_rectangle_obj_creation(self):
        test_obj = rectangle((0, 0), 1, 1)

        # Should make a 1 x 1 square
        self.assertEqual(test_obj.p1, (0, 0))
        self.assertEqual(test_obj.p2, (0, 1))
        self.assertEqual(test_obj.p3, (1, 1))
        self.assertEqual(test_obj.p4, (1, 0))
    
    def test_area_calc(self):
        test_obj_one = rectangle((0, 0), 2, 3)
        self.assertEqual(calc_area(test_obj_one), 6)

        test_obj_two = rectangle((-2, 17), 4, 4)
        self.assertEqual(calc_area(test_obj_two), 16)

    def test_square_sides_touching(self):
        # L/R edges touching
        t1rec1 = rectangle((0,0), 1, 1)
        t1rec2 = rectangle((1, 0), 1, 1)
        self.assertIsNone(find_new_square(t1rec1, t1rec2))
        self.assertIsNone(find_new_square(t1rec2, t1rec1))

    def test_top_bottom_touching(self): 
        # T/B edges touching
        t2rec1 = rectangle((0, 0), 1, 1)
        t2rec2 = rectangle((0, -1), 1, 1)
        self.assertIsNone(find_new_square(t2rec1, t2rec2))
        self.assertIsNone(find_new_square(t2rec2, t2rec1))

    def test_one_above_other(self):
        # One directly below (No touch)
        t3rec1 = rectangle((0, 0), 1, 1)
        t3rec2 = rectangle((0, 1.5), 1, 1)
        self.assertIsNone(find_new_square(t3rec1, t3rec2))
        self.assertIsNone(find_new_square(t3rec2, t3rec1))

    def test_left_right(self):
        # directly to side (no touch)
        t4rec1 = rectangle((0, 0), 1, 1)
        t4rec2 = rectangle((0, -1.5), 1, 1)
        self.assertIsNone(find_new_square(t4rec1, t4rec2))
        self.assertIsNone(find_new_square(t4rec2, t4rec1))

    def test_not_close(self):
        # Not near each other
        t5rec1 = rectangle((0, 0), 1, 1)
        t5rec2 = rectangle((-2, -2), 1, 1)
        self.assertIsNone(find_new_square(t5rec1, t5rec2))
        self.assertIsNone(find_new_square(t5rec2, t5rec1))

    def test_upper_right_inside(self):
        # One square is lower and right of the other
        t6rec1 = rectangle((0, 0), 1, 1)
        t6rec2 = rectangle((.5, -.5), 1, 1)
        t = rectangle((.5, 0), .5, .5)
        self.assertEqual(find_new_square(t6rec1, t6rec2), t)
        self.assertEqual(find_new_square(t6rec2, t6rec1), t)

    def test_upper_left_inside(self):
        # One square is lower and left of the other
        t7rec1 = rectangle((0, 0), 1, 1)
        t7rec2 = rectangle((-.5, -.5), 1, 1)
        t = rectangle((0, 0), .5, .5)
        self.assertEqual(find_new_square(t7rec1, t7rec2), t)
        self.assertEqual(find_new_square(t7rec2, t7rec1), t)

    def test_same_ys_overlappinng_x(self):
        # Same height, overlapping x
        t8rec1 = rectangle((0, 0), 1, 1)
        t8rec2 = rectangle((.5, 0), 1, 1)
        t = rectangle((.5, 0), 1, .5)
        self.assertEqual(find_new_square(t8rec1, t8rec2), t)
        self.assertEqual(find_new_square(t8rec2, t8rec1), t)

    def test_same_xs_overlapping_y(self):
        # same location different heights (y)
        t9rec1 = rectangle((0, 0), 1, 1)
        t9rec2 = rectangle((0, -.5), 1, 1)
        t = rectangle((0, 0), .5, 1)
        self.assertEqual(find_new_square(t9rec1, t9rec2), t)
        self.assertEqual(find_new_square(t9rec2, t9rec1), t)

    def test_two_points_contained_in_one(self):
        # one is only partially contained in another
        t10rec1 = rectangle((0, 0), 1, 3)
        t10rec2 = rectangle((1, -.5), 1, 1)
        t = rectangle((1, 0), .5, 1)
        self.assertEqual(find_new_square(t10rec1, t10rec2), t)
        self.assertEqual(find_new_square(t10rec2, t10rec1), t)

    def test_one_inside_other(self):
        # one fully contained in another
        t11rec1 = rectangle((0, 0), 3, 3)
        t11rec2 = rectangle((1, 1), 1, 1)
        t = rectangle((1, 1), 1, 1)
        self.assertEqual(find_new_square(t11rec1, t11rec2), t)
        self.assertEqual(find_new_square(t11rec2, t11rec1), t)

    def test_same_square(self):
        # same square
        t12rec1 = rectangle((0, 0), 3, 3)
        t12rec2 = rectangle((0, 0), 3, 3)
        t = rectangle((0, 0), 3, 3)
        self.assertEqual(find_new_square(t12rec1, t12rec2), t)
        self.assertEqual(find_new_square(t12rec2, t12rec1), t)

    def test_square_formed_from_overlap(self):
        # large overlap in the middle of both
        t13rec1 = rectangle((0, 0), 1, 3)
        t13rec2 = rectangle((1, -.5), 2, 1)
        t = rectangle((1, 0), 1, 1)
        self.assertEqual(find_new_square(t13rec1, t13rec2), t)
        self.assertEqual(find_new_square(t13rec2, t13rec1), t)

    def test_shift_x(self):
        t14rec1 = rectangle((0, 0), 1, 1)
        result1 = rectangle((1, 0), 1, 1)
        t14rec1.shift_x(1)
        self.assertEqual(t14rec1, result1)

        result2 = rectangle((-1, 0), 1, 1)
        t14rec1.shift_x(-2)
        self.assertEqual(t14rec1, result2)

    def test_shift_y(self):
        t15rec1 = rectangle((0, 0), 1, 1)
        result = rectangle((0, 1), 1, 1)
        t15rec1.shift_y(1)
        self.assertEqual(t15rec1, result)

        result = rectangle((0, -1), 1, 1)
        t15rec1.shift_y(-2)
        self.assertEqual(t15rec1, result)
        

if __name__ == '__main__':
    unittest.main()