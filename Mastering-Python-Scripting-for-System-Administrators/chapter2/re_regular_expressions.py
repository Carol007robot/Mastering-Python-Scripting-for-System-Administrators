"""The regular expression pattern \b matches word boundaries. So in both the raw and
regular strings, we were looking for individual lowercase words. Notice that raw_pat
tern matched the word boundaries appropriately on some_string and
non_raw_pattern didn’t match anything at all. Raw_pattern recognized \b as two characters rather than interpreting it as an escape sequence for the backspace character.
Non_raw_pattern interpreted the \b characters as an escape sequence representing the
backspace character. The regular expression function findall() was then able to use
the raw string pattern to find words. However, when findall() looked for the non-raw
pattern, it didn’t find any backspace characters."""
import re
raw_pattern = r'\b[a-z]+\b'
non_raw_pattern = '\b[a-z]+\b'
some_string = 'a few little words'
print(re.findall(raw_pattern, some_string))



### The regular expression was intended to match words that start with “t” and
### end with “e”. But the .*? command matches anything, including whitespace

re_obj = re.compile(r'\bt.*?e\b')

print(re_obj.findall("time tame tune tint tire"))


### To exclude the whitespace, you would use r'\bt\w*e\b':

re_obj = re.compile(r'\bt\w*e\b')
print(re_obj.findall("time tame tune tint tire"))
