

# def even(n,i=0):
#     if n!=0:
#         print(i*2,end=" ")
#         even(n=n-1,i=i+1)                         # n even numbers
# even(int(input("enter a number: ")))

#output:
# enter a number: 5
# 0 2 4 6 8 



# def even(n,i=0):
#     if n!=0:
#         print((i*2)+1,end=" ")
#         even(n=n-1,i=i+1)                         # n odd number numbers
# even(int(input("enter a number: ")))

# output:
#     enter a number: 5
#     1 3 5 7 9 



# def Fun(n,i=2):
#     if n%i==0 :
#         return True                     #  checking prime number
#     if i * i > n:
#         return False
#     return Fun(n,i=i+1)
        
# res=Fun(5)
# print(res)
        
        
# output
# enter a number:5
# prime

# enter a number:6
# not a prime 
    
    
# def prime_numbers(n, num=2, count=0):           # n prime numbers
    
#     def is_prime(num):
#         for i in range(2,num):
#             if num%i==0:
#                 return False
#                 break
#         else:
#             return True
#     if count==n:
#         return
#     if is_prime(num):
#         print(num,end=" ")
#         prime_numbers(n, num + 1, count + 1)
#     else:
#         prime_numbers(n, num + 1, count)
        
# prime_numbers(int(input("enter a  number :")))


# enter a  number :5
# 2 3 5 7 11 


# def fact(n,i=1):                  # factorial of a given number with using recursive function
#     if n!=0:
#         return n*fact(n=n-1)
#     return i
# print(fact(int(input("enter a number: "))))

# enter a number: 5
# 120



# def is_strong_number(num, total=0):              
#     def factorial(n):
#         if n == 0:
#             return 1
#         else:
#             return n * factorial(n - 1)

#     if num == 0:
#         return total == 0
#     else:
#         digit = num % 10
#         return is_strong_number(num // 10, total + factorial(digit))
    
# res=is_strong_number(145)
# print(res)


# # Test the function
# number = 145
# if is_strong_number(number):
#     print(f"{number} is a strong number")
# else:
#     print(f"{number} is not a strong number")


# def f(n):
#     print(n,end='')                       # some pgr
    
#     if n>0:
#         f(n=n-1)
#         print(n,end="")
            
# f(5)
#outPut:54321012345



# l=[[1,2],[3,4],[5,6]]

# def f(l):                                     #sum of the list elements
#     t=0
#     for i in l:
#         if type(i)==list:        
#             t=t+f(i)
#         else:
#             t+=i
#     return t
# print(f(l))

# outPut:21



# def even(n):
#     if n>0:
#         even(n-1)
#         print((n-1)*2,end=" ")

# even(5)



# def r(n,s=0):        #counting the numbers 
#     if n>9:
#         while n>0:
#             t=n%10
#             s=t+s
#             n=n//10
#         if s>9:
#             return r(n=s)
#         else:
#             return s
# print(r(5643))

# 5+6+4+3=18-->1+8=9

#output=9



# def is_strong_number(num, total=0, original=None):
#     if original is None:
#         original = num
#     def factorial(n):
#         if n == 0:
#             return 1
#         else:
#             return n * factorial(n - 1)
#     if num == 0:
#         return total == original 
#     else:
#         digit = num % 10 
#         return is_strong_number(num // 10, total + factorial(digit), original)

# res = is_strong_number(145)
# print(res) 


x=[1,2,3,[4,5],[6,7,8],9]

def fun(x,l=[]):

    for i in x:
        if type(i)==list:
            fun(i)
        else:
            l+=[i]
    return l
print(fun(x))
            
