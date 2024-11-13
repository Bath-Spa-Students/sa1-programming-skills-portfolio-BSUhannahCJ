#exercise 7
#Some Counting

'''Use your newly acquired knowledge of the for loop to complete the following tasks. Print all values to the console
in each case.
* Write a loop that counts up from 0 to 50 in increments of 1.
* Write a loop that counts down from 50 to 0 in decrements of 1.
* Write a loop that counts up from 30 to 50 in increments of 1.
* Write a loop that counts down from 50 to 10 in decrements of 2.
* Write a loop that counts up from 100 to 200 in increments of 5.
*You may include all loops in a single project*'''



print("Let's count from 0 to 50 in increments of 1!") #info message displays first
for H in range (0,51): #range from 0 to 50, 51 excluded, is stored in variable H
    print(H, end =",") #range is printed with end delimiter to improve readibility 

print('\n') #to make a space between each loop

print("Now lets count from 50 to 0 in decrements of 1!") #info message displays first
for A in range(50,-1,-1): #range from 50 to 0, -1 excluded, with count of -1, is stored in variable A
    print(A, end=',') #range is printed with end delimiter to improve readibility 

print('\n') #to make a space between each loop


print("Let's count from 30 to 50 in increments of 1!") #info message displays first
for N in range(30,51): #range from 30 to 50, 51 excluded, is stored in variable N
    print(N, end = ",") #range is printed with end delimiter to improve readibility 


print('\n') #to make a space between each loop


print("Let's count from 50 to 10 in decrements of 2!") #info message displays first
for Z in range (50,9,-2): #range from 50 to 10, 9 excluded, with count of -2, is stored in variable Z
    print(Z, end =",") #range is printed with end delimiter to improve readibility 


print('\n') #to make a space between each loop


print("Lastly, let's count from 100 to 200 in increments of 5!") #info message displays first
for I in range (100,201,5): #range from 100 to 200, 201 excluded, with count of +5, is stored in variable I
    print(I, end =",") #range is printed with end delimiter to improve readibility 
