# Python 3.6.0
#
# Date: 02/27/2017
#
# Author: Ada Chavez
#
# Program: The following is a drill from The Tech Academy demonstrating the range function
#
#

'''1. Start IDLE and use the Python range() function with one parameter to display the
following:
0
1
2
3
'''
my_list_1 = range(4)
for a in list(my_list_1):
    print (a)

    
# Prints new line
print()


'''
2. Use the Python range() function with 3 parameters to display the following:
3 2 1 0
'''
x = list(range(3,-1,-1))
print(x)

    
# Prints new line
print()

'''
3. Use the Python range() function with 3 parameters to display the following:
8 6 4 2
'''
y = list(range(8,0,-2))
print(y)
