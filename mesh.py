"""hello this is a comment"""

"""
1-List is a collection which is ordered and changeable. Allows duplicate members.
2-Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
3-Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
4-Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""
#newlist = [expression for item in iterable if condition == True]

def myfunc(*,x):
   print("num is", x)

myfunc(x=4)


y=lambda a,b : a / b

print(y(1,2))
