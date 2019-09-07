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