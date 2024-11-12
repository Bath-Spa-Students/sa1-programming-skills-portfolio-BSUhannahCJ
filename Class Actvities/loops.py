#loops
#while loops
vari = 1
while vari < 10:
  print(vari)
  vari += 1  #+= is the same as vari = vari+1 
  
  LLL = 2
while LLL < 12:
  print(LLL)
  LLL += 2 
  
number = 1
while number <= 10:
    print("numbert is:", number)
    number += 1
    
hanz = 1
while hanz < 6:
  print(hanz)
  if hanz == 3:
    break #helpful if you want to change a long code without rewriting the whole thing
  hanz += 1  

backpack = ["apple", "bandaid", "knife"]
for x in backpack: #assigning the list to a variable in a for loop
  print(x)

for h in range(0,25): #will print the numbers from 0 to 24 as 25 is excluded
      print (h)
