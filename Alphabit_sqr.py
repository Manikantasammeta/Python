


#                                  PATTEREN PROBLEMS
#                ALL THE PYTHON CODE ARE COMMENTED. IF YOU WANT TO RUN AND EXECUTE THE CODE,JUST UNCOMMENT THE CODE. 
#                THE RESPECTIVE OUTPUT WILL BE DISPLAYED AT THE BOTTOM OF THE CODE. CHECK IT ONCE.


# n=int(input("enter :"))
# val=ord("Z")
# val1=ord("y") 
# for i in range(n):
#   for j in range(n):
#     if j%2==0:
#      print(chr(val),end="   ")
#     else:
#         print(chr(val1),end="   ")
#         val1-=2
#         val-=2
#     if val<ord("A"):
#         val=ord("Z")
#     if val1<ord("a"):
#         val1=ord("y")
        
#   print()


# n:9
# A   a   Z   y   X   w   V   u   T   
# T   s   R   q   P   o   N   m   L   
# L   k   J   i   H   g   F   e   D   
# D   c   B   a   Z   y   X   w   V   
# V   u   T   s   R   q   P   o   N   
# N   m   L   k   J   i   H   g   F   
# F   e   D   c   B   a   Z   y   X   
# X   w   V   u   T   s   R   q   P   
# P   o   N   m   L   k   J   i   H 

# n=int(input("n :"))
# val=ord("A")
# for i in range(n):
#     for j in range(n):
#         print(chr(val),end=" ")
#         val+=1
#         if val>ord("Z"): val=ord("A")
#     val-=4
#     print()


#     n :5

# A B C D E 
# B C D E F 
# C D E F G 
# D E F G H 
# E F G H I 


# n=int(input("n :"))
# val=ord("A")
# for i in range(n):
#     for j in range(n):
#         if i==n//2 or j==n//2:
#             print(chr(val),end=" ")
        
#         else:
#             print(" ",end=" ")
#         val+=1
#         if val>ord("Z"): val=ord("A")
#     print()
# n :5

#     C     
#     H     
# K L M N O 
#     R     
#     W  



# n=int(input("n :"))
# v=ord("A")
# v1=ord("a")
# for i in range(n):
#     for j in range(n):
#         if j==n//2:
#             print(chr(v),end=" ")
#             v+=1
#             if i==j:
#                 v1+=1
#         elif i==n//2:
#             print(chr(v1),end=" ")
#             v1+=1
#         elif i==0 or j==0 or i==n-1 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()



#     n :5
# * * A * *
# *   B   *
# a b C d e
# *   D   *
# * * E * *

# n=int(input("n :"))
# v=ord("A")
# v2=ord("a")
# for i in range(n):
#     for j in range(n):
#         if j==n//2:
#             print(chr(v),end=" ")
#             v+=1
#             if i==j:
#                 v2+=1
#         elif i==n//2:
#             print(chr(v2),end=" ")
#             v2+=1
#         elif 
#     print()


# n=int(input("n :"))
# for i in range(n):
#     for j in range(n):
#         if i+j==0:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=int(input("n:"))
# val=ord("E")
# val1=ord("E")
# for i in range(n):
#     a=val
#     for j in range(n):
#         if i==0 or j==0 or i==n-1 or j==n-1:
#             print("*",end=" ")
#         elif i==n//2:
#             print(chr(val+j),end=" ")

        
#         elif j==n//2:
#             print(chr(val1+i),end=" ")
        
#         else:
#             print(" ",end=" ")
#     print()

# n:5
# * * * * * 
# *   F   * 
# * F G H * 
# *   H   * 
# * * * * *
    

# n=int(input("n :"))
# val=ord("A")
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print(chr(val),end=" ")
    
#         elif i+j==n-1:
#             print(chr(val+n),end=" ")
#         else:
#             print(" ",end=" ")

        
#     print()
#     val+=1



#     n :5

# A       F 
#   B   G   
#     C     
#   I   D   
# J       E


    


# n=int(input("n :"))
# val=ord("A")
# for i in range(n):
#     a=val
#     for j in range(n):
#         if i%2==0:
#             print(chr(val),end=" ")
#             val+=1
#             if val>ord("Z"):
#                 val=ord("A")
#         else:
#             print(chr(val+n-1),end=" ")
#             val-=1
#     print()
#     val=a+n
#     if val>ord("Z"):
#         val=ord("A")


# n :5 
# A B C D E 
# J I H G F 
# K L M N O 
# T S R Q P 
# U V W X Y 


    

