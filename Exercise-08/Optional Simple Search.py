#Exercise 8 - Simple Search
#optional requirements 

list_of_names = ["jake", "zac", "ian", "ron", "sam", "dave"]  #list of names 
name_search = input("What's the name that you are looking for? : ").lower() #input command in variable with .lower()
if name_search in list_of_names: #if name_search (which is the user's input) is = list_of_names then
    print("Name found.") #it will print this if its equal to
else: #else it will
    print ("Name not found.") #print this otherwise