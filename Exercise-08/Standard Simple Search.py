#Exercise 8- Simple Search
#standard requirements 

'''Write a program that searches for a specific string within a list of strings. The list is 
initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). 
, and your task is to search for "Sam".'''

list_of_names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]  # a list of names
if "Sam" in list_of_names:  # 'if' and 'in' command are used to find whether the name/string "Sam" is in the list
    print ("Sam is in the list.") #if the name/string is in the list, then it will print this output
else:
    print ("Sam is not in the list.") #Else if the name/string "Sam" is not in the list, this output will print