import json
#some json
x = '{ "name":"Saya", "age":17,"city":"Almaty"}'

#parse x
y = json.loads(x)

#the result is a Python dictionary:
print(y["city"])