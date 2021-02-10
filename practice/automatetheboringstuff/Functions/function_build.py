allGuests = {'Alice': {'apples': 5, 'pretzels': 12, 'bear': 3},
             'Bob': {'ham sandwiches': 3, 'apples': 2, 'bear': 1},
             'Carol': {'cups': 3, 'apple pies': 1, 'bear': 1}}


def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
       # print(item)
       #  if numBrought == 7:
       #      print('Hello, here is')
    return numBrought

print('Number of things being brought:')
print(' - Apples    ' + str(totalBrought(allGuests, 'apples')))
print(' - cups     ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes  ' + str(totalBrought(allGuests, 'Cakes')))
print(' - ham sandwiches   ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))