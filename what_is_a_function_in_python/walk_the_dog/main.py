def describe_dog (name, breed, age):
    if age < 0 :
        return f"Invalid age for {name}. Age cannot be negative."
    elif age == 0:
        return f"{name} is a newborn {breed}. A bundle of joy!"
    elif age == 1:
        return f"{name} is a {age}-year-old {breed}. A great companion!"
    elif age > 1:
        return f"{name} is a {age}-year-old {breed}. An old dog with much wisdom!"

#my_dog = describe_dog("Thor", "Rotwailler", 12)
#print(my_dog)
        
# Test the function with various scenarios
description = describe_dog("Buddy", "Labrador", 3)
print(description)