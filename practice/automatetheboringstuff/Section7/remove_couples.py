# def remove_couples(items):

def countItems(mylist):
    count = {}
    for x in mylist:
        count.setdefault(x, 0)
        count[x] = count[x] + 1
    print(count)
    return count

# def removeCouples(couples):
#     couples = countItems(mylist)


if __name__ == '__main__':
    a = [2, 3, 3, 4, 5, 3, 5]
    b = countItems(a)
    count = []
    for x, y in b.items():
        if y != 2:
            x = x * y
            print(x)
    print(count)



