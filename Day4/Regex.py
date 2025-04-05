import re

p = r"a."
text = "aa aab asds"
print(re.findall(p, text))

p1 =r"one$"
t2 = "Hello Everyone"
print(re.findall(p1, t2))

p2 =r"[abc0]"
t3 = "Hello all 000"
print(re.findall(p2, t3))


p3 =r"q+"              #"\d+ \d- \d* \w+ \W+ \s+ \S+ q*"
t4 = "Hello all 600 students, MLRIT 2025_ @gamil.com qq q qq false"
print(re.findall(p3, t4))

p4 =r"q{1,3}"
t5 = " qqq q qq false"
print(re.findall(p4, t5))


y = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z0-9]+$"
text = "lucky99@gmail.com"
print(re.findall(y, text))