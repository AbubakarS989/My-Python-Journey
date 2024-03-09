dictionary = {
    "pineapple": "A tropical fruit with a rough, spiky exterior and sweet, juicy flesh.",
    "watermelon": "A large, round fruit with a thick green rind and sweet red flesh.",
    "blackberry": "A small, dark purple berry that grows on bushes and is often used in desserts.",
    "blueberry": "A small, round, dark blue fruit that grows on bushes and is often eaten fresh or used in baking.",
    "cantaloupe": "A type of melon with a pale orange flesh and a sweet, musky aroma.",
}


# function: that check food is present in the dictionary or not and return value
def fruit_check(fruit):
    if fruit in dictionary:
        return dictionary[fruit]
    else:
        return "No food is found in dictionary"




# loop that run until user enter 'q'to quit program
while True:
    fruit= input("Enter a name of fruit:\nEnter 'q'to quit:")
    if fruit=='q':
        break
    
    # call function and pass the value entered by the user
    meaning=fruit_check(fruit)
    # print the value given by the function
    print(meaning)