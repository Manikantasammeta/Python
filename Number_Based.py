# n=int(input("n:"))
# r=n*n
# s=r%10
# print(s)
# if s==n:
#     print("it is a Automorphic number")                AMSTRONG NUMBER
# else:
#     print("it is not a Automorphic number")

# n:5
# 5
# it is a Automorphic numbe



# n=int(input("n:"))                                                            DECIMAL---TO---> HEXA
# hexa=""                                                                                       
# d={0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
# while n>0:                                                        
#     rem=n%16
#     hexa=d[rem]+hexa
#     n=n//16
# print(hexa)

# n=(input("n:")).upper()
# dec=0
# p=0
# for i in n[::-1]:
#     if i in "ABCDEF":
#         rem=ord(i)-55                                     hexa----to---->  desimal
#     else:
#         rem=int(i)
#     dec=rem*16**p+dec
#     p+=1
# print(dec)











# n=int(input("n:"))
# b=0
# p=0
# while n>0:
#     rem=n%2
#     b=rem*10**p+b                        dec----to---bin
#     n=n//2
#     p+=1
# print(b)

# d= int(input("enter a number ")  )         
# b= ""
# while d > 0:
    
#     r = d % 2
#     b = str(r) + b
#     d //= 2
# print(b)



# n=int(input("n:"))
# b=0
# p=0
# while n>0:
#     rem=n%10
#     b=rem*2**p+b                        bin----to---dec
#     n=n//10
#     p+=1
# print(b)

# n=int(input("n:"))
# r=n*n
# rh= r%10
# if n==rh:
#     print("it is Automorphic")
# else:
#     print("not a Automorphic")

# n=int(input("enter num :"))
# s=0
# for i in range(1,n):
#     if n%i==0:
#         s+=i
# if n==s:
#     print("it is aperfect number")
# else:
#     print("it is not a perfect number")
  
# enter num :28
# it is aperfect number

# enter num :32
# it is not a perfect number

# import random as rm





# class mylist :
#     def __init__(self,n):
#         self.n=n
#         self.l=[rm.randint(1,50) for i in range(self.n)]
#         print(self.l)
#     def prime(self):
#         l2=[]
#         for i in self.l:
#             for j in range(2,i):
#                 if i%j==0:
#                     break
#             else:
#                 l2.append(i)
#         if not l2:
#             return -1
#         else:
#             return l2
        
#     def fact(self):
#         d={}
#         def fun(l,k=1):
#             if l>0:
#                 return fun(l-1,k*l)
#             return k
        
#         for i in self.l:
#             r=fun(i)
#             d.update({i:r})
#         return d

# l=mylist(10)
# print(l.prime())
# print(l.fact())



# n=int(input("n:"))
# n1=1
# val=ord("A")
# for i in range(n):
#     a=val
#     for j in range(n):
#         if i==j:
#             print(n1,end=" ")
#             n1+=1
#         elif i>=j:
#             print(chr(val),end=" ")
#             val+=1
#         else:
#             print(" ",end=" ")
#         while n1>9:
#             n1=1
#         while val>ord("Z"):
#             val-26
            
#     print()
#     val=a 



