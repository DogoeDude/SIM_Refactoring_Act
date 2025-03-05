import unittest
from Group_Memor import sal_calc

class TestSalCalc(unittest.TestCase):

    # Test case 1: Test compute_deductions for an income of 20000
    def test_compute_deductions_20000(self):
        calc = sal_calc(20000)
        expected_deduction = 1200 + (20000 * 0.05) / 2 + 100 + 1875
        expected_net_income = 20000 - expected_deduction
        deduction, net_income = calc.compute_deductions()
        
        self.assertEqual(deduction, expected_deduction)
        self.assertEqual(net_income, expected_net_income)
    
    # Test case 2: Test compute_deductions for an income of 50000
    def test_compute_deductions_50000(self):
        calc = sal_calc(50000)
        expected_deduction = 1200 + (50000 * 0.05) / 2 + 100 + 1875
        expected_net_income = 50000 - expected_deduction
        deduction, net_income = calc.compute_deductions()
        
        self.assertEqual(deduction, expected_deduction)
        self.assertEqual(net_income, expected_net_income)

    # Test case 3: Test the display method for an income of 30000
    def test_display_30000(self):
        calc = sal_calc(30000)
        expected_deduction = 1200 + (30000 * 0.05) / 2 + 100 + 1875
        expected_net_income = 30000 - expected_deduction
        deduction, net_income = calc.display()
        
        self.assertEqual(deduction, expected_deduction)
        self.assertEqual(net_income, expected_net_income)

if __name__ == '__main__':
    unittest.main()
