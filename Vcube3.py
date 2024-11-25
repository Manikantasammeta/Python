# n=int(input("enter: "))
# v=ord("A")+n-1
# for i in range(n):
#     a=v
#     for j in range(n):
#         if i%2==0:
#             if j%2==0:
#                 print(chr(v),end=" ")
#                 v=v-1
#             else:
#                 print(chr(v+32),end=" ")
#                 v=v-1
#         else:
#             if j%2==0:
#                 print(chr(v+32),end=" ")
#                 v=v-1
#             else:
#                 print(chr(v),end=" ")
#                 v=v-1
                         
#     print()
#     v=a+n
    
# # e d c b a
# # j l h g f 
# # o n m l k
# # t s r q p
# # y x w v u


# n=int(input("n :"))
# val=ord("A")
# for i in range(n):
#     a=val
#     for j in range(n):
#         if i+j>=n-1:
#             print(chr(val),end=" ")
#             val=val+(n-j)
#             if val<ord("A"):
#                 val=ord("Z") 
#         else:
# #             print(" ",end=" ")
# #     print()
# #     val=a+i+2
# #     while val>ord("Z"):
# #         val-=26


# n=5
# val=ord("A")
# for i in range(n):
#     a=val
#     l=1
#     for j in range(n):
#         if i+j>=n-1:
#             print(chr(val),end=" ")
#             val=val+n-l
#             l=l+1
#         else:
#             print(" ",end=" ")
#     print()
#     val=1+a

# n=int(input("n: "))
# v=ord("A")
# for i in range(n):
#     a=v
#     x=1
#     for j in range(n):
#         if i+j>=n-1:
#             print(chr(v),end=" ")
#             v=v+n-x
#             x=x+1
#             if v>ord("Z"):
#                 v=ord("A")
#         else:
#             print(" ",end=" ")
        
#     print()
#     v=a+1
#     if v>ord("Z"):
#             v=ord("A")
   
#         A
#       B F
#     C G J
#   D H K M
# E I L N O  
 


# def prime(n): 
#     for i in range(2,n):
#         if n%i==0:
#             return False
#             break
#     else:
#         return True   

# for i in range(2,100):
#     if prime(i):
#         print(i,end=",")

# d={'b': 3, 'a': 2, 'c': 1}            #  WITH  OUT SORT METHOD IN LIST ASC
# d1={}                                  # by VALUES
# val = list(d.values())

# val.sort()
# print(val)
# for i in range(len(val)): 
#     for key, value in d.items():
#         if value == val[i]:
#             d1[key] = value
# print(d1)

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

# import random as rm
# no=int(input("no of pass:"))
# lnt=int(input("length od pass :"))
# A=[chr(96+i) for i in range(1,27)]
# a=[chr(64+i) for i in range(1,27)]
# a1=[str(i) for i in range(10)]                            #creating  a password by tacking user input
# l=a+A+a1
# l1=[]
# while len(l1)<no:
#     s2=""
#     while len(s2)<lnt:
#         c=rm.choice(l)
#         if c not in s2:
#             s2+=c
# print(l1)



# import random as rm
# lower=[chr(96+i) for i in range(1,27)]
# Upper=[chr(64+i) for i in range(1,27)]
# number=[str(i) for i in range(10)] 
# spl=[chr(i) for i in range(33,48)]  #creating  a password by tacking user input
# l=Upper+lower+number+spl
# s2=""
# while len(s2)!=10:
#     c=rm.choice(l)
#     if c not in s2:
#         s2+=c
        
# s2=rm.choice(Upper)+s2+"#"
# print(s2)
# rm.s
    
# from math import factorial
# import random as rm

# s=input("enter str:")                                         #creating the different patterens based on the user in put
# l=[]
# while len(l)<factorial(len(s)):
#     s1=""
#     while len(s1)<len(s):
#         c=rm.choice(s)
#         if c not in s1:
#             s1+=c
#     if s1 not in l:
#         l.append(s1)
# print(len(l))

# print(l)  
    

# import re
# s="Vcube@gmail.com"
# f="@gmail.com"
# ans=re.search(f,s)
# print(ans)

# n=5
# for i in range(n):
#     print(' ' * (n - i - 1), end='')
#     value = 1
#     for j in range(i + 1):
#         print(value, end=' ')
#         value = value * (i - j) // (j + 1)
#     print()
    
# for i in range(10, 99):
#     for j in range(100, 999):
#         res = i * j
#         if len(str(res))==5:
#             s = [str(res), str(i), str(j)]
#             combined = ''.join(s)
        
#             if len(combined) == len(set(combined)):
#                 print(f' {i} x {j} = {res}')



# class inventoryltem:
#     items=[]
#     def __init__(self,item_id,name,Qty):
#         self.item_it=int(item_id)
#         self.name=name
#         self.qty=int(Qty)
#         inventoryltem.items.append((self.item_it,self.name,self.qty))
        
#     def show_items(self):
#         for i in inventoryltem.items:
#             print(i)
              
#     def restock(self):
#         id=int(input("enter the item id: "))
#         for i in range(len(inventoryltem.items)):
#             if id in inventoryltem.items[i]:
#                 inventoryltem.items.remove(inventoryltem.items[i])
#                 break
    
# item1=inventoryltem(1,"tv",500)
# item2=inventoryltem(2,"dvd",900)
# item3=inventoryltem(3,"Ac",20)
# item4=inventoryltem(4,"shirts",10)
# item5=inventoryltem(5,"dress",6)
# item6=inventoryltem(6,"DFDF",67)
# item1.show_items()
# item1.restock()
# item1.show_items()


# s="Ma12#2hsjdWEBG"
# s2=""
# caps=0
# nums=0
# sml=0
# spl=0
# for i in s:
#     if "A"<=i<="Z":
#         caps+=1                                               #swapcase 
#     elif "a"<=i<="z":
#         sml+=1
#     elif "0"<=i>="9":
#         nums+=1
#     else:
#         spl+=1
        
# print("caps",caps)
# print("small",sml)
# print("nums",nums)
# print("spl",spl)


n=5
i=2
p_cnt=0
while True:
    d=1
    cnt=0
    while d<=i:
        if i%d==0:
            cnt+=1
        d+=1
    if cnt==2:
        p_cnt+=1
    if p_cnt==n:
        print(i)
        break
    i+=1
        
