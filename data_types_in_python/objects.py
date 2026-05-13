# Data Types

# Objects: Everything is object in python
# -->  every object have unique identity
# -->  every object have unique type
# -->  every object have value

# Mutable & Immutable

# Mutable is changable & Immutable means this is not changable


# Immutable 
variable = 2    
print(f"initilal value {variable}")
print(id(variable))

variable = 4
print(f"second initilal value {variable}")
print(id(variable))
# in the above example refererence is changing but value is does not change in memory 2 & 4 is stored at some location but 2 is not replaced by 4 initially variable pointing to 2 after it is pointing to 4  if id is same means it is mutable


# mutable
s = set()
print(f"beginning ==>{id(s)}")
s.add(1)
s.add(2)
print(s)
print(f"End ==>{id(s)}")




















