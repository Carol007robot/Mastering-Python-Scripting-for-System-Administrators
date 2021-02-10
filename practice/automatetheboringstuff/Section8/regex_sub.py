##19032020
import re
# namesRegex = re.compile(r'Agent \w+')
# print(namesRegex.sub('REDACTED', 'Agent Alice gave the secrect documents to Agent Bob')) ## the sub()regex method will substitute matches with some other text. #节选修订

# namesRegex = re.compile(r'Agent (\w)\w*')
# # print(namesRegex.findall('Agent Alice gave the secrect documents to Agent Bob'))
# print(namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secrect documents to Agent Bob')) #The \1 in that string will be replaced by whatever text was matched by group 1—that is, the (\w) group of the regular expression.

#For example, say you want to censor the names of the secret agents by showing just the first letters of their names. To do this, you could use the regex Agent (\w)\w* and pass r'\1****' as the first argument to sub().
# agentNamesRegex = re.compile(r'Agent (\w)\w*')
# print(agentNamesRegex.sub(r'\1***', 'Agent Alice told Agent Carol that Eve knew Agent Bot was a bouble agent.'))
#
# phoneRegex = re.compile(r'''(
# (\d{3}|\(\d{3}\))?              # area code
# (\s|-|\.)?                      # separator \s ==> space \d => digits
# \d{3}                           # first 3 digits
# (\s|-|\.)                       # separator
# \d{4}                           # last 4 digits
# (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
# )''', re.VERBOSE)               # 冗长的 re.VERBOSE lets you add whitespace and comments to the regex string passed to re.compile()
#
# print(phoneRegex.search('234-342-2342 ext.2342234'))