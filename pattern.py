import re
search_string = "TutorialsPoint"
pattern = "Tutorials"
match = re.match(pattern, search_string)

if match:
   print("regex matches: ", match.group())
else:
   print('pattern not found')
