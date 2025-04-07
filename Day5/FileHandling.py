file = open("demo.txt", "r")    #r means read
content = file.read()
print(content)
file.close()

#r+ w+ means read and write. a+ append and read
# w - To write into a file it will remove existing content
file = open("demo.txt", "w")    #r means read
file.write("Who are you?")
file.close()

#To save existing content use append mode
file = open("demo.txt", "a")    #r means read
file.write("Who are you? \n")
file.write(" are you? \n")
file.close()

#Context Manager(mostly using)
with open("demo.txt", "r") as file:
    content = file.read()
    print(content)
    #automatically closes the file

with open("demo.txt", "a") as file:
    content = file.read()
    print(content)
    #automatically closes the file

