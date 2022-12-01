name, character = input("enter name and a character ").split(",")
a = name.lower()
print(len(name))
print(a.count(character.lower()))
#the thing to observe is while giving space in input after comma you will ge the output as 0 even we have the characters which have been repeated we will fix this in next class