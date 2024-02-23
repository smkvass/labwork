import json

# a python object(dict)
x = {
    "Name": "Saya",
    "Age": 17,
    "City": "Almaty"
}
#convert into JSON
y = json.dumps(x)

#the result is a JSON string
print(y)