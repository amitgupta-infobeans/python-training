# will cover Operators if/else if/for/while/forEach loops..

print(3>4)  # return false;
print(1=='1')

# logical operators:
print(" 1 and 1 = ", 1 and 1)
print(" 1 and 0 ", 1 or 0)
print(" 0 and 0 = ", 0 or 0 )

# if statement:
if 1 > 8:
    print('Big')
else:
    print('Small')


#if else statement..
if 3 > 1:
    print('3 is greater')
elif 4 > 6:
    print("4 is greater")
else:
    print("nothing happend")


# for loop in python...
Items = [3,4,5,6,7]
for someItem in Items:
    print("Item in list =", someItem)

# for loop with Dictionary..
dictItems = {'a':'apple', 'b':'boy', 'c':'cat', 'd':'dog'}
for dictItm in dictItems:
    print("key = ",dictItm," value= ", dictItems[dictItm])

# looping in tuples:

mypairs = [(1,3), (2,4), (5,7), (6,8)]
for tup1, tup2 in mypairs:
    print("touple key = ",tup1, " touple value = ",tup2)

#while loop
i = 5
while(i>0):
    print("i value in while loop = {}".format(i))
    i = i-1

# rang(startValue, endValue, valueDifference) function..  endValue index, will not be included in result.
rangItems = list(range(0,20, 2))
print(rangItems)  # it will not cover 20th index















