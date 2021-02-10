# print("please input a value for X: ")
# x = input()
# print("please input a value for Y: ")
# y = input()
#
# if x == 'I am carol':
#     x, y = y, x
#     print(x)
#     print(y)
# else:
#     print(x, y)

numbers = [1, 7, 6, 0, 9]
# for x in numbers:
#     # linux out of range error, it requires 6 length, but it can only find 5, -1 in len to reduce the length to 5
#     for i in range(len(numbers)-1):
#         if numbers[i] > numbers[i+1]:
#             numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
# print(number)
count = 0
while count <= len(numbers):
        # count = count + 1
    #    print(count)
    for i in range(len(numbers)-1):
            # print(i)
        if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                print(numbers, count)
        # exit()
    count = count + 1

print("hello")