# global var
x = 5

def myfun():
    x = 50   # local scope
    return x

print(x)  # print global variable value.
print(myfun())  # print local variable...

x = myfun()  # global variable now change to 50
print("now x has updated bcoz myfun return some value ",x)


# global keyword:
y = 50
def changeGlobal():
    global y  # we are using global y here...
    y = 500

print("y before function call ",y)
changeGlobal()
print("y has been changes now =",y)  


# NOTES:  Try to don't use global keywords in place of it we can return value from the function...

#  ----------------------------Class and Object ----------------------------------------------------#
class Sample:
    pass
objS = Sample()
print( type(objS ))


class Circle():

    pi = 3.14
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def __str__(self):
        return "string representation..."
    
    def __del__(self):
        # print("a circle ci has been deleted...")
        pass

obct = Circle(3)
obctDel = Circle(4)
print(obct)
#del obctDel # to delete the object....
print("Circle radius ", obct.radius)
print("Area of circle ", obct.area())

try:

    filee = open('myfile.txt', 'r')
    content = filee.read()
    print(content)

    # writefilee = open('myfile.txt', 'w')
    # writefilee.write("Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model tny web sites still in their infancy, and a search for 'lorem ipsum' will uncover many web sites still in their infancy")

except: # catch the exception..
    # This section will execute if any error Occured...
    print("Hnadle Execption here if any error found")

#=============== This else is optionally, We can use finally in place of it....
# else:
#     # this else corresponding to the exception. If no exception found than run else block..
#     print("NO ERROR FOUND!")
#     filee.close()
#     # writefilee.close()
#==============================================
finally:
    # This block will always be executed...
    print("I am Final block and will always be executed on success or failure....")
    filee.close()
    # writefilee.close()







