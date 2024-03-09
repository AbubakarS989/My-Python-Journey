print("Variable in Python Day 02 ")
# I import date time module which basically enable me to print date time
from datetime import datetime

# now() means current or i want current date so i write 
# now().date() - this show me the current date.
print("Date:",datetime.now().date())


# !Day 02 Variables
# These are used to store data into the memory
# It can store:
# !integers - 2,45, etc
# !Character - 's'
# !String - "HI"
# !boolean- True False
# !Floating point - 0.34 , 4.3
#! Complex number - 3+2i
#! Tuple
#! List
#! Mapped Data Dictionary 

#! integers 

num=34
print(num)

#! Character - 's'
# When we write one single character within single quotes,it will become character
# only one character is allowed to write. 
ch='a'
print(ch)


#! String - "HI"
#Just like Character, When we write multiple character within double quotes,it will become string type
# No limit of character

name="Abubakar"
print(name)

# !boolean- True False
# True means 1 and False means 0.
# We can store  them into variables or use in any condition , where u need to make true or false.

BOOL=True
print(BOOL)

# In condition 
# while True:
#     print("HI")

# !Floating point - 0.34 , 4.3
height=5.6
print(height)


# !Complex NUmber -  3+9i
COMplex=complex(2,3)
print(COMplex)


print("The type of num is :",type(num))
print("The type of name is :",type(name))
print("The type of ch is :",type(ch)) #We can check type of each value.
print("The type of height is :",type(height))
print("The type of BOOL is :",(type(BOOL)))
print("The type of COMPLEx  is :",type(COMplex))




#! All data type have some limit to store date inside them.
