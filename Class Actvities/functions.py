#functions
# function definition format -> 'def function_name():'

#void function
def print_greeting():
    print("Hi there! How are you?")

#calling the function
print_greeting()


#local variables
def print_variable():
    vari_1 = "Achoo!"
    print(vari_1)

#calling the function again
print_variable()


'''two def functions can have the same code inside, but as long as the def function name is different,
it will count as two different ones. for example'''

def printing1():
    example = "hi there"
    print(example)

def printing2():
    example = "hello there"
    print(example)

printing1()
printing2()

#passing arguments through functions"
def print_bsu(greeting):
    print(greeting)

greet_me = 'Welcome to BathSpa'
print_bsu(greet_me)

def greet_name(fname):
    print('Hello', fname)

greet_name('Hannah')
greet_name('Maram')
