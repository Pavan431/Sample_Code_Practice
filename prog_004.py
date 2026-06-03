'''
list1=["google.com","facebook.com","naukri.com","linkedln.com","gmail.com"]

print(list1[0])
print(list1[len(list1)-1])

for i in range(len(list1)):
    print(list1[i])


num=int(input("Enter the number:"))


if num%3==0 and num%5==0:
    print(f"Given number {num} is divisble by 3 and 5")
else:
    print("Given number is not divisible by 3 and 5")
'''


num=int(input("Enter the number:"))

for i in range(1,11):
    res=num*i
    print(num,"*",+i,"=",+res)
