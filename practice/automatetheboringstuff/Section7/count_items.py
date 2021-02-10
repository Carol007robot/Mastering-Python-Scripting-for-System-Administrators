# items = "the cat is on the mat".split()
# count = {}
# for x in items:
#     count.setdefault(x, 0)
#     count[x] = count[x] + 1
#
#print(count)

items2 = [1, 1, 2, 2, 3, 4, 5]
count = {}
for x in items2:
    count.setdefault(x, 0)
    count[x] = count[x] + 1
print(count)