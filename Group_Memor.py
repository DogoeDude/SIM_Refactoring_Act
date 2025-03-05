class sal_calc:
    def __init__(self, income):
        self.income = income
        self.sss = 1200
        self.philhealth = (income * 0.05) / 2
        self.pagibig = 100
        self.tax = 1875

    def compute_deductions(self):
        return self.sss + self.philhealth + self.pagibig + self.tax

    def compute_net_income(self):
        return  self.income - self.compute_deductions()

    def display_Payroll(self):
        print(f"Gross Salary: {self.income:.2f}")
        print(f"SSS Deduction: {self.sss:.2f}")
        print(f"PhilHealth Deduction: {self.philhealth:.2f}")
        print(f"Pag-IBIG Deduction: {self.pagibig:.2f}")
        print(f"Tax Deduction: {self.tax:.2f}")
        print(f"Total Deductions: {self.compute_deductions():.2f}")
        print(f"Net Salary: {self.compute_net_income():.2f}")


Salary = float(input("Enter your monthly salary: "))
payroll = sal_calc(Salary)
payroll.display_Payroll()