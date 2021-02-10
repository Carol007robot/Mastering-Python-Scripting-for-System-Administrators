"""find_nearest([9, 15, 25, 30],10)
returns: 9, because 9 is the nearest number in the list to 10
find_nearest([9, 15, 25, 30], 28)
returns: 30
find_nearest([1, 2, 3, 4, 5],100)
returns: 5
find_nearest([1,2,3],2)
returns: 2

if there are many answers, can choose one of them as answer
"""
def find_nearest(list, x):
    k = list[0]
    for i in list:
        print(i)
        b = x - i
        if abs(b) <= k:
            k = b
            print(k)
    return k
a = [9, 15, 25, 30]
b = 10
print(find_nearest(a, b))
