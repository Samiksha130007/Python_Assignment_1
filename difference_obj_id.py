a = 10   
b = 10
print(id(a)) # same memory address
print(id(b)) # same memory address

a = [10]
b = [10]
print(id(a)) #different list objects, Separate memory allocated
print(id(b)) #Different list objects ,Separate memory allocated