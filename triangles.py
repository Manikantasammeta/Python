
#                               Alpbhabet Triangle


# n=int(input("n :"))
# val=ord("A")


# for i in range(n):
#     a=val
#     for j in range(n-i):
#         print(chr(val),end=" ")
#         val+=(n-j)
#         if val>ord("Z"): val=ord("A")
#     print()
#     val=a+1
#     if val>ord("Z"): val=ord("A")






# n :5
# A F J M O 
# B G K N 
# C H L 
# D I 
# E 


# n=int(input("n :"))
# val=ord("A")+(n-1)
# for i in range(n):
#     a=val
#     for j in range(n-i):
#         print(chr(val),end=" ")
#         val+=(n-j-1)
#     print()
#     val=a-1


# n :5
# E I L N O 
# D H K M 
# C G J 
# B F 
# A 


# n=int(input("n :"))
# val=ord("A")+(n-1)
# for i in range(n):
#     a=val
#     for j in range(n):
#         if i>=j and  i+j<=n-1:
#             print(chr(val),end=" ")
#             val+=n-j-1
#             while val>ord("Z"):
#                 val=ord("A")
#         else:
#             print(" ",end=" ")
   
#     print()
#     val=a-1
#     while val>ord("Z"):
#         val=ord("A")


# n :5
# E
# D H       
# C G J     
# B F       
# A

# n=int(input("n :"))
# val=ord("A")
# for i in range(n):
#     a=val
#     for j in range(n):
#         if i+j>=n-1:
#             print(chr(val),end=" ")
#             val-=1
#             if val<ord("A"):
#                 val=ord("Z") 
#         else:
#             print(" ",end=" ")
#     print()
#     val=a+i+2
#     while val>ord("Z"):
#         val-=26

# n :5
#         A 
#       C B 
#     F E D 
#   J I H G 
# O N M L K 

# n=int(input("n:"))

# for i in range(n):
#     val=ord("A")
#     for j in range(i+1):
#         print(chr(val),end="")
#         val+=1
#     print()

#     n:5
# A
# AB
# ABC
# ABCD
# ABCDE


 
# n=int(input("n:"))

# for i in range(n):
#     val=ord("A")
#     for j in range(n):
#         print(chr(val),end="")
#         val+=1
#     print()
#     n-=1


#     n:5
# ABCDE
# ABCD
# ABC
# AB
# A


# n=int(input("enter :"))
# val=ord("A")
# for i in range(n):
#   for j in range(n):
#     print(chr(val),end="")
#     if val>ord("Z"):
#       val=ord("A")
#   val+=1
#   n-=1
#   print()

#   enter :9
# AAAAAAAAA
# BBBBBBBB
# CCCCCCC
# DDDDDD
# EEEEE
# FFFF
# GGG
# HH
# I

# n=int(input("enter :"))
# val=ord("A")
# val1=ord("b")
# for i in range(n):
#   for j in range(n):
#     if j%2==0:
#         print(chr(val),end="  ")
#     else:
#         print(chr(val1),end="  ")
#         val+=2
#         val1+=2
#     if val>ord("Z"):
#       val=ord("A")
#     if val1>ord("z"):
#       val1=ord("a")
#   n-=1
#   print()

# n=int(input("enter :"))
# val=ord("A")
# for i in range(n):
#   for j in range(n):
#     print(chr(val),end="")
#     val+=1
#     if val>ord("Z"):
#       val=ord("A")
#   n-=1
#   print()

# enter :9
# ABCDEFGHI
# JKLMNOPQ
# RSTUVWX
# YZABCD
# EFGHI
# JKLM
# NOP
# QR
# S

# n=int(input("enter :"))

# for i in range(n):
#   val=ord("A")
#   for j in range(i):
#     print(chr(val),end="")
#     val+=1
    
#   print()


# A
# AB
# ABC
# ABCD
# ABCDE
# ABCDEF
# ABCDEFG
# ABCDEFGH


#   enter :7
# A  b  C  d  E  f  G  
# G  h  I  j  K  l  
# M  n  O  p  Q  
# Q  r  S  t  
# U  v  W  
# W  x  
# Y 


# n=int(input("n:"))
# val=ord("A")
# for i in range(n):
#     a=val
#     for j in range(n+i):
#         if i+j>=n-1:
#             print(chr(val),end=" ")
#             val-=1
#         else:
#             print(" ",end=" ")
#     print()
#     val=a+(2*i+3)


#     output-->

#     n:5
#         A 
#       D C B 
#     I H G F E 
#   P O N M L K J 
# Y X W V U T S R Q 




# n=int(input("n:"))
# val=ord("A")
# a=val 
# for i in range(n):
#     for j in range(n+i):
#         if i+j>=n-1:
#             print(chr(val),end=" ")
#             val-=1
#         else:
#             print(" ",end=" ")
#     print()
#     val=a+(2*i+2)


# n:5
#         A 
#       C B A 
#     E D C B A 
#   G F E D C B A 
# I H G F E D C B A 

