string = "is she is beautiful and she is a good dancer"
print(string.replace("is","was"))
print(string.replace("is","was",2))

print(string.find("is",1))
# tells the interpreter to find the given word from index 1
pos1 = string.find("is")
pos2 = string.find("is", pos1 + 1)
#to find out next "is" after the first "is"
print(pos2)