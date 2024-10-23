# num1 = int(input('enter a number:'))
# num2 = int(input('enter a number:'))

# # Finding the smaller number between num1 and num2
# if num1 < num2:
#     least = num1                                             #GCD
# else:
#     least = num2

# # Start with the smallest number and iterate downwards to find GCD
# div = least
# while div >= 2:
#     if num1 % div == 0 and num2 % div == 0:
#         print('GCD', div)
#         break
#     div = div - 1
# else:
#     print('There is no GCD')



# n=int(input("enter number :"))#               nth primenumbers
# while n>0:
#     i=1
#     c=0
#     while i<=n:
#         if n%i==0:
#             c=c+1
#         else:
#             pass
#         i+=1
#     if c==2:
#         print(n)
#     n=n-1


# n = 10
# num1 = 0
# num2 = 1
# next_number = num2  
# count = 1
 
# while count <= n:
#     print(next_number, end=" ")
#     count += 1
#     num1, num2 = num2, next_number
#     next_number = num1 + num2
# print()



# # Function to generate Fibonacci series up to n terms
# def fibonacci(n):
#     # Initialize the first two terms
#     a, b = 0, 1
#     fibonacci_series = []

#     # Iterate from 0 to n
#     for _ in range(n):
#         fibonacci_series.append(a)
#         # Compute the next term
#         a, b = b, a + b

#     return fibonacci_series

# # Number of terms in the Fibonacci series
# n = 10

# # Generate Fibonacci series up to n terms
# fib_series = fibonacci(n)

# # Print the Fibonacci series
# print("Fibonacci series up to", n, "terms:")
# print(fib_series)



# n=int(input("enter :"))
# for i in range(n): 
#     for j in range(n):
#         print("*",end="")
    
#     print()
#     n-=1

# n=int(input("n :"))
# for i in range(n):
#     for j in range(n):
#         if i==j or j==0 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# x=int(input("enter numbet"))
# y=int(input("enter numbet"))

# if (y-x)>0:
#     print(y,"y is grater")
# else:
#     print(x,"x is grater")



# alpha=0
# digits=0
# spl=0
# for i in v:
#     if i in ("A","Z"):
#         alpha=alpha+1
#     elif i in (0,9):
#         digits+=1
#     else:
#         spl+=1
# print(alpha,digits,spl)
        
        
# l=[0,1,2,3,4,5,6,7,8,9]
# nu=int(input("enter anumber : "))                 # GETTING PAIRS OF INTS SUM OF GIVEN NUM
# l1=[]
# for i in range(len(l)):
#     for j in range(1,len(l)):
#         if l[i]+l[j] ==nu:
#             t=l[i],l[j]
#             t1=l[j],l[i]
#             # if t  and t1 not in l1:
#             if (t and t1 not in l1) and l[i] != l[j]:
#                 l1.append(t)
# print(l1)

# OUTPUT:[(0, 6), (1, 5), (2, 4)]     


# n=5 
# i=0
# while i<=n:       #90 trinagel by while loop
#     c=1
#     while c<=i:
#         print(c,end=" ")
#         c+=1
#     print()
#     i+=1



# n=int(input("Enter anumber: "))      #even numbers

# def even(n,l=[]):
#     if n>0:
#         if n%2==0:
#             l.insert(0,n)
#             return even(n=n-1)
#         return even(n=n-1)
#     return l

# print(even(n))




# n=int(input("enter a number :"))
# def prime(n,i=2):
#     if n==1:
#         return "not aaa prime number"
#     if n%i==0:
#         return "Not a prime number"
#     if n>0:
#         return prime(n=n-1)
#     return "prime"

# print(prime(n))

# print(123//10,123%10)

# n=145
# e=n
# s=0
# while e!=0:
#     r=e%10            #checking Strong number
#     r1=1
#     i=1
#     while i<=r:
#         r1*=i
#         i+=1
#     s=s+r1
#     e=e//10
# if s==n:
#     print("strong number ")
# else:
#     print(" not a strong number ")    



# kk=["yellow","green","orange","blue","black"]             #decoraters

# def reverse(fun):
    
#     def inner(l):
#         l.sort()
        
