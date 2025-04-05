#Custome Exception
class NegativeNumberException(Exception):
    def __init__(self, message):
        self.Mesg = message  #mesg is the attribute of -ve number class
        super().__init__(message)
try: 
    a = int(input("Enter the Number: "))
    if a < 0 :
        raise NegativeNumberException("Error: Entered negative number") #it will go to the constructor
    print("You are entered a Valid number.")
except Exception as e:
    print(e)

finally:
    print("END")
    