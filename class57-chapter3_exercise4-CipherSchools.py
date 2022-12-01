n = input("enter number more than one digit: ")
# method to solve problem in human language is called algorithm
#don't convert them to int let them be in string form but transform it to int seperately in loop
i = 0
total = 0
while i < len(n):
    total += int(n[i])
    i += 1
print(total)