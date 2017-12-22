#!/usr/bin/python


#*****************DICTIONARY EXAMPLE********************#
dict = {'Name': 'Aaron', 'Name': 'Josh', 'Age': 9, 'Age': 10}
dict1 = {'Name': 'Aaron', 'Age': 23, 'Ethnicity': 'white', 'Height': 76, 'Weight': 230}
#(Invalid Syntax) - dict2 = {'Name': 'Aaron', 'Josh', 'Age': 9, 10}
#(Invalid Syntax) - dict3 = {'Name: 'Aaron', 'Age': 9, 'Name': 'Josh', 'Age': 10}

#(Invalid Syntax) - print(dict)
#(Invalid Syntax) -print(dict1))

print(dict['Name'], dict['Age']) #Will print the last element in the dictionary for each identifier.
print(dict1['Name'], dict['Age'])

dict1['Name'] = "Josh"
dict1['Age'] = 24

print(dict1['Name'], dict['Age'])
print(len(dict1))

#(Invalid Syntax) - ? confused - print cmp(dict, dict1)
#(Invalid Syntax) - ? confused - print(str(dict1))
#(Invalid Syntax) - ? confused - print(type(dict1))
#(Invalid Syntax) - ? confused - print(dict.keys())

#(Invalid Syntax) - ? confused - del dict['Age'] # Will delete the element for age.
#(Invalid Syntax) - ? confused - dict .clear()	# Will clear all the elements in the dictionary.
#(Invalid Syntax) - ? confused - del dict	# Will delete the dictionary.

#*****************LIST EXAMPLE********************#
list1 = ['physics', 'chemistry', 'math', 'history']
list2 = [1,2,3,4,5,6]
list3 = ['Aaron', 'Josh', 'Grace', 1994, 1993, 1995]

list1.extend(['english', 'cooking'])
print("List1: ", list1)

del list1[0]
del list2[0]
del list3[0]

print("List1: ", list1)
print("List2: ", list2)
print("List3: ", list3)

list4 = list1 + list2

print("List4: ", list4)

#*****************TUPLE EXAMPLE********************#
tup1 = ('physics', 'chemistry', 'math', 'history')
tup2 = (1,2,3,4,5,6)
tup3 = ('Aaron', 'Josh', 'Grace', 1994, 1993, 1995)

tup4 = tup1 + tup2

print("Tup4: ", tup4)

# TUPLES dont support deletion of a specific item. - del tup1[0]
del tup1

#*****************COMBINATION EXAMPLE********************#
classes = ['Physics', 'English', 'Math', 'History', 'Spanish', 'Music']
periods = [1, 2, 3, 4, 5, 6]

curriculum = {'CLASS: ': classes, 'PERIOD: ': periods}

print("Curriculum: ", curriculum)