# n=int(input("n:"))
# for i in range(n):
#     val=ord("A")
#     v1=1
#     a=True
#     for j in range(n+i):
#         if i+j>=n-1:
#             if a:
#                 print(v1,end=" ")
#                 v1=v1+1 if j<n-1 else v1-1
#             else:
#                 print(chr(val),end=" ")
#                 val=val+1 if j<n-1 else val-1
#                 if j==n-1 and not(a): v1-=1
#                 elif j==n-1 and a: val-=1
#             a=not(a)
#         else:
#             print(" ",end=" ")
#     print()

# n:5
#         1 
#       1 A 1 
#     1 A 2 B 1 
#   1 A 2 B 2 A 1 
# 1 A 2 B 3 C 2 B 1


# n=int(input("n:"))
# for i in range(n):
#     v=1
#     for j in range(n+i):
#         if i+j>=n-1:
#             print(v,end=" ")
#             v=v+1 if j<n-1 else v-1
#         else:
#             print(" ",end=" ")
#     print()

# n:5
#         1 
#       1 2 1 
#     1 2 3 2 1 
#   1 2 3 4 3 2 1 
# 1 2 3 4 5 4 3 2 1

# n=int(input("n:"))
# for i in range(n):
#     v=ord("A")
#     for j in range(n+i):
#         if i+j>=n-1:
#             print(chr(v),end=" ")
#             v=v+1 if j<n-1 else v-1
#         else:
#             print(" ",end=" ")
#     print()


# n:5
#         A 
#       A B A 
#     A B C B A 
#   A B C D C B A 
# A B C D E D C B A

# n=int(input("n:"))
# for i in range(n):
#     val=ord("A")
#     v1=1
#     a=True
#     for j in range(n+i):
#         if i+j>=n-1:
#             if a:
#                 print(v1,end=" ") 
#                 v1=v1+1 if j<n-1 else v1-1     
#             else:
#                 print(chr(val),end=" ")
#                 val=val+1 if j<n-1 else val-1
                
#             a=not(a)
#             if j==n-1 and not(a): val-=1
#             elif j==n-1 and a: v1-=1
#         else:
#             print(" ",end=" ")
#     print()
# n:9
#                 1 
#               1 A 1 
#             1 A 2 A 1 
#           1 A 2 B 2 A 1 
#         1 A 2 B 3 B 2 A 1 
#       1 A 2 B 3 C 3 B 2 A 1 
#     1 A 2 B 3 C 4 C 3 B 2 A 1 
#   1 A 2 B 3 C 4 D 4 C 3 B 2 A 1 
# 1 A 2 B 3 C 4 D 5 D 4 C 3 B 2 A 1


# n=int(input("n:"))
# for i in range(n):
#     val=ord("A")
#     v1=1
#     a=True
#     for j in range((n*2)-1-i):
#         if j>=i:
#             if a:
#                 print(v1,end=" ")
#                 v1=v1+1 if j<n-1 else v1-1
#             else:
#                 print(chr(val),end=" ")
#                 val=val+1 if j<n-1 else val-1
#             a=not(a)
#             if j==n-1 and a: v1=v1-1
#             elif j==n-1 and not(a): val=val-1
#         else:
#             print(" ",end=" ")
#     print()

# n:9
# 1 A 2 B 3 C 4 D 5 D 4 C 3 B 2 A 1 
#   1 A 2 B 3 C 4 D 4 C 3 B 2 A 1 
#     1 A 2 B 3 C 4 C 3 B 2 A 1 
#       1 A 2 B 3 C 3 B 2 A 1 
#         1 A 2 B 3 B 2 A 1 
#           1 A 2 B 2 A 1 
#             1 A 2 A 1 
#               1 A 1 
#                 1 



# n=int(input("n:"))
# m=int(input("m:"))
# if m>9:
#     a=9
# else:
#     a=m
# val=ord("A")
# for i in range(n):
#     for j in range(m):
#         if i%2==0:
#             print(chr(val),end=" ")
#             val+=1  
#             if val>ord("Z"):
#                 val=ord("A")
#         else:
#             print(a,end=" ")
#             a-=1
#             if a<1:
#                 a=9
#     print()

# n:9
# m:10
# A B C D E F G H I J 
# 9 8 7 6 5 4 3 2 1 9 
# K L M N O P Q R S T 
# 8 7 6 5 4 3 2 1 9 8 
# U V W X Y Z A B C D 
# 7 6 5 4 3 2 1 9 8 7 
# E F G H I J K L M N 
# 6 5 4 3 2 1 9 8 7 6 
# O P Q R S T U V W X


# n=5
# val=ord("A")
# v1=1
# t=0
# a=True
# for i in range(n*2-1-t):
#     for j in range(n):
#         if i>=j and i+j<=2*n-2:
#             if i%2==0:
#                 print(v1 if a else chr(val),end=" ")
#                 v1=v1+1 if j<n-1 else v1-1
#             else:
#                 print(chr(val) if not(a) else v1,end=" ")
#                 val=val+1 if j<n-1 else val-1
#             a=not(a)
#             if j==n-4 and a: v1=v1-1
#             elif j==n-4 and not(a):val=val-1
#         else:
#             print(" ",end=" ")
#     print()
#     t+=1



i=1
while i<=10:
    if i==5:
        continue
    print(i)
    i+=1