#The regular expression looks for any words that starts with an upper case "S":
import re 
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group()) 