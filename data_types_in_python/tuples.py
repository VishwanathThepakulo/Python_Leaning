# Tuples ------> ()

# What is Tuple?
# Tuple = collection of elements
# t = (1,2,3)


# Tuple is IMMUTABLE
# Once created → cannot change

# ❌ Cannot modify
# t[0] = 100
# Error ❌


# 🟢 Why tuples exist then?

# Because:

# Some data should NEVER change

# Examples:

# ✔ Coordinates
# ✔ Database records
# ✔ Fixed settings
# ✔ Dictionary keys

# Tuple syntax

t  =  (1,2,3)

# Single element tuple 
# t = (5,)

# Comma important.

# Without comma:

# t = (5) #integer only


# 🟢 Accessing elements
# t = (10,20,30)

# print(t[0])
# print(t[-1])

# 🔥 Tuple Methods

# Very few methods because immutable.

t = (1,2,2,3)

print(t.count(2))

# index()
print(t.index(3))

# Tuple Packing
# t = 1,2,3

# Python automatically packs into tuple.


# Tuple Unpacking
# a,b,c = (1,2,3)

# print(a)
# print(b)
# print(c)

# Very Powerful Feature
# a,b = b,a

# Tuple unpacking internally 🔥



# 🟢 Nested Tuples
# t = ((1,2), (3,4), (5,6))

# Access:

# print(t[1][0])

# Output:

# 3


# Tuple vs List


# Feature	    List	    Tuple
# Syntax 	     []	          ()
# Mutable	    ✅	        ❌
# Methods	    Many	     Few
# Faster	    ❌	        ✅
# Hashable	    ❌	        ✅


# Why tuple faster?

# Because immutable:

# Python can optimize memory



# ⚠️ Important Confusion

# Tuple immutable BUT:

# t = ([1,2], [3,4])

# Lists inside tuple still mutable


# Memory Trick
# List  → changeable
# Tuple → fixed/protected


# Use tuple when:

# ✔ Data should not change
# ✔ Faster lookup needed
# ✔ Dictionary/set compatibility needed



# student = ("Vishwanath", 22, "AI Engineer")

# name, age, role = student

# print(name)
# print(age)
# print(role)



names = ("xyz", "abc", "def")
(a,b,c) = names
print(f"names are : {a}, {b}, {c}")

abcd, efgh = 1,2
print(f"ratio of abcd is  : {abcd} and efgh is {efgh}")
abcd, efgh = efgh, abcd
print(f"ratio of abcd is  : {abcd} and efgh is {efgh}")
print(f"is xyz available in name ? {"xyz" in names}")








































