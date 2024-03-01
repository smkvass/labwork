#Print the position (start- and end-position) of the first match occurrence.
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())