#         return l
#     return inner

# @reverse
# def mani(l):
#     print("done")
    
# print(mani(kk))
    
    

       
# n=int(input("enter a number :"))
# i=1
# while i<=10:
#     r=n*i
#     print(n,"x",i,"=",r)
#     i+=1
 

# l=[1,2,3,1,2,4,5]
# # s=set(l)
# # c=0
# # for i in s:
# #     r=l.count(i)
# #     if r>1:
# #         c+=1
# # print(c)
# for i in l:



# n=int(input("enter :"))
# t=1
# for i in range(2*n-1):
#     for j in range(2*n-1):
#         if i+j==n-1 or i-j==n-1 or j-i==n-1 or i+j==(2*n)+2:
#             print(t,end=" ")
#         else:

#             print(" ",end=" ")
#     if i<n-1:
#         t+=1
#     else:
#         t-=1
#     print()
        
#         1
#       2   2       
#     3       3     
#   4           4   
# 5               5 
#   4           4   
#     3       3     
#       2   2       
#         1



# s="python"
# x=0
# t=2
# for i in range((len(s)*2)):
#     if i< len(s)+1:
#         print(s[x:i])
#     else:
#         print(s[x:(i-t)])
#         t=t+2

# p
# py
# pyt
# pyth
# pytho
# python
# pytho
# pyth
# pyt
# py
# p



# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or j==n-1 or i==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()



# n=int(input("enter a number :"))
# v=ord("A")
# for i in range(n):
#     a=v
#     for j in range(n):
#         print(chr(v),end=" ")
#         v+=n
#         while v>ord("Z"):
#              v=v-26
        
#     v=a+1
    
#     print()
#     if v>ord("Z"):
#         v=ord("A")



# n=int(input("n:"))
# b=0
# p=0
# while n>0:
#     rem=n%2
#     b=rem*10**p+b                        dec----to---bin
#     n=n//2
#     p+=1
# print(b)

# n=int(input("enter the hour :"))
# m=int(input("enter the mnt: "))
# h= (n % 12 + m / 60) * 30
# minute_angle = 6 * m
# angle = abs(h - minute_angle)
# print(min(360 - angle, angle))




# n=5
# s="VVCUBEPVT"
# for i in range(2*n-1):
#     for j in range(2*n-1):
#         if i==n-1:
#             print(s[j],end=" ")
#         elif ((i+j>=n-1 and j-i<=n-1) and i<n-1) or (i-j<=n-1 and i+j<=2*n+2 and i>n-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()



# n=3
# v=ord("a")+n-1
# c=0  
# for i in range((2*n)-1):
#     t=n+1
#     for j in range(n*n):
#         if  :
#             print(chr(v),end="")
#         else:
#             print("-",end="")
    
#     print()  



# def mani(fun):
#     def inner(h1):
#         return h1+"hello"
#     return inner

# @mani
# def hi(h1):
#    pass
    
# print(hi("mani"))


# def print_rangoli(size):
    # row = size + (size-1)
    # col = row + (row-1)
    # n = (row/2)+0.5
    # mul = 1
    # for i in range(1, row+1):
    #     s = [chr(97+size-j) for j in range(1, mul+1)]
    #     r = list(reversed(s))
    #     s = s[:-1]+r
    #     s = '-'.join(s)
    #     if i >= n:
    #         mul -= 1
    #     else:
    #         mul += 1
    #     print(s.center(col, '-'))
        

# print_rangoli(int(input("enter a number :")))


# def decc(fun):
#     def inner(y):
#         return "hello "+y+" welcome"
    
#     return inner
    



# @decc
# def m1(e):
#     print("done")
    
    
# print(m1("Vcube"))
    

# n=int(input("enter a number "))           #  prime facter
# for i in range(2,n+1):
#     if n%i==0:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i,end=" ")
                       
# enter a number 20
# 2 5  
      
 
 
# num1 = 12
# num2 = 18
# larger_num = max(num1, num2)
# smaller_num = min(num1, num2)
# lcm = larger_num

# while True:
#     if lcm % smaller_num == 0:
#         # If the LCM is divisible by the smaller number, it is the LCM of both numbers
#         break
#     else:
#         # Increment the LCM by the larger number and check again
#         lcm += larger_num

