import unittest
from hex_calculator import calculator

class test_hex_mean(unittest.TestCase):

    def test_many(self):
        self.assertEqual(calculator.hex_mean(
        ["004b9d",
        "202f55",
        "13c2f0",
        "003882",
        "2472ce",
        "0d2b60",
        "123576"]), '115393')
    
    def test_none(self):
        self.assertEqual(calculator.hex_mean([]), '000000')
    
    def test_one(self):
        self.assertEqual(calculator.hex_mean(['004b9d']), '04b9d')
    
    def test_non_string(self):
        with self.assertRaises(ValueError):
            calculator.hex_mean([0x004b9d])
        
    def test_non_list(self):
        with self.assertRaises(TypeError):
            calculator.hex_mean(0x004b9d)
    
class test_mean(unittest.TestCase):
    
    def test_mean(self):
        self.assertEqual(calculator.mean([1, 2]), 2)

    def test_0_mean(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.mean([])
    
    def test_negative_mean(self):
        self.assertEqual(calculator.mean([-4, 2]), 1)
    
    def test_float_mean(self):
        self.assertEqual(calculator.mean([1.5, 10]), 6)
    
    def test_bool_mean(self):
        self.assertEqual(calculator.mean([True, False]), 0)

class test_hex_to_rgb(unittest.TestCase):

    def test_string(self):
        self.assertEqual(calculator.hex_to_RGB(['004b9d','202f55']),
                                               ([0, 32], [75, 47], [157, 85]))
    
    def test_empty(self):
        self.assertEqual(calculator.hex_to_RGB([]), ([],[],[]))
    
    def test_non_string(self):
        with self.assertRaises(ValueError):
            calculator.hex_to_RGB([0x004b9d])
        
    def test_non_hex_string(self):
        with self.assertRaises(ValueError):
            calculator.hex_to_RGB(['a', 'b'])
            


if __name__ == '__main__':
    unittest.main()