# n=int(input("n :"))
# val=ord("A")
# a=False
# for i in range(n):
#     for j in range(n):
#         if a:
#             print(chr(val),end=" ")
#             a=False
#         else:
#             print(chr(val+32),end=" ")
#             a=True
#         val+=1
#         if val>ord("Z"):
#             val=ord("A")
#     print()


#         a=True
# n :5
# A b C d E 
# f G h I j 
# K l M n O 
# p Q r S t 
# U v W x Y 

#   a=False
# n :5
# a B c D e 
# F g H i J 
# k L m N o 
# P q R s T 
# u V w X y 


# n=int(input("n :"))
# val=ord("A")
# t=True
# for i in range(n):
#     x=val
#     for j in range(n):
#         if i%2==0:
#             if t:
#                 print(chr(val),end=" ").  
#             else:
#                 print(chr(val+32),end=" ")
#         else:
#             if not(t):
#                 print(chr(val),end=" ")
#             else:
#                 print(chr(val+32),end=" ")
#         t=not(t)
#         val= val+n
#         while val>ord("Z"):
#             val=val-26
#     val=x+1 
#     print()
#     if val>ord("Z"):
#             val=ord("A")

# n :6
# A g M s Y e 
# b H n T z F 
# C i O u A g 
# d J p V b H 
# E k Q w C i 
# f L r X d J    
     


# n=int(input("n :"))
# val=ord("A")+n-1
# t=True
# for i in range(n):
#     x=val
#     for j in range(n):

#         if t:
#             print(chr(val),end=" ")
#         else:
#             print(chr(val+32),end=" ")
#         t=not(t)
#         val= val-1
#         while val>ord("Z"):
#             val=val-26
#     val=x+n
#     print()
#     if val>ord("Z"):
#             val=ord("A")



# n :5
# E d C b A 
# j I h G f 
# O n M l K 
# t S r Q p 
# Y x W v U 


# n=int(input("n:"))
# val=ord("A")
# val1=1
# for i in range(n):
#     for j in range(n):
#         if i%2==0:
#             print(val1,end=" ")
#             val1+=1
#             while val1>9:
#                 val1=1
#         else:
#             print(chr(val),end=" ")
#             val+=1
#             while val>ord("Z"):
#                 val=ord("A")
#     print()
#     val=ord("A")
#     val1=1


# n:27
# 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A 
# 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A 
# 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A 
# 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A 
# 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A 
# 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A 
# 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A 
# 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
# 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
# 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
# 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
# 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
# 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
# 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9


# n=int(input(" n:"))
# v=ord("A")
# v1=v
# for i in range(n):
#     for j in range(n):
#         if j==n//2 or i==j or i+j==n-1:
#             print(chr(v),end=" ")
#             if i==n//2 and i==j:
#                 v1-=1
#         elif i==n//2:
#             print(chr(v1),end=" ")
#             v1= v1+1 if j<n//2 else v1-1
#         else:
#             print(" ",end=" ")
#     print()
#     v=v+1 if i<n//2 else v-1

#     n:5
# A   A   A 
#   B B B   
# A B C B A 
#   B B B   
# A   A   A 


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

# n=int(input("n :"))
# if n>26:
#     val=ord("Z")
# else: val=ord("A")+n-1
# for i in range(n):
#     a=val
    
#     for j in range(n):
#         if i%2==0:
#             print(chr(val),end=" ")
#             val-=1
#             if val<ord("A"):
#                 val=ord("Z")
#         else:
#             print(chr(val),end=" ")
#             val+=1
#             if val>ord("Z"):
#                 val=ord("A")
            
#     print()
#     val=a+( n*2)-1 if i%2!=0 else a+1
#     if val>ord("Z"):
#         val=ord("A")
#     if val<ord("A"):val=ord("Z")

# n :9
# I H G F E D C B A 
# J K L M N O P Q R 
# A Z Y X W V U T S 
# B C D E F G H I J 
# S R Q P O N M L K 
# T U V W X Y Z A B 
# A Z Y X W V U T S 
# B C D E F G H I J 
# S R Q P O N M L K 


# n=int(input("n:"))
# for i in range(n):
#     for j in range(n):
#         if i%2==0:
#             if j%2==0:
#              print("0",end=" ")
#             else:
#                   print("1",end=" ")
#         else:
#             if j%2==1:
#              print("0",end=" ")
#             else:
#                   print("1",end=" ")

