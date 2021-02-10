# import pprint
# #message = "it was a bright cold day in April, and the clocks were striking thirteen.".split()
# message = [1, 1, 2, 2, 3, 4, 5]
# count = {}
#
# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1
#
# pprint.pprint(count)

# customer = {
# #     "name": "John Smith",
# #     "age": 30,
# #     "is_verified": True
# # }
# # print(customer.get

phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)