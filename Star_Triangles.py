


#                THIS PY FILE CONTAIN ONLY DIFFEREFNT PATTERENS OF "*" 
#                ALL THE PYTHON CODE ARE COMMENTED. IF YOU WANT TO RUN AND EXECUTE THE CODE,JUST UNCOMMENT THE CODE. 
#                THE RESPECTIVE OUTPUT WILL BE DISPLAYED AT THE BOTTOM OF THE CODE. CHECK IT ONCE.








# n=int(input("n :"))
# for i in range(n):
#     for j in range(2*n-i-1):
#         if i<=j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n :5
# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * * 
#         * 


# n=5
# l=[]
# for i in range(n): 
#     l.append("  "*i+"* "*(2*(n-i)-1))

# print("\n".join(l))

# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * * 
#         * 

# n=int(input("enter :"))
# for i in range(n): 
#     for j in range(n):
#         print("*",end="")
    
#     print()
#     n-=1


# enter :9
# *********
# ********
# *******
# ******
# *****
# ****
# ***
# **
# *



# n=int(input("n :"))
# val=ord("A")+(n-1)
# for i in range(n):
#     a=val
#     for j in range(n):
#         if i>=j and  i+j<=n-1:
#             if j%2==0:
#                 print("*",end=" ")
#             else: print("@",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#     n :9
# *
# * @
# * @ *
# * @ * @
# * @ * @ *
# * @ * @
# * @ *
# * @
# *


# n=int(input("n :"))
# val=ord("A")+(n-1)
# for i in range(n):
#     a=val
#     for j in range(n):
#         if i>=j and  i+j<=n-1:
#             if i%2==0:
#                 print("*",end=" ")
#             else: print("@",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


#     n :9
# *
# @ @
# * * *
# @ @ @ @
# * * * * *
# @ @ @ @
# * * *
# @ @
# *

# n=5
# val=ord("A")+(n//2)
# for i in range(n):
#     a=val
#     for j in range(n):
#         if j>=i and  j+i<=n-1:
#             print(chr(val),end=" ")
#             val+=n-j-3
#         else:
#             print(" ",end=" ")
#     print()
#     val=a-1



# n=int(input("n :"))
# for i in range(n):
#     for j in range(n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()
#     n-=1
    
#     n :5
#           * 
#         * * * 
#       * * * * * 
#     * * * * * * *                                                                                                 
#   * * * * * * * * * 



# n=int(input("n :"))
# for i in range(n):
#     for j in range(2*n-1):
#         if i+j>=n-1 and j-i<=n-1:
#             print('*',end=' ')
#         else:
#             print(" ",end=" ")
#     print()


#     n :5

#         *
#       * * *       
#     * * * * *     
#   * * * * * * *   
# * * * * * * * * * 

# n=int(input("n :"))
# val=1
# for i in range(n):
#     for j in range(n+i):
#         if i+j>=n-1:
#             print("*",end=' ')
#         else:
#             print(" ",end=" ")
#     print()

#     n :5

#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 

# n=int(input("n :"))
# for i in range(n):
#     for j in range(n):
#         if i>=j and  i+j<=n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n :9
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# n=int(input("n :"))
# for i in range(n):
#     for j in range(n):
#         if i<=j and  i+j>=n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


#     n :9
#                 * 
#               * * 
#             * * * 
#           * * * * 
#         * * * * * 
#           * * * * 
#             * * * 
#               * * 
#                 * 



# n=int(input("n :"))
# for i in range(n):
#     for j in range(n):
#         if j<=i and  j+i>=n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n :9




#         *
#       * * *       
#     * * * * *     
#   * * * * * * *   
# * * * * * * * * * 




# n=int(input("n :"))
# for i in range(n):
#     for j in range(n):
#         if j>=i and  j+i<=n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# n :9
# * * * * * * * * * 
#   * * * * * * *   
#     * * * * *     
#       * * *       
#         *
   

# n=int(input("n :"))
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print("*",end=" ")
#     for j in range(n-i-1):
#         print("*",end=" ")
#     print()


# n :5
#   * * * * * * * * * 
#     * * * * * * * 
#       * * * * * 
#         * * * 
#           * 
 

