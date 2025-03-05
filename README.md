# SIM_Refactoring_Act

Income Calculation Program
Description
This Python program calculates the deductions from an employee's salary and computes the net income after deductions. The deductions include:

SSS (Social Security System): A fixed amount of 1200.
PhilHealth: A 5% contribution of the income, divided by 2.
Pag-IBIG: A fixed amount of 100.
Tax: A fixed amount of 1875.
The program defines a sal_calc class to handle these computations, taking the salary (income) as input.

Features
Takes in the gross salary (income) as input.
Computes deductions for SSS, PhilHealth, Pag-IBIG, and Tax.
Returns both the total deduction amount and the net income (income after deductions).
Requirements
Python 3.x
Code Overview
Class: sal_calculate
Attributes:

income: The gross income of the employee.
sss: Fixed SSS contribution (1200).
philhealth: PhilHealth contribution calculated as 5% of income divided by 2.
pagibig: Fixed Pag-IBIG contribution (100).
tax: Fixed tax contribution (1875).
Methods:

compute_deductions(): Computes and returns the total deductions and the net income (income - total deductions).
display(): Displays the results of the deduction calculation by calling compute_deductions().

Installation
Ensure you have Python 3.x installed on your system.
Download or clone the repository.
Run the Group_Memor.py

License
This code is open-source and can be used freely. Feel free to modify and distribute it as needed.
