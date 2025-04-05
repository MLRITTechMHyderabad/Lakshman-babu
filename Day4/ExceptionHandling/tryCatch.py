a = int(input("Enter a number: "))
li = [1,2,3,4,5,6,6]
try: 
    if a < 0 :
        raise ValueError("Entered negative number") #it will go to the constructor
    print(10/a)
    print("Hi")
    print(x)
    d = li[20]
# except ZeroDivisionError as e:
#     print(e)
# except IndexError as I:
#     print(I)

except Exception as e:
    print(e)

except (ZeroDivisionError, IndexError) as e:
    print("Err:::::", e)

else:
    print("No Erros")
finally:
    print("This block is executed at the end of the program, No matter got error or not")