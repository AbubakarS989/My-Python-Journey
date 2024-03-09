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


#! List - [2,34,"ahmad",'a']
# It is an ordered collection of data with element separated by comma and enclosed within square brackets
# We can change list data using list method, can be modified after creation. 
list_name=["ahmad","ali","rehman",4,34.4]
print(list_name)

# ! Tuple
# It is an ordered collection of data with element separated by comma and enclosed within parenthesis
tuple_name=(3,4,("helo"))
print(tuple_name)


#! Mapped Data Dictionary 
# A dictionary is an unordered collection of data containing a key-value pair.
# The key-value pair enclosed within curly brackets 

dict1={
    "name":"Ali",
    "age":22
}
print(dict1)
# here key is [name] and value is [ali]
# here key is [age] and value is [22]
# we can access value of any key using key name.




#We can check type of each value.
print("The type of num is :",type(num))
print("The type of name is :",type(name))
print("The type of ch is :",type(ch)) 
print("The type of height is :",type(height))
print("The type of BOOL is :",(type(BOOL)))
print("The type of COMPLEx  is :",type(COMplex))
print("The type of List name  is :",type(list_name))
print("The type of Tuple name is  is :",type(tuple_name))
print("The type of Dict1 is :",type(dict1))




#! All data type have some limit to store date inside them.
