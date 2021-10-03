# ToRun
# pytest .\function_test.py


import unittest
from function import minimum_coins_required

class MinimumCoinsTestCase(unittest.TestCase):
    def test_minimum_coins(self):
        self.assertEqual(minimum_coins_required(5), 1)
        self.assertEqual(minimum_coins_required(13), 3)        
        self.assertEqual(minimum_coins_required(38), 5)               
        self.assertEqual(minimum_coins_required(59), 4)
        self.assertEqual(minimum_coins_required(138), 6)
        self.assertEqual(minimum_coins_required(150), 2)
        self.assertEqual(minimum_coins_required(200), 1)        
        self.assertEqual(minimum_coins_required(87), 5)               
        self.assertEqual(minimum_coins_required(0), 0)
        self.assertEqual(minimum_coins_required(38760), 196)
        self.assertEqual(minimum_coins_required('34'), 4)
        self.assertRaises(ValueError, minimum_coins_required, 'bob')
        self.assertRaises(ValueError, minimum_coins_required, '34.56')