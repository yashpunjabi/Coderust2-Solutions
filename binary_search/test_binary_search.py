import unittest
from binary_search import binary_search

class BinarySearchTests(unittest.TestCase):

    def setUp(self):
        self.arr = [1, 2, 3, 4, 5]

    def testEmptyList(self):
        self.assertEqual(binary_search([], 0), -1)

    def testSingleElementList(self):
        self.assertEqual(binary_search([5], 5), 0)

    def testFirstElement(self):
        self.assertEqual(binary_search(self.arr, self.arr[0]), 0)

    def testLastElement(self):
        self.assertEqual(binary_search(self.arr, self.arr[-1]), len(self.arr)-1)

    def testElement(self):
        self.assertEqual(binary_search(self.arr, 2), 1)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
