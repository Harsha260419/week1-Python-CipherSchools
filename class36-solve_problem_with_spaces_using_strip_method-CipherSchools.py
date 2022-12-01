name, character = input("enter name and a character ").split(",")
print(len(name))
something = name.strip().lower().count(character.strip().lower())
print(something)