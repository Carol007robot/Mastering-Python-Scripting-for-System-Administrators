import re
###17032020


# startRegex = re.compile(r'^Hello') # ^Means the string must start with the pattern
# print(startRegex.search("Hello world!"))
#
# endRegex = re.compile(r'world!$') # $Means the string must end with the pattern.
# print(endRegex.search('Hello world!'))
#
# digitsRegex = re.compile(r'^\d+$') # ^$both means the entire string must match the pattern
# print(digitsRegex.search('23423423423'))
# print(digitsRegex.search('234234x23423'))


# nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)') # You can use the dot-star (.*) to stand in for that “anything.” Remember that the dot character means “any single character except the newline,” and the star character means “zero or more of the preceding character.”
# print(nameRegex.search('First Name: Al Last Name: Sweigart'))

# nongreedyRegex = re.compile(r'<.*?>') #To match any and all text in a nongreedy fashion, use the dot, star, and question mark (.*?). Like with curly brackets, the question mark tells Python to match in a nongreedy way.
# print(nongreedyRegex.search('<To serve man> for dinner.>'))
#
# greedyRegex = re.compile(r'<.*>') #The dot-star uses greedy mode: It will always try to match as much text as possible.
# print(greedyRegex.search('<To serve man> for dinner.>'))



# prime = 'Serve the public trust.\nProtest the inocent.\nUpload the law.'
#print(prime)
# dotStar = re.compile(r'.*')
# print(dotStar.search(prime))
# dotStar = re.compile(r'.*', re.DOTALL) #pass re.DOTALL as the second argument to re.compile() to make the .dot match newlines as well
# print(dotStar.search(prime))

# voweRegex = re.compile(r'[aeiou]')
# print(voweRegex.findall('Al, why does your programming book talk about RoboCop so much'))
voweRegex = re.compile(r'[aeiou]', re.I) #Pass re.I as the second argument to re.compile() to make the matching case-insensitive
print(voweRegex.findall('Al, why does your programming book talk about RoboCop so much'))
