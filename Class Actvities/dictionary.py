#Dictionary 
#format is dictionary = {}
#inside are keys and values

DILLH = {'name' : 'Hannah',
    'age' : '18'
} #name is the key, Hannah is the value

#printing the type 
print(type(DILLH))

wait = {'name' : 'mizu', 
    'age': '17',
    'mood' : 'stressed'
}
#to get something specific
print(wait["name"])
print(wait.get('age'))

#to check the keys or values 
print(wait.keys())
print(wait.values())

#to check items
print(wait.items())

#del method
del wait['mood']
print(wait)

#pop method
print(DILLH.pop('age'))

