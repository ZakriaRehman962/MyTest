i=10
for row in range(1,i+1):
    for col in range(1,i+1):
        print(row*col, end="\t")
    print()

"""import math
import string
import operator
#Example code for basic operations on lists
list_1=['Statistics', 'Programming', 2016, 2017, 2018, 2019]
list_2=['A', 'B', 2001, 2002, 2003, 2004]
print("Length: ", len(list_1))
print("Concatenation: ", [1,2,3] + [4, 5, 6])
print("Repetition :", ['Hello'] * 4)
print("Membership :", 3 in [1,2,3])
print("Iteration :")
for x in [1,2,3]: print(x)
# Negative sign will count from the right
print("slicing :", list_1[-2])
# If you dont specify the end explicitly, all elements from the specified
#start index will be printed
print("slicing range: ", list_1[1:])
print("Max of list: ", max([1,2,3,4,5]))
print("Min of list: ", min([1,2,3,4,5]))
print("Count number of 1 in list: ", [1,1,2,3,4,5,].count(1))
list_1.extend(list_2)
print("Extended :", list_1)
print("Index for Programming:",list_1.index('Programming'))
print (list_1)
print("pop last item in list: ", list_1.pop())
print("pop the item with index 2: ", list_1.pop(2))
list_2.remove('A')
print("removed b from list: ", list_1)
list_1.reverse()
print("Reverse: ", list_1)
list_1 = ['a','c','b']
list_1.sort()
print("Sort ascending: ", list_1)
list_1.sort(reverse = True)
print("Sort descending: ", list_1)"""