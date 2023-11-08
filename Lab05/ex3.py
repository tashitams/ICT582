"""
Read the following Python code:
a = 1
b = a
b = 3
Question 1: Do variables a and b refer to the same object after the second statement? Explain why.
Verify your answer with the id function to see the id of each object.

Answer: Yes, variable a and b refers to the same object after the second statement. When we write b = a
what is copied to variable b is not value 1, rather, it is the start address of object a.
This means both a and b contain the same address, which points to the same object 1. We call b an alias of
a because they point to the same object.

"""
a = 1
b = a

print(id(a))
print(id(b))

# --------------------- End of question 1 ------------------------------


"""Question 2: In the 3rd statement, we assigned a new value to variable b. Would this change affect variable a? 
Explain why. 

Answer: No, the assignment of value 3 to b will not affect variable a because in line 3, when we changed 
the value of b to 3, we made a separate copy of the value from a when we assigned it to b.
"""

# --------------------- End of question 2 ------------------------------


"""
x = [1, 2, 3]
y = x
Question 3: Do variables x and y refer to the same object? Explain why.

Answer: Yes, both x and y refer to the same object. This is because, in Python, we use the = operator to create a 
copy of an object. It would be wrong to think that this creates a new object; it doesn't. It only creates a 
new object (y) that also points to the same memory address as the original object (x).
"""
x = [1, 2, 3]
y = x

print(x, y)
print(id(x))
print(id(y))

# --------------------- End of question 3 ------------------------------


"""
y.append(4)

Question 4: What is the current value of y? What is the current value of x? Why?

Answer: The current value of x and y will be the same, that is, [1, 2, 3, 4] because both objects x and y 
share the same memory address. So, when we added 4 to y since x also points to the same address, 
the change is visible in both.
"""
x = [1, 2, 3]
y = x

y.append(4)

print(x)  # [1, 2, 3, 4]
print(y)  # [1, 2, 3, 4]

# --------------------- End of question 4 ------------------------------


"""
y = y + [5]
Question 5: What is the current value of y? What is the current value of x? 
Are x and y having the same value or different values? Why?

Answer: The current value of y is [1, 2, 3, 4, 5], whereas the current value of x is [1, 2, 3, 4]
x and y will have different values since the y object when we assign a new value y + [5], 
will create a new reference address.
"""
x = [1, 2, 3]
y = x

y.append(4)

y = y + [5]

print(x)  # [1, 2, 3, 4]
print(y)  # [1, 2, 3, 4, 5]

# --------------------- End of question 5 ------------------------------


"""
z = x[:]
Question 6: What is the current value of z? Do variables x and z refer to the same object or different objects? 
Why? Can you give some concrete evidence?

Answer: The current value of z is the same as that of x [1, 2, 3]. However, x and z do not refer to the same object.
This is evident when we check the id of the x and z objects. They return a different address. z is an independent object 
with identical contents as x.

"""
x = [1, 2, 3]
z = x[:]

print(id(x))
print(id(y))

print(x)
print(z)
