#Sequences: lists and tuples where lists are mutable and tuples are immutable 
#lists 
list = ['hi', 20, 2.7] #you can store different types of data in lists in python

#class activity for lists 
#homogeneous list
strings=['hannah','year 1','group 3','creative computing']
print(strings)

friends=['elizabet','dawna','zhea','anagha','denise','marah','khadija']
print(friends)

#heterogeneous list
birthday=[2006,'17',0.6]
print(birthday)
math=['abc','xyz',2.5,3.14,21]

# * is a repitition operator when applied to a sequence and integers 
nums = [1,2,3,4]
new_nums = nums * 2
print (new_nums)

say = ['hi','hello','hey']
new_say = say * 3
print (new_say)

birthday = ['june',17,2006]
new_birthday = birthday * 6
print (new_birthday)

#Indexing in lists is used to find the position of the element in a list
#python is a zero index programming language meaning it'll start from 0,1,2,3...
lovergirl = [1,2,3,34,5] #here 1 = 0, 2 = 1, and 3 = 2
mylist = lovergirl.index(3) 
print(mylist) # so the output will be 2

#len function in list is used to determine the length of a list/ the amount of elements in a list
imgoingmad = [2,60,3,4,2]
length = len(imgoingmad)
print(length) #output is 5

#lists are mutable meaning you can change the content inside of a list even after its been created. for example
list6 = [1,2,3]
list6[2] = 4 #the number in the bracket is the position for where we want to put the new element which is '4'
print(list6) # output is 1,2,4 because we changed it instead of adding it 

#concatenating lists
# note that u cannot add lists of two different data types together
uno = [1,2,3]
onu = [4,5,6]
add = uno + onu
print (add)

#list slicing
#list slicing format is 'list[start:end]'
backpack = ["gun", "medkit", "socks", "shirt", "canned food", "water"]
print(backpack[2:5]) #5 is exclusive. so if u want to print, for example, "water" as well then you need to add one more number so thats [2:6]

backpack2 = ["gun", "medkit", "socks", "shirt", "canned food", "water"]
print(backpack2[-3:-1]) #works with negative numbers as well. 
#-1 will start from the end and work its way to the start. 'water' is -1 so it will be skipped and so "canned food" and "shirt" will be printed\

# in and not in operator to find an item in a list whether true or false
#in
if "gun" in backpack2:
    print ('true')
else:
    print ("false")

listnumber = [1,2,3,4,5]
if 2 in listnumber:
    print ("true")
else:
    print ("false")

#not in 
if 2 not in listnumber:
    print ("true")
else:
    print ("false")

# append function is list is used to add elements to an already existing list
backpack2.append("tissue")
print (backpack2)

#insert function in list is used to insert/add an element but also in a certain position
alphabet = ["a",'b','d']
alphabet.insert(2, "c")
print (alphabet)

#sort function in list is used to sort the elements in ascending or descending order
example = [2,3,6,4,8,1,9]
example.sort(reverse = True) #for descending order from right to left
print(example)

example.sort() #for ascending order from right to left 
print (example)

#remove function is used to an element from a list
example.remove(9)
print (example)

#reverse function is used to reverse the elements in a list like how it was used in the sort function earlier
example.reverse()
print (example)

#del function
listfive = [2,4,6,9,0,2,1,3,5]
del listfive[0] #instead oof zero it will delete the element with the position of 0 which is 2
print (listfive)

#min and max function used to find elements with the lowest and highest value 
minimum = min(listfive)
maximum = max(listfive)
print(minimum)
print(maximum)