# # Print the result
# print(f"The LCM of {num1} and {num2} is {lcm}")






# s='''i am mani                                    # counting lines words characters od str
# i am mani'''
# ch_c=0
# line_c=len(s.split("\n"))
# w_c=0
# for i in range(len(s)):
        
#     if len(s.split(" ")) > 1:
#         w_c = len(s.split(" "))
        
#     if len(s.split(" ")) == 1:
#         w_c = 1
        
#     if s[i].isalpha():
#         ch_c += 1
        
#     if s[-1]==" ":
#            w_c-=1 
                    
# print("lines-->\t",line_c ,"\n","words -->\t",w_c,"\n","characters-->\t",ch_c)








# s="122231111"                        #counting elements in string
# c=0
# p=s[0]
# for i in s:
#     if i==p:
#         c+=1
#     else:
#         print((c,int(p)),end="")
#         c=1
#         p=i
# print((c,int(s[-1])))

# output:(1, 1)(3, 2)(1, 3)(1, 1)


# n=int(input("n :"))
# l=[]
# for i in range(n):                        #converting value in data type 
#         s=input("enter element:")
#         try:
#                 v=int(s)
#         except:
#                 try:
#                         v=float(s)
#                 except:
#                         try:
#                                 v=complex(s)
#                         except:
#                                 v=s
#         l.append(v) 
# print([type(i) for i in l])



# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)

#     def __str__(self):
#         return f"({self.x}, {self.y})"

# # Create two Vector objects
# v1 = Vector(1, 2)
# v2 = Vector(2, 3)
# v3 = Vector(1, 2)
# # # Use the overloaded + operator
# # result = v1 + v2
# # print(result)  # Output: (4, 6)

# print(v1+v2)
# print(v1.__str__())

# L=[1,2,[3,4],(5,6),{7,8}]
# l1=[]
# for i in L:
#     if type(i)==():
#         for j in i:
#             l1.append(j)
# print(l1)

# l=[0,1,2,3,4,5,6,7,8,9]
# nu=6
# l1=[]
# for i in range(len(l)):
#     for j in range(1,len(l)):
#         if l[i]+l[j] ==nu:
#             t=l[i],l[j]
#             t1=l[j],l[i]
#             if t and t1 not in l1:
#                 l1.append(t)
# print(l1)


# s = "rfdeeejkaaaajoaeiourduuudnfaaaa"
# y = "aeiouAEIOU"

# def extract_substrings(s, vowels):
#     substrings = []
#     current_substring = ""
#     surrounded_by_consonants = True

#     for char in s:
#         if char in vowels:
#             current_substring += char
#             surrounded_by_consonants = False
#         elif not surrounded_by_consonants:
#             if len(current_substring) > 2 and current_substring[0] == current_substring[-1]:
#                 substrings.append(current_substring)
#             current_substring = ""
#             surrounded_by_consonants = True
#         else:
#             surrounded_by_consonants = True

#     return substrings

# result = extract_substrings(s, y)
# print(",".join(result))

# n=5

# 1
# 121
# 12321
# 1234321
# 123454321

# for i in range(1,n+1):
#     l=[j for j in range(1,i+1)]
#     d=l+l[-2::-1]
#     print("".join(map(str,d)))



# s=input("Enter email:")
# if "@gmail.com" in s:
#     print(s[:2]+"*"*(len(s)-12)+s[len(s)-10:])
# else:
#     print("not a valid g mail")

# d= int(input("enter a number ")  )         
# b= ""
# while d > 0:
#     r = d % 2
#     b = str(r) + b
#     d //= 2
# print(b)


# l=[ input() for i in range(int(input()))]
# print(l)




# l=[30,"Py",50,80,30,"Jy",20,90,60,"Qy",10]
# for i in range(len(l)-1):                                       #sorting only strings in list
#         for j in range(i+1,len(l)):
#             if (type(l[i])==type(l[j])  and type(l[i])==str):
#                 if l[i]>l[j]:
#                     l[i],l[j]=l[j],l[i]
# print(l)


