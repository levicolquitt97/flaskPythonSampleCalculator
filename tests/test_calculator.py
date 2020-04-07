# LEVI COLQUITT
# Assignment 2 STQA
# 3/15/2020
# Unit tester for calculator file
import unittest
import calculator


class TestCalc(unittest.TestCase):
    # The following test will just test the accuracy of the BMI function
    # Since the Flask forms are how we keep out undesireable values these
    # tests wont tell us if the range is correct rather if the formulas are correct

    # These tests are not 'on' or 'off a boundary because the boundary is not implemented
    # In the calculator.py however using these as our initial tests will allow their resuse later
    def test_BMICalcOffLower(self):
        result = calculator.BMICalc(0, -1, -1, 1, ' ')
        self.assertEqual(result, (-719.9999999999999, ' weight category: Underweight'))

    def test_BMICalcOnLower(self):
        result = calculator.BMICalc(1, 0, 0, 1, ' ')
        self.assertEqual(result, (0.0, ' weight category: Underweight'))

    def test_BMICalcInterior(self):
        result = calculator.BMICalc(5, 3, 125, 1, ' ')
        self.assertEqual(result, (22.67573696145124, ' weight category: Normal weight'))

    def test_BMICalcOnUpper(self):
        result = calculator.BMICalc(12, 12, 1000, 1, ' ')
        self.assertEqual(result, (29.585798816568044, ' weight category: Overweight'))

    def test_BMICalcOffUpper(self):
        result = calculator.BMICalc(13, 13, 1001, 1, ' ')
        self.assertEqual(result, (25.23441055985434, ' weight category: Overweight'))

    def test_BMICalcObese(self):
        result = calculator.BMICalc(4, 10, 400, 1, ' ')
        self.assertEqual(result, (85.61236623067775, ' weight category: Obese'))

    # The following test will just test the accuracy of the retirement function
    # Since the Flask forms are how we keep out undesireable values these
    # tests wont tell us if the range is correct rather if the formulas are correct

    # These tests are not 'on' or 'off a boundary because the boundary is not implemented
    # In the calculator.py however using these as our initial tests will allow their resuse later
    def test_retirementCalcOffLower(self):
        result = calculator.retirementCalc(-1, -1, -1, -1, ' ')
        self.assertEqual(result, ("You will have saved: $0.0135 By age: 0 Which meets your savings goal of: $-1"))

    def test_retirementCalcOnLower(self):
        result = calculator.retirementCalc(0, 0, 0, 0, ' ')
        self.assertEqual(result, ("You will have saved: $0.0 By age: 1 Which meets your savings goal of: $0"))

    def test_retirementCalcInterior(self):
        result = calculator.retirementCalc(22, 60000, 10, 50000, ' ')
        self.assertEqual(result, ("You will have saved: $56700.0 By age: 29 Which meets your savings goal of: $50000"))

    def test_retirementCalcOnUpper(self):
        result = calculator.retirementCalc(99, 1000000000, 99, 100000000, ' ')
        self.assertEqual(result, ("You will have saved: $1336500000.0 By age: 100 Which meets your savings goal of: $100000000"))

    def test_retirementCalcOffUpper(self):
        result = calculator.retirementCalc(100, 100000000, 100, 100000000, ' ')
        self.assertEqual(result, ("You will have saved: $135000000.0 By age: 101 Which meets your savings goal of: $100000000"))


if __name__ == '__main__':
    unittest.main()
