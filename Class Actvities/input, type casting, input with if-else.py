# input function. a function used to get input from the user.
varsity = input("enter sports club:") 
print (varsity)
age = input('enter your age:')
print(age)

#type casting
Age = int(input('enter your age:')) #its better to define the data type with 'int' when using integers and same with float
print(Age)

#nested if. two conditions(if) and one alternative (else)
Earning = int(input("enter your earning per year:")) #earning is a variable used for user input and we specified it with int because of the question.
work_experience = float(input("enter your work experience:")) #work_experience is a variable used for user input and we specified it with float because of the question. for example someone might add '2.5 years'
if Earning >= 30000: #first condition
    if work_experience >= 2:
        print ('eligible for loan')
    else:
        print("sorry your work experience is less than 2 years")
else:
    print ("sorry your earning is less than 30K")
