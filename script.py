from random import randint
import numpy as np
a=np.array([[1,2],[3,4]])
print(a)

randomNumber = randint(0, 49)
playerNumber=32
playAmount =550
totalAmount=500

if playerNumber > 49 or playerNumber < 0:
    print("Invalid number")
else:
    if playAmount > totalAmount:
        print("High stakes")
    else:
        if playerNumber == randomNumber:
            playAmount *=50
            totalAmount +=playAmount
            print("You won!!!", playAmount, "total amount is", totalAmount)
        else:
            playAmount -=playAmount
            totalAmount -=playAmount
            print("You lost!!!")
