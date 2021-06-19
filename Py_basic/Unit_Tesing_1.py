import unittest
import calc

class TestCalc(unittest.Testcase):
    def test_add(self):
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(-1,1),0)
        self.assertEqual(calc.add(-1,-1),-2)

if __name__ == '__main__':
    unittest.main()
