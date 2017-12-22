#!/usr/bin/python

'Option 1'
''' def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(kwarfirst_name="Aaron", last_name="Valoroso") '''

'Option 2'
'''def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))

print_kwargs(my_name="Aaron", your_name="Casey")'''

'Option 3'
''' def print_kwargs(**kwargs):
    if 'my_name' in kwargs:
        print(kwargs['my_name'])

print_kwargs(my_name="Aaron") '''

'Option 4'
def my_kwargs(**kwargs):
    if 'bbox' in kwargs:
        w,s,n,e = [str(c) for c in kwargs['bbox']]
        print("Norht: " + n) 
        print("East: " + e )
        print("South: " + s)
        print("West: " + w )
bbox = [50,40,30,20]
my_kwargs(bbox=bbox)