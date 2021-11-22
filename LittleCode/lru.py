'''
Implement a Least Recently Used (LRU) cache structure that holds onto the N 
most recently accessed items. The order of access (from most recently accessed to least recently accessed) 
within the cache shall be maintained at all times. Whenever a new access is attempted, 
the item accessed becomes “most recently used”. If doing so adds a new item to the cache, 
and would cause the cache to exceed N items, the least recently used item in the cache should be evicted.

Data structure containing 'N' items
Order from most recent to least recent
can try to use a value
    If value is there, it is made most recently used
    if it is not, then it is added to most recently used
        May bump least recent out

test_obj = LRU(5)

test_obj.lst.append(1)
test_obj.lst.append(2)
test_obj.lst.append(3)
test_obj.lst.append(4)

test_obj.access(4)

print(test_obj.lst)

test_obj = LRU(5)

test_obj.lst.append("a")
test_obj.lst.append("c")
test_obj.lst.append(1)
test_obj.lst.append("7")
test_obj.lst.append(2)

test_obj.access(5)

print(test_obj.lst)

'''

import unittest

class LRU:

    def __init__(self, N):
        self.size = N
        self.lst = []

    def shift_item(self, item):
        for idx in range(self.lst.index(item) -1, -1, -1):
            self.lst[idx + 1] = self.lst[idx]
            self.lst[idx] = item

    def access(self, item):
        if item in self.lst:
            self.shift_item(item)
        else:
            if len(self.lst) < self.size:
                self.lst.append(item)
                self.shift_item(item)
            else:
                self.lst[-1] = item
                self.shift_item(item)


class TestLRU(unittest.TestCase):
    def test_data(self):
        '''
        tests access w/ empty list
        test access while list is still filling
        test access with item already existing in list but not full
        test fill entire list
        test adding new item with full list
        test accessing item within full list
        '''
        test_obj = LRU(5)
        test_data = [1, 2, 3, 2, 1, 5, 6, 2, 1, 4, 7, 9]
        correct = [
            [1],
            [2, 1],
            [3, 2, 1],
            [2, 3, 1],
            [1, 2, 3],
            [5, 1, 2, 3],
            [6, 5, 1, 2, 3],
            [2, 6, 5, 1, 3],
            [1, 2, 6, 5, 3],
            [4, 1, 2, 6, 5],
            [7, 4, 1, 2, 6],
            [9, 7, 4, 1, 2]
        ]

        for data, ans in zip(test_data, correct):
            test_obj.access(data)
            self.assertEqual(test_obj.lst, ans)
        

if __name__ == '__main__':
    unittest.main()
