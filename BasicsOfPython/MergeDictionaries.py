car1 = {
    "name" : "ford",
    "model" : "Mustang",
    "year" : 1969
}
car2 = {
    "name" : "Shelby",
    "model" : "Mustang",
    "year" : 1968
}

car1.update(car2)
# print(car1)

car = car1 | car2
# print(car)

supercar = car1.copy()
for key, value in car2.items():
    supercar[key] = value
print (supercar)
