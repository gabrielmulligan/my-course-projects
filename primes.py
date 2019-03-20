# Problem 5 : 16th Mar 2019
# ask the user to input a number
x = int(input("Please enter an integer: "))
# ensure the user has entered a positive number greater than 1 (the lowest prime)
if x > 1:
    # we need to divide the user's input by every number between 2 and their input number
    for i in range(2,x):
        #we check that there is zero remainder (using the moldulo "%" instead of the divisor "/")
        if (x % i) == 0:
            #if not, we print that it's not a prime number
            print(x, "is not a prime number")
            break
    # if zero remainder, we tell the user it is a prime number
    else:
        print(x, "is a prime number")
# we display a message to the user that their input has to be greater than 1
else:
    print(x, "is not a valid integer greater than 1")
    