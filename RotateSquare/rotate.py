from rectangle import Rectangle
import unittest

def rotate(matrix, direction):
    rec = Rectangle(matrix)
    if direction == "clockwise":
        return rec.rotate_clockwise()
    return rec.rotate_counter_clockwise()

class TestRotateFunction(unittest.TestCase):
    def test_case_square(self):
        matrix = [[1,2,3],
                  [4,5,6],
                  [7,8,9]]
        
        self.assertEqual(rotate(matrix, 'counter-clockwise'), [[3,6,9],[2,5,8],[1,4,7]])
        self.assertEqual(rotate(matrix, 'clockwise'), [[7,4,1],[8,5,2],[9,6,3]])
        self.assertEqual(rotate(rotate(matrix, 'counter-clockwise'), 'clockwise'), [[1,2,3],[4,5,6],[7,8,9]])
        self.assertEqual(rotate(rotate(rotate(rotate(matrix, 'clockwise'), 'clockwise'), 'clockwise'), 'clockwise'), [[1,2,3],[4,5,6],[7,8,9]])
    
    def test_unequal_square(self):
        matrix = [[1,2,3],
                  [4,5,6],
                  [7,8,9],
                  [10,11,12]]
        
        self.assertEqual(rotate(matrix, 'counter-clockwise'), [[3,6,9,12],[2,5,8,11],[1,4,7,10]])
        self.assertEqual(rotate(matrix, 'clockwise'), [[10,7,4,1],[11,8,5,2],[12,9,6,3]])

    def test_single(self):
        '''Test single row column'''
        matrix = [[1,2,3]]
        
        self.assertEqual(rotate(matrix, 'counter-clockwise'), [[3],[2],[1]])
        self.assertEqual(rotate(matrix, 'clockwise'), [[1],[2],[3]])
        self.assertEqual(rotate(rotate(matrix, 'clockwise'), 'clockwise'), [[3,2,1]])


if __name__ == '__main__':
    unittest.main()