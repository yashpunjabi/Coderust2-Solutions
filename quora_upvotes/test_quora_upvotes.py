import unittest
from quora_upvotes import quora_upvotes, countRanges

class QuoraUpvotesTests(unittest.TestCase):

    def setUp(self):
        self.arr = [1,2,3,1,1]
        self.window_size = 3
        self.expected_output = [3,0,-2]

    def testCountRanges(self):
        ranges = [(1,3), (3,4)]
        expected = 1 + 0
        self.assertEqual(countRanges(ranges), expected)

    def testValidInput(self):
        self.assertEqual(quora_upvotes(self.arr, self.window_size),
            self.expected_output)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
