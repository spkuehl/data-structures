import unittest
from arrays import find_missing_integer_array

class FindMissingIntegerArray(unittest.TestCase):

    def test_missing_number_is_5(self):
        self.assertEqual(find_missing_integer_array((1,2,3,4,6)), 5)


if __name__ == '__main__':
    unittest.main()
