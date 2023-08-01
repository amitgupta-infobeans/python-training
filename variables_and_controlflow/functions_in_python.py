import random;
def firstFunction(param1, param2='defualtValue'):
    """
    This is first function...
    """
    type_of_var = type(param1)  # check the type of a variable..
    print("My first python function having first {} and second is {}".format(param1, param2))

#function calling..
firstFunction("Parameter-1")

#find even numbers from the list...
listt = [3,4,5,5,6,7,8,9,934,56,345,4456,766,23423,111,767,898,5656];

def findEvenNo(lst):
    return lst%2 == 0
evenList = []
oddList = []
for evenNo in listt:
    if(findEvenNo(evenNo)):
        evenList.append(evenNo)
    else:
        oddList.append(evenNo)
print("All Even Numbers {}".format(evenList))
print("All Odd Numbers {}".format(oddList))

# Some of the common function of string:
St1 = "My String seprated by spaces"
print(St1.upper())
print(St1.lower())
splited_string =  St1.split()
print(splited_string)


if 'x' in [2,3,4]:
    print ('True')
else:
    print("False")   # output will be false... as x is not in [2,3,4]


# return True if the sequence of 1,2,3 exist in given list or not.
exList = [1,1,2,3,4,5]
exList2 = [1,1,2,4,1]
exList3 = [1,1,2,1,2,3]

def arrayCheck(nums):
    existt = False
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3 :
            existt = True
            break

    if(existt):
        print("1,2,3 sequence exist in list ")
    else:
        print("string sequence not found..")

arrayCheck(exList)
arrayCheck(exList2)
arrayCheck(exList3)


# check string end with another string:
s1 = "I love India"
s2 = "India"
a = s1.lower()
b = s2.lower()
if a.endswith(b) or b.endswith(a) :
    print("s2 string exist in s1..")
else:
    print("not exist...")

# Double each character of the given string...
s3 = 'mystring'
resultt  = ''
for eachChar in s3:
    resultt += eachChar*2
print("Double each character of {} will get result = {}".format(s3, resultt))


#--------------------------------------------









































