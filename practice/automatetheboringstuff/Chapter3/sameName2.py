def spam():
    global eggs
    eggs = 'test'
eggs = 'global'
spam()
print(eggs)

'''Because eggs is declared global at the top of spam() ❶, when eggs is set to 'spam' ❷, this assignment is done to the globally scoped eggs. No local eggs variable is created.

There are four rules to tell whether a variable is in a local scope or global scope:

If a variable is being used in the global scope (that is, outside of all functions), then it is always a global variable.

If there is a global statement for that variable in a function, it is a global variable.

Otherwise, if the variable is used in an assignment statement in the function, it is a local variable.

But if the variable is not used in an assignment statement, it is a global variable.'''