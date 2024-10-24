'''Steps:
1. Write a program that asks the user “What is the capital of France?” and
waits for their response.
2. If the user’s answer is correct (i.e., “Paris”), the program should print a
message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the
answer is wrong.
Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of
the capitalization (e.g., “paris”, “Paris”, and “PaRis” should all be considered
correct). Multiple Questions: Extend the program into a quiz that asks for the
capitals of 10 European countries. Provide feedback for each question.'''

#this is a quiz program that asks the user the capital city of 10 european countries

Qnum_1= input("What is the capital of France?: ") #first variable stores a question that is asking an answer/input from the user with the input command.
print (Qnum_1) #print function will display the question on the screen, allowing the user to type in their question
if Qnum_1.lower() == "paris": # the .lower() command allows the program to ignore capitlization in terms of the answer. For example, users can then put "PaRis" or "PARIS" and still get the 'correct answer' output.
    print("Correct answer!") #if the user puts the correct answer which is 'paris', then 'correct answer' will display on screen
else:
    print("Wrong answer!") # else it will display 'wrong answer'

#From here on it's a copy and paste coding program except for the variable names, values, and the if-else condition.

Qnum_2= input("What is the capital of Germany?: ")
print (Qnum_2)
if Qnum_2.lower() == "berlin":
    print("Correct answer!")
else:
    print("Wrong answer!")
    
Qnum_3= input("What is the capital of Italy?: ")
print (Qnum_3)
if Qnum_3.lower() == "rome":
    print("Correct answer!")
else:
    print("Wrong answer!")
    
Qnum_4= input("What is the capital of Spain?: ")
print (Qnum_4)
if Qnum_4.lower() == "madrid":
    print("Correct answer!")
else:
    print("Wrong answer!")

Qnum_5= input("What is the capital of Netherlands?: ")
print (Qnum_5)
if Qnum_5.lower() == "amsterdam":
    print("Correct answer!")
else:
    print("Wrong answer!")
    
Qnum_6= input("What is the capital of Belgium?: ")
print (Qnum_6)
if Qnum_6.lower() == "brussels":
    print("Correct answer!")
else:
    print("Wrong answer!")
    
Qnum_7= input("What is the capital of Austria?: ")
print (Qnum_7)
if Qnum_7.lower() == "vienna":
    print("Correct answer!")
else:
    print("Wrong answer!")
    
Qnum_8= input("What is the capital of Greece?: ")
print (Qnum_8)
if Qnum_8.lower() == "athens":
    print("Correct answer!")
else:
    print("Wrong answer!")
    
Qnum_9= input("What is the capital of Sweden?: ")
print (Qnum_9)
if Qnum_9.lower() == "stockholm":
    print("Correct answer!")
else:
    print("Wrong answer!")
    
Qnum_10= input("What is the capital of Poland?: ")
print (Qnum_10)
if Qnum_10.lower() == "warsaw":
    print("Correct answer. End of quiz!") #as long as the user finishes the quiz, the last question displays 'end of quiz' whether the question is right or wrong
else:
    print("Wrong answer. End of quiz!")
