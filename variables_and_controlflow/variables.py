
# Number datatype in python...
a = 4
b = 2
print("Addition = ", a+b )
print("Multiplication = ", a*b )
print("Subtraction = ", a-b )
print("Divison = ", a/b)
print("Power = ", a**b)

# String datatype:
a = 'abcdefghij'

#string operation:  index start from zero
print(a[2:])   # string start from index 2 to last index:  cdefghij
print(a[2:5])   # string start from index 2 to 4th index :   cde
print(a[:3])   #  string that has first 3 letters:  abc here first index is not given so default start from zero.
print(a[:])   #  will return same string a;
print(a[::2])  # output will be:  acegi
print (a.upper())   # Capitalize all letters of a
print (a.lower())    # make all the letters of a tosmall letter.
print(a.capitalize()) # make first letter capitalize.
b = "This is second string"
c = "This is 3rd string"
print(" Hi, {} {}".format(b, c))  # how to add variable value into string.
print(" Hi, {b} {c}".format(b="b value", c="C value"))


#List in Python:
mylist = [1,2,3,4,5,6,7,9]  # it is a list data type
mylistString = ['one', 'two', 5,6, True] # mixed data types
print("length of mylistString var = ", len(mylistString)) # length of the list..

# append()
mylist.append(54)   #  to add a new item in list at the last...
print(mylist)
listTwo = [3,4,5]
listTwo.extend([6,7,8])  #  will add individual item in listTwo Array...
print(listTwo)   #  output will be:  [3,4,5,6,7,8]

# pop()
print("before Delete = ",listTwo)
listTwo.pop()
print("After Delete = ", listTwo)
listTwo.pop(0)   # delete item of index: 0

# reverse()  will reverse the original array...
print("Before Reverse the list  = ", listTwo)
listTwo.reverse()
print("Reverse  = ", listTwo)

# -------------- List Data Type -----------------
# sort() method...
sortValue = [90,31,11,21,121,131,54,65,78,87,77,654,323]
print("Before sorted list = ", sortValue)
sortValue.sort()
print("After sorted list = ", sortValue)

multipleList = [ [1,2,3], [5,6,7], [8,9,10]]
firstrow = [row[0] for row in multipleList]   # get the first item of each index item array in this example..
print(firstrow)

# -------------- Dictionary Data Type -----------------
my_dict = {"key1":"value1", "key2":"value2", "key3":"value3"}
print(my_dict["key2"])   # print the second key value..

#add new key in dictionary:
my_dict['name'] = "Rajesh"
print("after new key dictionary = ", my_dict)


# Boolean data type:
bolvalue = True
print("Boolean value before change = ", bolvalue)
bolvalue = False
print("After change Boolean value = {}".format(bolvalue))

#Tubles in Python:
tup = (1,2,3)
print("at index 2 ", tup[2])
 
#Set Data Type:
x = set()

x.add(34)
x.add(12)
x.add(6)
x.add(11)
x.add(9)
x.add(41)
print("Set = ", x)  #  once item is added in Set the same item will not be added again, becoz it is a unique collection..

y = (1,2,3)
z = (1,2,3)
print(y == z)  # true both Set are same... 

# some Exercise....
s = 'django'
print(s[:1])
print(s[-1])
print(s[0:4])
print(s[1:4])
print(s[4])
rev = s[::-1]
print("reverse the string using index = ", rev)
d3 = {'k1': [{'nest_key':['this', ['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])



