import re
### The outer group should match all the characters beginning with the
### letter “A” through to the ending period. The characters between the beginning A and
### the ending period make up inner groups that should match “big or small,” “brown or
### purple,” and so on.
re_obj = re.compile(r"""(A\W+\b(big|small)\b\W+\b
                    (brown|purple)\b\W+\b(cow|dog)\b\W+\b(ran|jumped)\b\W+\b
                    (to|down)\b\W+\b(the)\b\W+\b(street|moon).*?\.)""",
### The re.VERBOSE function lets you write
### simpler regular expressions, so it is a great tool for improving the maintenance of code
### that includes regular expressions
                    re.VERBOSE)
print(re_obj.findall('A big brown dog ran down the street. \
                    A small purple cow jumped to the moon.'))