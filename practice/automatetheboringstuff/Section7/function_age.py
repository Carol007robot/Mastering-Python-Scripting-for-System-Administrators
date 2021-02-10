#as a programer you should always anticipate this kind of exceptions.
#comments explain whys and hows, not what
try:
    age = int(input('Age: '))
    income = 2000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid value')
