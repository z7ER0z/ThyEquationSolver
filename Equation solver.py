import numpy as np
import math
import pandas
import cmath

print("Choose the format of the equation:\n 1) ax + b = c \n 2) ax + by = c \n dx + ey = f \n 3) ax^2 + bx + c = 0 \n So, what's it gonna be?")

while True:
 choice = int(input())
 if choice == 1:
    print("You choose this:\n ax + b = c")
    print("a: ")
    a = int(input())
    print("b: ")
    b = int(input())
    print("c: ")
    c = int(input())
    x = (c-b)/a
    print("The solution to",str(a) + 'x + ' + str(b) + ' = ' + str(c) ,"\n X =", x)
    print("\n now pick another format :)")
 elif choice == 2:
    print("You choose this:\n ax + by = c \n dx + ey = f")
    print("\n Choose in which way you desire to solve: \n 1)Matrics way ~~ Prefered \n 2)Simple way")
    i = 0
    while i <= 2:
        choice_2 = int(input())
        if choice_2 == 1:
            i =+ 1
            print("Enter the constants ~~ The numbers next to the variables.. \n Note:Each value should be in a new line/row ~~ Just hit enter after each value..")
            consts = np.array([[int(input()), int(input())], [int(input()), int(input())]])
            print("Here are the constants you entered:\n")
            df = pandas.DataFrame(consts)
            print(df)
            print("Enter the values ~~ The numbers after the (=) sign")
            values = np.array([int(input()), int(input())])
            print("Here are the values you entered")
            df_2 = pandas.DataFrame(values)
            print(df_2)
            solution = np.linalg.solve(consts, values)
            print("And here is the soultion:\n", solution)
            i =+ 3
            print("\n now pick another format :)")
        elif choice_2 == 2:
            i =+ 1
            print("a: ")
            a = int(input())
            print("b: ")
            b = int(input())
            print("c: ")
            c = int(input())
            print("d: ")
            d = int(input())
            print("e: ")
            e = int(input())
            print("f: ")
            f = int(input())
            x = (c*e-f*b)/(a*e-d*b)
            y = (f*a-c*d)/(a*e-d*b)
            print("The solution to", str(a) + 'x + ' + str(b) + 'y + ' + ' = ' + str(c) + ' and \n' + str(d) + 'x + ' + str(e) + 'y ' + ' = '  + str(f) , "\n X =", x, "\n Y =", y)
            i =+ 3
            print("\n now pick another format :)")
        else:
            i = +1
            print("You have to pick one of the two..")
 elif choice == 3:
     print("You choose this:\n ax^2 + bx + c = 0")
     print("a: ")
     a = int(input())
     print("b: ")
     b = int(input())
     print("c: ")
     c = int(input())
     #Too many darn parentheses..
     if (b*b) >= (4*a*c):
         root_1 = ((-b) + (math.sqrt((b*b)-4*a*c))) /(2*a)  
         root_2 = ((-b) - (math.sqrt((b*b)-4*a*c))) /(2*a)
         print("root 1: ", root_1, "\n" + "root 2: ", root_2)
         print("\n now pick another format :)")
     else:
         root_1 = ((-b) + (cmath.sqrt((b*b)-4*a*c))) /(2*a)  
         root_2 = ((-b) - (cmath.sqrt((b*b)-4*a*c))) /(2*a)
         print("root 1: ", root_1, "\n" + "root 2: ", root_2)
         print("Tip: That number was a complex / imaginary number")
         print("\n now pick another format :)")
 else:
    print("Pick one of the 3 ones, please.")
     