#     print()
# n:7
# 0 1 0 1 0 1 0 
# 1 0 1 0 1 0 1 
# 0 1 0 1 0 1 0 
# 1 0 1 0 1 0 1 
# 0 1 0 1 0 1 0 
# 1 0 1 0 1 0 1 
# 0 1 0 1 0 1 0 

# n=int(input("n:"))
# val=ord("A")+n-1
# t=True
# for i in range(n):
#     a=val
#     for j in range(n):
#         if i%2==0:
#             print(chr(val) if t==True else chr(val+32),end=" ")
#             val-=1
#         else:
#             print(chr(val) if t==True else chr(val+32),end=" ")
#             val+=1
#         t=not(t)
#     print()
#     val=a+n*2-1 if i%2!=0 else a+1

#     n:5
# E d C b A 
# f G h I j 
# O n M l K 
# p Q r S t 
# Y x W v U



# n=int(input("n:"))
# t=1
# if n>26:
#     val=ord("Z")
# else: val=ord("A")+n-1
# for i in range(n):
#     a=val
#     for j in range(n):
#         print(chr(val),end=" ")
#         val=val+(2*i+1) if j%2==0 else val+(2*n)-(1+2*i)
#         while val>ord("Z"):
#             val-=26
#     print()
#     t+=1
#     val=a-1
#     if val>ord("Z"):
#         val=ord("A")

# n:9
# I J A B S T K L C 
# H K Z C R U J M B 
# G L Y D Q V I N A 
# F M X E P W H O Z 
# E N W F O X G P Y 
# D O V G N Y F Q X 
# C P U H M Z E R W 
# B Q T I L A D S V 
# A R S J K B C T U 

# n=int(input("n:"))
# t=True
# if n>26:
#     val=ord("Z")
# else: val=ord("A")+n-1
# for i in range(n):
#     a=val 
#     for j in range(n):
#         if i%2==0:
#             print(chr(val) if t else chr(val+32),end=" ")
#             val=val+(2*i+1) if j%2==0 else val+(2*n)-(1+2*i)
#             while val>ord("Z"):
#                 val-=26
#         else:
#             print(chr(val) if not(t) else chr(val+32),end=" ")
#             val=val+(2*i+1) if j%2==0 else val+(2*n)-(1+2*i)
#             while val>ord("Z"):
#                 val-=26
#         t=not(t)
#     print()
#     val=a-1
#     if val>ord("Z"):
#         val=ord("A") 

# n:8
# H i X y N o D e 
# g J w Z m P c F 
# F k V a L q B g 
# e L u B k R a H 
# D m T c J s Z i 
# c N s D i T y J 
# B o R e H u X k 
# a P q F g V w L


# n=int(input("n:"))
# m=int(input("m:"))
# if m>9:
#     a=9
# else:
#     a=m
# if n>26:
#     val=ord("Z")
# else: val=ord("A")+n
# for i in range(n):
#     t=val
#     for j in range(m):
#         if i%2==0:
#             print(chr(val),end=" ")
#             val-=1  
#             if val<ord("A"):
#                 val=ord("Z")
#         else:
#             print(a,end=" ")
#             a-=1
#             if a<1:
#                 a=9
#     print()
#     val=t

# n:7
# m:9
# H G F E D C B A Z 
# 9 8 7 6 5 4 3 2 1 
# H G F E D C B A Z 
# 9 8 7 6 5 4 3 2 1 
# H G F E D C B A Z 
# 9 8 7 6 5 4 3 2 1 
# H G F E D C B A Z 

# n=int(input("n:"))
# val=ord("A")+n//2
# v1=val
# for i in range(n):
#     for j in range(n):
#         if i==j or i+j==n-1 or j==n//2:
#             print(chr(val),end=" ")
#             if i==n//2 and i==j:
#                 v1+=1
#         elif i==n//2:
#             print(chr(v1),end=" ")
#             v1=v1-1 if j<n//2 else v1+1
#         else:
#             print(" ",end=" ")
#     print()
#     val=val-1 if i<n//2 else val+1
# n:5
# C   C   C 
#   B B B   
# C B A B C 
#   B B B   
# C   C   C 

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


#         A 
#       B F 
#     C G J 
#   D H K M 
# E I L N O 

# n=int(input("n:"))
# val=ord("A")+(n-1)
# m=n
# for i in range(n):
#     a=val
#     for j in range(i+1):
#             if i%2==0:
#                 print(chr(val),end=" ")
#             else:
#                 print(m,end=" ")    
#     print()
#     if i%2==0:
#         val-=1
#     else:
#         m-=1

# n:5
# E 
# 5 5 
# D D D 
# 4 4 4 4 
# C C C C C 