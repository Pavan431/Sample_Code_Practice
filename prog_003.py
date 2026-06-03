def test_1():
    list1=[]
    for i in range(1,21):
        if i%2==0:
            #print(i,end=" ")
            list1.append(i)

    return list1

def test_2():
    for i in range(1,11):
        print(i,end=" ")


print(test_1())
test_2()
