f = open("foo.txt", "r")
lines = f.readlines()

print(lines)
print(len(lines))
print(len("".join(lines)))
