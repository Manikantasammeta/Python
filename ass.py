#1. l=[3,5,8,7,11,4,9,10,2,1]

# for i in range(len(l)-1):
#     for j in range(i+1,len(l)):       #sorting the list with out useing built-Functions
#         if l[i]>l[j]:                 #it is also know as Bubble Sort
#             l[i],l[j]=l[j],l[i]
# print(l)
# ot-->[1, 2, 3, 4, 5, 7, 8, 9, 10, 11]

# 2.Reversing the elements in list

# l=[11,21,31,41,51]
# l1=[]
# for i in l:
#     k=str(i)
#     k=k[::-1]
#     m=int(k)
#     l1.append(m)
# print(l)                       
# print(l1)


# ot-->[11, 21, 31, 41, 51]
#      [11, 12, 13, 14, 15]


# 3.Finding the elements between given two elements and print elements in list
#find the length of the list

#      list=[1,5,2,6,9,10,51,78,32,86,7,23,56,72,55]

#     enter 1st num:5
#     enter 2nd num:78
#     elements:[2, 6, 9, 10, 51]
#      length:5


#4. Recursion function
#Trace the Program and write the output


# def fun(n):
#     print(n,end='')
#     if n>0:
#         fun(n-1)
#         print(n,end='')
        
# fun(5)
#54321012345

# 5.write the python logic for given patteren

# n=int(input("n:"))
# val=ord("A")+n-1
# t=True
# for i in range(n):
#     a=val
#     for j in range(n):
#         if t:
#             print(chr(val),end=" ")
#             val-=1
#             if val>ord("Z"):
#                 val=ord("A")
#         else:
#             print(chr(val+32),end=" ")
#             val-=1
#             if val>ord("Z"):
#                 val=ord("A")
#         t=not(t)

#     print()
#     val=a+n
#     if val>ord("Z"):
#             val=ord("A")

#     n:5
# E d C b A 
# j I h G f 
# O n M l K 
# t S r Q p     
# Y x W v U 


#6.Convert 2 lists into a dictionary
