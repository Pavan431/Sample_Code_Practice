
'''
import time

def timer(func):
    def wrapper():
        start= time.time()
        func()
        time.sleep(5)
        end= time.time()
        print("Time taken",end-start)
    return wrapper

@timer
def time_diff():
    print("Function is running")
    
time_diff()

'''
'''
#Check how many times that decorator is called 
def my_decorator(func):
    count=0
    def wrapper():
        #print(count)
        nonlocal count
        count+=1
        print("Decorator called for ",count,"times")
        func()
        
    return wrapper

@my_decorator
def test_sample():
    print("Calling function")

test_sample()
test_sample()
test_sample()

'''
'''
#Runs the wrapper function if  the given num is positive else prints the error
def my_decorator(func):
    def wrapper(n):
        if n>0:
            print("Given number is positive")
            func(n)
        else:
            print("error")
    return wrapper

@my_decorator
def test_num(n):
    print("Function is called")

test_num(4)
test_num(-3)
'''



# #print the function name before running the actual function
# def my_decorator(func):
#     def wrapper():
#         Exec_func= func.__name__
#         print(f"Executing function :{Exec_func}")
#         func()
#     return wrapper


# @my_decorator
# def test_sample():
#     print("Function is running")

# test_sample()


# #runs the functio if a variable like allowed is true and if not blocks the execution
# def my_decorator(func):
#     def wrapper():
#         if allowed:
#             func()
#         else:
#             print("Not allowed")
#     return wrapper

# @my_decorator
# def test_sample():
#     print("Function called")

# allowed = False
# test_sample()


# #check the condition if age>18 should be eligible for vote and not using raise exception
# def check_age(age):
#     if age<18:
#         raise ValueError("Age is below 18 so not eligible to vote")
#     else:
#         print("Eligible to vote")

# check_age(19)




#Convert string into integer using try except block
def converted_string(Str1):
    try:
        Str1=int(Str1)
        print(Str1)
    except Exception:
        print("Given string in not in digits")

converted_string("40325")