# n=int(input("enter: "))
# for i in range(0,n+1,2):
#     if i==n:
#         print("even")
#         break
#     else:
#         print("odd")
#         break



# l=[5,[1,2],8,[3,4],[5,6]]

# def f(l):                                     #sum of the list elements
#     t=[]
#     for i in l:
#         if type(i)==list:        
#             t=t+f(i)
#         else:
#             t.append(i)
#     return t
# print(f(l))


# n=int(input("n: "))
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==n-1 or i+j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()    

# l=[82,76,69,45,92,32]
# for i in range(1,6):
#    l[i-1]=l[i]
# for i in range(0,6):
#     print(l[i],end=" ")

# n=5
# v=ord("A")
# for i in range(n):
#     a=v
#     for j in range(n-i):
#         print(chr(v),end=" ")
#         v+=1
#     v=a+1
#     print()
    
# a=list(map(lambda x:x*2,[i for i in range(50)]))
# print(a)

# n=int(input("n:"))
# s="*PYT*HON*"
# for i in range(2*n-1):
#     for j in range(2*n-1):
#         if i==n-1:
#             print(s[j],end=" ")
#         elif ((i+j>=n-1 and j-i<=n-1) and i<n-1) or (i-j<=n-1 and i+j<=2*n+2 and i>n-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# n=5
# for i in range((2*n)-1):
#     for j in range(n):
#         if j<=i and i+j<=2*n-2 :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
    


# l=[1,[2,3],4,[5]]
# t=0
# def f(l):                                     #sum of the list elements
#     global t
#     for i in l:
#         if type(i)==int:        
#             t=t+i
#         else:
#             f(i)
#     return t
# print(f(l))



# n=5
# t=0
# for i in range(2*n-1):
#     print(" *"*(t+1)+"  "*(n-t))   #single loop
#     t=t+1 if i<n-1 else t-1
    
# print()


# l=[122,345,765,234,9876]
# l1=[]
# for i in l:
#     s=""
#     for j in str(i):
#         s=j+s
#     l1=l1+[int(s)]
# print(l1)
        
        
# # Original list of integers
# l = [122, 345, 765, 234, 9876]

# # Using nested list comprehension to reverse each integer in the list
# l1 = [''.join([i[j] for j in range(len(i)-1, -1, -1)]) for i in [str(num) for num in l]]

# print(l1)

    
# def r(n):
#     t=[int(i) for i in str(n)]
#     if len(str(t))>=2:
#         return r(t)
#     else:
#         return t
    
# print(r(5643))


# n=5643
# while True:
#     s=0
#     while n>0:
#         r=n%10
#         s=s+r
#         n=n//10
#     if s>9:
#         n=s
#     else:
#         break
# print(s)
    


# count=0                                                   #countins 2 only 
# for i in range(2,35+1):
#     if len(str(i))<=1 and "2" in str(i):
#         count+=1
#     else:
#         for j in str(i):
#             if "2" in j:
#                 count+=1
# print(count)


# n=int(input("n:"))
# s="Vcubesols"
# for i in range(2*n-1):
#     for j in range(2*n-1):
#         if i==n-1:
#             print(s[j],end=" ")
#         elif ((i+j>=n-1 and j-i<=n-1) and i<n-1) or (i-j<=n-1 and i+j<=2*n+2 and i>n-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()



#         1
#       2   2       
#     3       3     
#   4           4   
# 5               5 
#   4           4   
#     3       3     
#       2   2       
#         1




# n=int(input("enter :"))
# t=1
# for i in range(2*n-1):
#     for j in range(2*n-1):
#         if i+j==n-1 or i-j==n-1 or j-i==n-1 or i+j==(2*n)+2:
#             print(t,end=" ")
#         else:
#             print(" ",end=" ")
#     if i<n-1:
#         t+=1
#     else:
#         t-=1
#     print()



# n=int(input("n: "))
# v=65
# for i in range(n):
#     a=v
#     l=1
#     for j in range(n):
#         if i+j>=n-1:
#             print(chr(v),end=" ")
#             v=v+n-l
#             l+=1
#             if v>ord("Z"):
#                 v=ord("A")
#         else:
#             print(" ",end=" ")
#     print()
#     v=a+1

