import Modules

print(Modules.Year)
print(Modules.add(3,4))
obj = Modules.demo("Hello Everyone!!!")
print(obj.msg)

#import only demo class
from Modules import demo
obj = demo("Hello Everyone!!!")
print(obj.msg)

import csv

with open("mod.csv", 'a+', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(['Tony',20,'C',"Bangalore"])
    reader = csv.reader(file)
    for i in reader:
        print(i)

with open("mod.csv", 'a+', newline = '') as file:
    c = csv.DictReader(f)
    for i in c:
        print(i)


