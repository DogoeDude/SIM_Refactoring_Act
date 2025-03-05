SalaryCalculator Class
---------------------
A simple class to calculate salary deductions and net pay in the Philippines.

### Attributes:
- income: Monthly gross salary (float)
- sss: SSS contribution (fixed at 1200)
- philhealth: PhilHealth contribution (2.5% of salary)
- pagibig: Pag-IBIG contribution (fixed at 100)
- tax: Income tax (fixed at 1875)

### Methods:
- compute_deductions(): Returns tuple of (total_deductions, net_salary)
- display(): Prints detailed breakdown of salary and deductions

### Usage:
    calc = SalaryCalculator(20000)
    calc.display()

### Improvements from Procedural to OOP:
1. Encapsulation: 
   - All salary-related data and calculations are bundled together in one class
   - Easier to maintain and modify related functionality

2. Reusability: 
   - Can create multiple calculator instances with different salaries
   - Can use calculations without printing (just call compute_deductions())

3. Organization: 
   - Clear separation of data (attributes) and behavior (methods)
   - More readable and structured code

4. Extensibility: 
   - Easy to add new features (e.g., new deduction types) by adding attributes/methods
   - Can inherit from this class for specialized calculators

5. State Management: 
   - Each calculator instance maintains its own state (salary and deductions)
   - No need to pass variables around between functions

The OOP approach makes the code more robust, flexible, and suitable for expansion compared to the original procedural version, while maintaining the same core functionality.
