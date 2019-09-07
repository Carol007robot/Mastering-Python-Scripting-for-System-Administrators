"""The four primary regular expression methods (or functions) which are most likely to
be used often are findall(), finditer(), match(), and search(). You might also find
yourself using split() and sub(), but probably not as often as you will use the others"""
import re
def run_re():
    pattern = 'pDq'
    re_obj = re.compile(pattern)

    infile = open('large_re_file.txt', 'r')
    match_count = 0
    lines = 0
    for line in infile:
        match = re_obj.search(line)
        if match:
            match_count += 1
        lines += 1
    return (lines, match_count)

if __name__=="__main__":
    lines, match_count = run_re()
    print('LINES::', lines)
    print('MATCHES::', match_count)


# Match() and search() provide similar functionality to one another. Both apply a regular
# expression to a string; both specify where in the string to start and end looking for the
# pattern; and both return a match object for the first match of the specified pattern. The
# difference between them is that match() starts trying to match at the beginning of the
# string at the place within the string where you specified it should start looking and does
# not move to random places within the string, but search(), however, will try to match
# the pattern anywhere in the string or from the place within the string that you tell it to
# start, ending at the place within the string where you told it to finish.

re_obj = re.compile('FOO')
search_string = ' FOO'
print(re_obj.search(search_string))
print(re_obj.match(search_string))