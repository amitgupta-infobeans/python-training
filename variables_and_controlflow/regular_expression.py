import re

patterns = ['test1', 'test2']

msg = "making it look like test1 readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model textContent here, content here', making it look like test2 readable English. Many desktop publishing packages and web page editors now use Lorem test1 Ipsum as their default model text, and a search for 'lorem ipsum' test1 will uncover many web sites still in their in"


# matchh = re.search('test1', msg)
matchh = re.findall('test1', msg) # 3 occurance..
print(matchh)

for pattern in patterns:
    print("I am searching for ", pattern)
    if re.search(pattern, msg):  # return  boolean value either : True or False..
        print("Match...")
    else:
        print("Not found...")


# findd = ['sd*']    # zero of more d
# findd = ['sd+']    # atleast one more d
# findd = ['sd?']    # zero or one time of d
# findd = ['sd{3}']  # exact 3 occurance of d after s
# findd = ['^ !?@.']+  # does not contain ?, @, . ! in output..

# [r'\s+'] for spacess,    [r'\d+'] for one or more numbers,    [r'\D'] for not numbers

# a = 'this is a string having number 345'
# nummPattern = "[r'\d+']"
# ans = re.findall(nummPattern, a)
# print('STRING CONTAIN NUMBERS', ans)

matc_string = 'sd{3}'
msg2 = "ish. Many desktop publishing sdddd packages and wesddddb page editors now use Lore sddd m Ipsum as their sddd defaultsdddd model textContent here, content here', making it look lisddddke test2 r"
print(re.findall(matc_string, msg2))