
a = 10
b = 50

#swipe both the variable value

#method one by using a new variable

""" 
m = a
a = b
b = m
print(a,b)  #two variable print in single line by using coma
print(a)
print(b)
"""
#method two by using intercnaging this method only work in c python
"""
a,b = b,a
print(a,b)
print(a)
print(b)
"""

#method three by using additoin and subtration

a = a + b
b = a - b
a = a - b
print(a)
print(b)