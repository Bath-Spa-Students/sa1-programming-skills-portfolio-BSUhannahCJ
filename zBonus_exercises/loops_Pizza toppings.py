'''Write a loop that prompts the user to enter a series of pizza toppings until they enter a
'quit' value. As they enter each topping,
Print a message saying you’ll add that topping to their pizza.'''

while True: #while loop
    pizza_toppings = input("Add a pizza topping or enter 'quit' to stop: ") #input
    if pizza_toppings.lower() == 'quit': #condition
        break #break if condition true
    print("Okay! adding the", pizza_toppings, "to your pizza!") #otherwise it prints this