S1=input("Enter the string with combination of letters and numbers")

count=0
for i in S1:
    if i.isdigit():
        count+=1

print(f"Total digits in given string is {count}")
