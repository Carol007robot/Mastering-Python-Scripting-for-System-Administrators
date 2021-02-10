# def remove_repeats(items):
#     orig_items = None
#     new_items = []
#     for x in items:
#         # (print(x))
#         if x != orig_items:
#             new_items.append(x)
#             orig_items=x
#  #           print(orig_items)
#     return new_items
#
# if __name__ == '__main__':
#     a = [2, 3, 3, 4, 5, 3, 5]
#     b = "The cat and cat is on on the mat mat".split()
#     # print(remove_repeats(a,b))
#     print(remove_repeats(a))
#     print(remove_repeats(b))


numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)