print(type(Hannah)) #this command allows us to check the data type of the value inside the variable.

#the command below allows us to change the data type of the values in  the variables

WEB = int(2.07) #however you cannot define a string as an integer or a float. There are restrictions.
print(type(WEB))

REP = str(17)
print(type(REP))

RIO = float(3)
print(type(RIO))

print('RIO') #when we put quotations, it'll print as it is even if its the same as a variable
print(RIO) #here it print the value assigned to the variable

#string concatenation through variable
message = 'hello'+' BathSpa!'
print(message)
enter = 'welcome' + ' home ' + 'mother!'
print(enter)

#string concatenation through print statement
print('come' + ' back' + ' soon!')

#string concatenation through different variables
a = "Hello"
b = 'hannah'
c = a + " " + b
print(c)
