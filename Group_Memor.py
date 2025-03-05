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
    
    def display(self):
        return self.compute_deductions()


calc = sal_calc(20000)#Function finish
