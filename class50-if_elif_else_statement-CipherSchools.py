age = input("please input your age: ")
age = int(age)
if age <=0:
    print("age is not relevant please type the relevant age")
if 0 < age <= 3:
    print("ticket price : free")
elif 3 < age <= 10:
    print("ticket price : 150")
elif 10 < age <= 60:
    print("ticket price : 250")
