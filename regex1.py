import re  # Regular expression
import os
# string = input()
# strformat1=string.strip('[')
# strformat2=strformat1.strip(']')
# # STRIP, SPLIT OPTION
# inputaray = list(map(int,strformat2.strip().split(',')))
# inputaray= list(filter(None,inputaray))
# print('input array',inputaray)
# # REOMVE OPTION
# stringn = ["","hi","","","4"]
# while("" in stringn) :
#     stringn.remove("")
# # regex split
# str1= list(map(int,filter(None,re.split('\W',string))))
# print('re split:',str1)
# to search for any pattern/text inside a string
# Normal string and raw string difference
# print('\tTab')
# print(r'\tTab')
# creating pattern to search for some text
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# pattern = re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d')
pattern = re.compile(r'[89]00[.-]\d\d\d[.-]\d\d\d\d')
with open('abcd','r') as rf:   # another way to read file in ascii
# with open('abc','r',encoding='utf-8'):
    contents = rf.read()

    matches=pattern.finditer(contents)

    for match in matches:
        print(match)

print(contents)
# print(sentence)
#pattern = re.compile('abc')
#pattern = re.compile(r'\\')    # baackslash to be prefixed to escape special meaning for meta characters
#                           .+*?[]({}   |
#pattern = re.compile(r'www\.payback\.in')   # to  search url - escape parameter to be passed in raw string before dot
multi_line_text="""
hello Hello hello
123.345-9999 
youtube.com
 Multi_line_string
"""
# pattern = re.compile(r'youtube\.com')
# matches = pattern.finditer(multi_line_text)
#pattern = re.compile(r'\bhe')
# pattern = re.compile(r'\Bhe')
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# matches = pattern.finditer(multi_line_text)
# for match in matches:
#     print(match)
#print(sentence[161:162])
# special characters which matches all characters except few or matching some set of characters
# .   - Any Character excepet New line
# \d  - Matching digits (0-9)
# \D  - Matching  Not a digits (0-9)
# \w  - Matching word character (a-z, A-Z,0-9, _)underscoer
# \W  - Matching NOT a word character
# \s  - Matching white space
# \S  - Matching NOT white space (space, tab, new line)
# The below ones r used as anchors tolocate the position before and after characters  in conjunction with other search pattern
# \b  -  word boundary  - identified by whitespace or non-alphanumeric
# \B  -  Not a word boundary  - pattern identified  without word boundary ie.,other than whitespace
# ^  -  Beginning of string
# $  -  End of string
# []  - Matches characters in brackets
# [^ ] - Matches not in brackets
# | - Either or
# ()  - group
# Quantifiers
# *  - 0 or more
# +  - 1 or more
# ?  - 0 or one
# {3}  - Exact Number
# {3,4}  - Range of Numbers (Minimum , Maximum)
# sample regexs
# [0-9a-zA-Z_.+-]+@[0-9a-zA-Z-]+\.[a-z]


# [] -  Matches charactes in brackets
# [^] -  Matches charactes NOT in brackets
# pattern = re.compile(r'[A-Z]')  OR r'[a-z]'
# pattern = re.compile(r'[^b]bc')
text_search ="""
Mr. Smith
Ms. Smith
Mrs. Robinson
Mr. T
M/s. Tutor
Mr Rob
"""

pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
pattern = re.compile(r'tutor',re.IGNORECASE)
matches = pattern.findall(text_search)
matches = pattern.finditer(text_search)
matches_begin = pattern.match(text_search) # returns the matched item only at the beginning of the string
matches_search = pattern.search(text_search) # reeturns the matched item in the entiere string search otherwise none

for match in matches:
    print(match)

# print(match.group(0)) either 1 or , 2 or 3 based on no of groups matched
urls = """
https://wwww.google.com
http://github.com

"""
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
sub_urls = pattern.sub(r'\2',urls)
print(sub_urls)
