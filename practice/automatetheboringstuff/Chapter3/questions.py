"""
1. Why are functions advantageous to have in your programs?
A: Functions are the primary way to compartmentalize your code into logical groups.
Since the variable in functions exist in their own local scops, the code in one function
cannot directly affect the values of variables in other functions. This limits what code
could be changing the values of your variables, which can be helpful when it comes to debugging
your code

2. When does the code in a function execute: when the function is defined or when the function is called?
A: A function call is just the function's name followed by parentheses, possibly with some number of argumentss in between the parentheses.

3. What statement creates a function?
A: def

4. What is the difference between a function and a function call?

Q:

5. How many global scopes are there in a Python program? How many local scopes?
A: There is only one global scope, and it is created when your program begins
local scope: you can use many as you want.
Q:

6. What happens to variables in a local scope when the function call returns?
it will return the value of the variable.
Q:

7. What is a return value? Can a return value be part of an expression?
When you call the len() function and pass it to an argument such as 'Hello, the function call evaluates
to the integer value 5, which is the length of the string you passed it. In general, the value that a function call
evaluates to is called the return value of the function.
Yes, when an expression is used with a return statement, the return value is what this expressin evaluates to.


8. If a function does not have a return statement, what is the return value of a call to that function?
None, which represents the absence of a value.

Q:

9. How can you force a variable in a function to refer to the global variable?

If a variable is being used in the global scope (that is, outside of all functions), then it is always a global variable.

If there is a global statement for that variable in a function, it is a global variable.

Otherwise, if the variable is used in an assignment statement in the function, it is a local variable.

But if the variable is not used in an assignment statement, it is a global variable.


10. What is the data type of None?
None is the only value of the NoneType data type.

11. What does the import areallyourpetsnamederic statement do?

Q:

12. If you had a function named bacon() in a module named spam, how would you call it after importing spam?

Q:

13. How can you prevent a program from crashing when it gets an error?
spam.bacon()


14. What goes in the try clause? What goes in the except clause?
Errors can be handled with try and except statements.
The code that could potentially have an error is put in a try clause.
The program execution moves to the start of a following except clause if an error happens.
"""
