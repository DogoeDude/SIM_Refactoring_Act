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

**Report Outline**

**Technical Debt Identified**

Before refactoring, the original code had several issues contributing to technical debt:

1.) Lack of Modularity - The function compute_deductions handled all computations and print statements, making it difficult to maintain or extend.

2.) Global Scope Issues - The salary input was obtained outside of a function, limiting reusability.

3.) Hardcoded Values - Values such as SSS, Pag-IBIG, and tax were defined as fixed constants without clear encapsulation.

4.) Lack of Encapsulation - The function performed multiple tasks, including calculation and display, instead of separating concerns.

**Refactoring Improvements Made**

To address the technical debt, we implemented the following improvements:

1.) Object-Oriented Programming (OOP) Approach - We introduced a class sal_calc to encapsulate salary computation, improving organization and reusability.

2.) Encapsulation of Computations - Salary components such as deductions and net salary were encapsulated into methods, improving clarity.

3.) Improved Readability - Using f-strings for formatted output and meaningful method names (compute_deductions, compute_net_income, display_Payroll) enhanced code readability.

4.) Error Handling - We added a try-except block to handle invalid user inputs gracefully.

5.) Main Guard (if __name__ == "__main__":) - Ensured that the script runs properly when executed as a standalone file, making it more robust for reuse in other projects.

**Challenges Faced & Solutions**

**1. Git Collaboration Issues**

Challenge:

There were existing Git accounts on the school computer, which caused conflicts when pushing changes.

Unexpected delays occurred due to authentication and access issues.

Solution:

We configured Git by setting up local repositories and managing credentials correctly.

Used git config --global user.name and git config --global user.email to ensure proper identity configuration.

Reset credentials where necessary and ensured smooth access to the remote repository.

**2. Effective Refactoring Approach**

Challenge:

The team needed to decide on the best way to refactor the code for maintainability.
Initially, we considered simply restructuring the function, but we opted for an OOP approach for better scalability.

Solution:

-We mapped out the existing issues in the code and identified areas that could benefit from encapsulation.

-Applied OOP principles to improve code organization and reusability.

-Conducted code reviews to ensure everyone understood the refactoring changes.

**3. Unit Testing**

To ensure the correctness of our refactored code, we implemented unit tests using Python's unittest framework. The tests validate salary computations for various income levels, confirming that deductions and net           salaries are accurately calculated. These tests are stored in a separate file, ensuring that our main script remains clean and focused on computation. With unit tests in place, we can confidently maintain and extend       our codebase while minimizing the risk of introducing errors.

By addressing these issues, we successfully improved the maintainability and efficiency of the salary computation code.

