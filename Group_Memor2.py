class sal_calc:
    def __init__(self, income):
        self.income = income
        self.sss = 1200
        self.philhealth = (income * 0.05) / 2
        self.pagibig = 100
        self.tax = 1875

    def compute_deductions(self):
        deduction = self.sss + self.philhealth + self.pagibig + self.tax
        net_income = self.income - deduction
        return deduction, net_income
    
    def display_calculation(self):
        deduction, net_income = self.compute_deductions()
        return f"Deduction: {deduction}, Net Income: {net_income}"

#Function finish
try:
    user_input = int(input("Enter your income: "))
    calc = sal_calc(user_input)
    print(calc.display())
except ValueError:
    print("Invalid input. Please enter a number.")