f = open("some_writable_file.txt", "w")
f.write("Test\nFile\n")
f.close()
g = open("Some_writable_file.txt", "r")

print(g.read())


f = open("writelines_outfile.txt", "w")
f.writelines("%s\n" % i for i in range(10))
f.close()

g = open("writelines_outfile.txt", "r")
print(g.read())



# It is important to note that writelines() does not write a newline (\n) for you; you have
# to supply the \n in the sequence you pass in to it. It’s also important to know you don’t
# have to use it only to write line-based information to your file. Perhaps a better name
# would have been something like writeiter().
def myRange(r):
    i = 0
    while i < r:
        yield "%s\n" % i
        i += 1
f = open("writelines_generator_function_outfile", "w")
f.writelines(myRange(10))
f.close()
g = open("writelines_generator_function_outfile", "r")
print(g.read())