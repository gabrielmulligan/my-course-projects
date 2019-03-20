# 16th Mar : Problem Set 1
# asks the user to input a number
i = input("Please enter a positive Integer :")
# ensures the number is a positive integer
i = int (i)
# ensures the sum is currently 0
sum = 0
# increments by 1 from 1 to the n entered above
for num in range(0,i+1,1):
    sum = sum+num
# prints the result back to the user
print("The sum of the first", i, "numbers is:", sum )