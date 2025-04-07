import json

di = {
    "name": "John",
    "age": 30,
    "skils":["python", "SQL", "JAVA"]
}

json_s = json.dumps(di, indent= 2, sort_keys = True)
print(json_s)
print(json.loads((json_s)))
print(type(json_s))