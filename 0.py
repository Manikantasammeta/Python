
# n=int(input("'n:"))
# if n==1:
#     print("it is not a prime number")
#     exit()
# def fun(n,s=True,a=2):
#     if a<n:
#         if n%a==0:
#             s=False
#         return fun(n,a+1,s)
#     return s
# p=fun(n)
# if p==False:
#     print("is not a prime")
# else:
#     print("is prime")


# n=5
# s="PYSPIDERS"
# for i in range(2*n-1):
#     for j in range(2*n-1):
#         if i==n-1:
#             print(s[j],end=" ")
#         elif (i-j<=1 and i+j<=n+n//2) or (i+j>=2*n-1 and i-j<=1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=int(input("n:"))
# s="PYSPIDERS"
# for i in range(2*n-1):
#     for j in range(2*n-1):
#         if i==n-1:
#             print(s[j],end=" ")
#         elif (j+i>=n-1 and j-i<=n-1) or (i-j>=n-1 and i+j<=2*2+2):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=int(input("n :"))
# a=n
# sum=0
# mul=1
# while n>0:
#     r=n%10
#     sum=sum+r
#     mul=mul*r
#     n=n//10
# if sum==mul:
#     print(a,"is a spynumber")
# else:
#     print(a,"is not a spynumber")

# def fun(n,i=0):
#     if i<n:
#         print(i*2,end=" ")
#         fun(n,i+1)
# fun(int(input("n:")))

# t=(1,2,3,4,5,6,7,8,1,2,3,6)
# d={}
# for i in t:
#     r=t.count(i)
#     d.update({i:r})
# print(d)

# [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
# l1=[1,2,3,4]
# l2=[1,4,5,6,7,8]
# d1={}
# for i in l1:
#     r=l2.count(i)
#     d1.update({i:r})
# print(d1)


# l1=[1,2]
# l3=[3,4,5]
# l=[]


# s=[l1,l3,l1]
# for i in s:
#     if not i:
#         print(s[i])
#     else: pass



# x=10
# y=10
# print(id(x))
# print(id(y))



# n=int(input("enter a number:"))
# for i in range(1,11):
#     d=n*i
#     print(f"{n} x {i} = {d}")


# n=int(input("enter num :"))
# t=1
# for i in range(2*n-1):
#     print("  "*(n-t)+" *"*t)
#     t=t+1 if i<n-1 else t-1
# print()


# n=int(input("enter:"))
# s=str(n)
# t=0
# l=len(str(n))
# for i in range(l):
#     r=int(s[i])**l
#     print(r)
#     t+=r
# print(t)


# n=int(input("enter num:"))
# l=[]
# for i in range(2,n):
#     if n%i==0:
#         l.append(i)
# print(*l)

# ot-->

# enter num:44
# 2 4 11 22
# n=5
# for i in range(1,2*n):
#     if i<n+1:
#         print(i,end=" ")
#     else:
#         print(n-i+n,end=" ")

# x=10
# y=20
# print(x.__add__(y))
# print(x.__mod__(y))
# print(x.__divmod__(y))
# print(x.__mul__(y))
# print(x.__sub__(y))


# d={1:2,2:4,5:3,3:8,9:4}
# for i in d.keys():
#     print(id(i))


# from turtle import *


# def m():
#     for i in range(300):
#         circle(190-i,90)
#         left(90)
#         circle(190-i,90)
#         left(18)
#         circle(190-i,90)
#         left(79)
        
# m()
# mainloop()

# import turtle as td

# for i in range(100):
#     td.speed(3)
#     td.pencolor("green")
#     td.write("i am mani reddy")
#     td.forward(5)


# class no(Exception):
#     pass


# try:
#     n1=int(input("enterage :"))
#     if n1<21:
#         raise no
# except no:
#     print("not valid")
# else:
#     print("valid") 


# s="i am manikanta Reddy  maniand i am from mani Bapatla College of Arts & Sciences and mani my phon number is mani 8897672572"
# e=['[a-z]+']
# e1=re.findall(s,e)
# print(e1)

# def check(patteren,pahara):
#     for i in patteren:
#         print(re.findall(i,pahara))
# pahara = "i am the Mani reddy and I am The King"
# patteren = ['[A-Z]+'+'[a-z]+']
# check(patteren,pahara) 

# s=input("enter gmail:")
# l1=["gmail.com","gmail.in","gmail.ogr"]
# import re
# t1=re.split("@",s)
# t2=t1[-1]
# s2=" "
# if s2 in s:
#     print("not valid") 
# if t2[1]==int(s[0]):
#     print("not valid")
# else:
#     if t2 in l1:
#         print(s)
#         print("valid")
#     else:
#         print(s)
#         print("not valid")



# class mani():
    
    
#     def __init__(self):
#         self.name="mani"
#         self.age=21
#         self.gender="mail"
#         self.ph=123456789
        
        
#     def getname(self):
#         return self.name
    
#     def getph(self):
#         return self.ph
    
#     def getage(self):
#         return self.age
    
#     def setname(self,name):
#         self.name=name
    
#     def setph(self,ph):
#         self.ph=ph
        
        
# m=mani()
# print(m.getage())
# print(m.getname())
# m.setname("reddy")
# print(m.getname())




# d={1:34,4:12,7:65,48:89,9:77,6:34,64:12,95:34,41:56}
# l=list(d.keys())
# l.sort()
# print(l)
# d1={d[i]:i for i in l}
# print(d1)


# l=[("mani",9),("reddy",6),("poja",7),("rowdy",4)]


# s=input("enter  str :")
# s= "pwwkew"
# c=0
# for i in range(0,len(s)):
#     for j in range(i):
#         if s[i]!=s[j]:
#             c+=1
#         elif s[i]==s[j]:
#             c==0
# print(c)


# def length_of_longest_substring(s):
#     # Initialize a dictionary to store the last seen index of each character
#     char_map = {}
#     max_length = 0
#     start = 0

#     for end in range(len(s)):
#         # If the current character is already in the dictionary and its index is greater than or equal to the start index,
#         # update the start index to the next index of the repeated character
#         if s[end] in char_map and start <= char_map[s[end]]:
#             start = char_map[s[end]] + 1

#         # Update the last seen index of the current character
#         char_map[s[end]] = end

#         # Update the maximum length if necessary
#         max_length = max(max_length, end - start + 1)

#     return max_length

# # # Test the function with the provided examples
# # s1 = "abcabcbb"
# # print(length_of_longest_substring(s1))  # Output: 3

# # s2 = "bbbbb"
# # print(length_of_longest_substring(s2))  # Output: 1

# # s3 = "pwwkew"
# # print(length_of_longest_substring(s3))  # Output: 3

# print(length_of_longest_substring(input("enter str: ")))



n=input("enter str :")
s=""
for i in range(len(n)):
    if n[i].isnumeric:
        s=str(n[i])+s
if s[0]=="0":
    s=s[1:len(s)]
if s[-1] in ['-','$','+','/']:
    s=s[-1]+s[0:len(s)-1]
print(s)