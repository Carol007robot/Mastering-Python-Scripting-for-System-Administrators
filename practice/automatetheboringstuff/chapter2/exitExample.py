import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')

    """
     1. What are the two values of the Boolean data type? How do you write them?
     True and False
     2. What are the three Boolean operators?
     and, or, and not

     3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).
        True or True    True
        True or False   True
        False or True   True
        not False       True
        
4. What do the following expressions evaluate to?


(5 > 4) and (3 == 5)
False
not (5 > 4)
False
(5 > 4) or (3 == 5)
True
not ((5 > 4) or (3 == 5))
True
(True and True) and (True == False)
False
(not False) or (not True)
True

5. What are the six comparison operators?
== 
!=
<
>
<=
>=

6. What is the difference between the equal to operator and the assignment operator?
The == operator ## asks whether two values are the same as each other
The = operator  puts the value on the right into the value on the left.  

7. Explain what a condition is and where you would use one.
Condition is just a more specific name in the context of flow control statements. Conditions always evaluate down to a Boolean value, True or False. 
A flow control statement decides what to do based on whether its condition is True or False, and almost every flow control statement uses a condition. 

8. Identify the three blocks in this code:
spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')

The first block of code starts at the line print('eggs') and contains all the lines after it. inside 
this blosk is another block 2


9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
'''
print('How many spam do you have')
spam = input()
if spam == '1':
    print('Hello')
elif spam == '2':
    print('Howdy')
else:
    print('Greetings!')
'''
10. What can you press if your program is stuck in an infinite loop?
ctrl + c

11. What is the difference between break and continue?
The continue statement will continue to the next value of the for loop's counter, as if the program execution had reached the end of the loop and returned to the sttart.
In fact, you can use continue and break statement only inside while and for for loops. If you try to use these statements elsewhere, Python will give you an error.

12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
range(10), this lets you change the interger passed to range(10) to follow any sequence of integers.
range(0, 10), the first argument will be where the for loops variable starts, in here, it start from 0, and the second argument will be up to, but not including,, the number to stop at 10.
range(1, 10, 1), calling range(1, 10, 1) will count from 1 to 9 by intervals of 1. 
13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
for i in range(1, 11)
    print(i)
i = 0
while i < 11:
    print(i)
    i = i + 1

14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
spam.bacon()
     """