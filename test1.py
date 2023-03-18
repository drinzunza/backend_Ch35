from about import me

print(me)

# read data from the dict
print(me["name"])

# print the full name
name = me["name"]
last = me["last_name"]
print(name + " " + last)


# modify 
me["age"] = me["age"] + 1
print(me)

# add
me["preferred_color"] = "blue/gray"
print(me)


# print name: age
# eg: Sergio: 37
age = me["age"]
print(name + ": " + str(age))


# string format
print(f"{name}: {age}")

# delete a key from dict
del me["age"]

# z = me["age"].pop()

# optional HW
# 1 print the same ^ - but using python string formatting
# 2 delete the age key from the dictionary and print the dictionary to confirm