def collatz(number):
    if number == 1:
        print('Collatz Complete. Amazing isn\'t it!')
    elif number % 2 == 0:
        print(int(number / 2))
        collatz(number / 2)
    else:
        print(int(3 * number + 1))
        collatz(3 * number + 1)

collatz(int(input('Enter number: ')))

# try:
#     collatz(int(input('Choose any integer greater than 1: ')))
# except ValueError:
#     print('Non-Interger entered, program will exit')