# n=int(input("n :"))
# for i in range(2*n-2):
#     for j in range(n):
#         if i>=j and i+j<=2*n-2:
#             print("*",end=" ")

#     print()


# n :5
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# n=5
# l=["* "*(i+1) for i in range(n)]
# print("\n".join(l+l[-2::-1]))


# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
 

# n=int(input("n:"))
# for i in range(n):
#     for j in range(n):
#         if i==0 or i+j==n-1 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n:5
# * * * * * 
#       * * 
#     *   * 
#   *     * 
# *       * 



# n=int(input("n:"))
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()

# n:5
#           * 
#         * * * 
#       * * * * * 
#     * * * * * * * 
#   * * * * * * * * * 

# n=5
# for i in  range(n):
#     for j in range(n+n-1):
#         if i+j>=n-1 and j-i<=n-1:
#             print("*",end=" ")
#         else: print(" ",end=" ")
#     print()

#         *
#       * * *       
#     * * * * *     
#   * * * * * * *   
# * * * * * * * * * 

# n=int(input("n:"))
# s="PYSPIDERS"
# for i in range(2*n-1):
#     for j in range(2*n-1):
#         if i==n-1:
#             print(s[j],end=" ")
#         elif (j-i>=1 and i+j<=n+2) or (i+j>=2*n-1 and i-j>=1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# n:5
#   * * * * * * *   
#     * * * * *     
#       * * *       
#         *
# P Y S P I D E R S 
#         *
#       * * *       
#     * * * * *     
#   * * * * * * * 

# n=int(input("n:"))
# s="PYSPIDERS"
# for i in range(2*n-1):
#     for j in range(2*n-1):
#         if i==n-1:
#             print(s[j],end=" ")
#         elif ((i+j>=n-1 and j-i<=n-1) and i<n-1) or (i-j<=n-1 and i+j<=2*n+2 and i>n-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n:5

#         *
#       * * *       
#     * * * * *     
#   * * * * * * *   
# P Y S P I D E R S 
#   * * * * * * *   
#     * * * * *     
#       * * *       
#         *



# n=int(input("n:"))
# t=0
# for i in range(2*n-1):
#     print("  "*(n-t)+" *"*(t+1))   single loop
#     t=t+1 if i<n-1 else t-1
    
# print()

# n:5
#            *
#          * *
#        * * *
#      * * * *
#    * * * * *
#      * * * *
#        * * *
#          * *
#            *


# n=5
# s="PYSPIDERS"
# for i in range(2*n-1):
#     for j in range(2*n-1):
#         if j==n-1:
#             print(s[i],end=" ")
#         elif i+j>=n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
    
        
# n=int(input("enter num :"))
# for i in range(n):
#     for j in range(1,2*n):
#         if j==2*n//2+i or j==2*n//2-i or i==n-1:
#              print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# n=int(input("enter num :"))
# for i in range(n):
#     for j in range(1,2*n):
#         if j==i+1 or j==2*n-i-1 or i==0:
#              print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# class Quadrilateral:
#     def __init__(self,name,height,Base):
#         self.name =name
#         self.height =height
#         self.width =Base
#     def CalculateArea(self,Base,height):
#         Area = Base *height
        
        
# class Trapezoid(Quadrilateral):
#     def CalculateArea(self):
#         print(self.name)
#         print((self.height+self.width)/2*self.height)
    
    
# class Rectangle(Quadrilateral):
#     def CalculateArea(self):
#         print(self.name)
#         print(self.height*self.width)

# t=Trapezoid()



n=5
for i in  range(n):
    for j in range(n+n-1):
        if i+j>=n-1 and j-i<=n-1:
            print("H",end=" ")
        else: print(" ",end=" ")
    print()
for i in range(n+1):
    print("""   H H H H H H                     H H H H H H""")
for i in range(n//2+1):
    print("""       H H H H H H H H H H H H H H H H H H """)
for i in range(n+1):
    print("""   H H H H H H                     H H H H H H""")
for i in  range(n):
    for j in range(n+n-1):
        if i<=j and j+i<=2*n-2: 
            print("H",end=" ")
        else: print(" ",end=" ")
    print()