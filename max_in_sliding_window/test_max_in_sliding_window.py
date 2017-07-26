import unittest
from max_in_sliding_window import max_in_sliding_window

class MaxInSlidingWindowTests(unittest.TestCase):

    def setUp(self):
        self.arr = [1,2,-1,6,-5,4,3,0]
        self.window_size = 3
        self.expected_output = [2, 6, 6, 6, 4, 4]

    def testTooSmallList(self):
        self.assertEqual(max_in_sliding_window([], self.window_size), [])
        self.assertEqual(max_in_sliding_window([1, 2], self.window_size), [])

    def testInvalidWindowSize(self):
        self.assertRaises(ValueError, max_in_sliding_window, self.arr, 0)
        self.assertRaises(ValueError, max_in_sliding_window, self.arr, -1)

    def testValidInput(self):
        self.assertEqual(max_in_sliding_window(self.arr, self.window_size),
            self.expected_output)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
