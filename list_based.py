


#                ALL THE PYTHON CODE ARE COMMENTED. IF YOU WANT TO RUN AND EXECUTE THE CODE,JUST UNCOMMENT THE CODE. 
#                THE RESPECTIVE OUTPUT WILL BE DISPLAYED AT THE BOTTOM OF THE CODE. CHECK IT ONCE.




# import random as rm

# class list:
#     def li(self,m):
#        l=[rm.randint(1,100) for i in range(m)]
#        print(l)


# l=list()
# l.li(5)

# ot-->[5, 13, 44, 4, 51]
#                                                    random elements by tackingthe user input


# import random as re
# class list:
#     def li(self,n):
        
#         self.l=[int(input("enter element:")) for i in range(n)]
#         return  self.l

#                                                             sum of list by tacking user input    
#     def summ(self):
#         s=0
#         for i in self.l:
#             s=s+i
#         return s

# k=list()
# print(k.li(5))
# print(k.summ())



# i=[5,4,3,2,1]
# l=[i[j] for j in range(len(i)-1,-1,-1)]
# print(l)
#                                          reversing the list with out sliceing and built in methods
# ot-->[1, 2, 3, 4, 5]


#   2nd method
# i=[5,4,3,2,1]
# l1=[]
# for j in i:
#     l1=[j]+l1
# print(l1)

# ot-->[1, 2, 3, 4, 5]


# l=[11,21,31,41,51]
# l1=[]
# for i in l:
#     k=str(i)
#     k=k[::-1]
#     m=int(k)
#     l1.append(m)
# print(l)                              # reversing the elements in list
# print(l1)
# ot-->[11, 21, 31, 41, 51]
#      [11, 12, 13, 14, 15]



# class list:
#     def li(self,n):
#         self.n=n
#         l1=[]
#         while n-1>0:
#             for i in range(2,n):
#                 if n%i==0:                     
#                     break                                 
#             else:                              #list of prime numbers of given
#                 l1.insert(0,n)
#             n=n-1
#         return l1

# k=list()
# print(k.li(int(input("enter range:"))))

# ot-->enter range:5
#          [2, 3, 5]


# import random as rm
# n=int(input("enter the range"))
# l=[rm.randint(1,100) for i in range(n)]
# print(l)
# def fun(l,k=l[0],j=l[0]):
#     for i in l:
#         if i>k:                                        #finding max number in list min number
#             k=i
#         if i<j:
#             j=i
#     return f"max-->{k}\nmin-->{j}"
# print(fun(l))



# l=[34,7,4,5]
# k=l[0]
# o=0                                                            #finding min number in list
# for i in l:
#     if i<k:
#         o=i
# print(i)

# ot-->5

# l=[10,1,3,2,2,2,2,2,1,1,1,1,5,7]
# mx=0
# ele=0
# for i in set(l):
#     c=0
#     for j in range(len(l)-1):
#         if l[j]==l[j+1]==i:                             # finding the element present in more times in the list 
#             c+=1
#     if mx<c:
#         ele=i
#         mx=c
# print(ele,mx)

# ot--> 2 4

# l=[1,1,2,2,3,3,3,3,4,4,5,2,2,3,4]
# mx=0
# ele=0
# i=0
# while i<len(l)-1:
#     for j in range(i+1,len(l)):
#         if l[i]!=l[j]:
#             if mx<len(l[i:j]):
#                 mx=len(l[i:j])                        #finding the element repeted more times in list
#                 ele=l[i]
#                 break
#     i=j
# print(ele,mx)

# ot-->3 4


# l=[3,5,8,7,11,4,9,10,2,1]
# for i in range(len(l)-1):
#     for j in range(i+1,len(l)):                               #sorting the list with out useing built-inmethods
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)
# ot-->[1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
 
# l=[30,"py",50,80,30,"jy",20,90,60,"Qy",10]
# for i in range(len(l)-1):
#     if type(l[i])!=str:                                       #sorting only integers in list
#         for j in range(i+1,len(l)):
#             if type(l[j])!=str:
#                 if l[i]>l[j]:
#                     l[i],l[j]=l[j],l[i]
# print(l)
        
# ot-->[10, 'py', 20, 30, 30, 'jy', 50, 60, 80, 'Qy', 90]



# l=[30,"py",50,80,30,"jy",20,90,60,"Qy",10]
# for i in range(len(l)-1):                                      #sorting both integers and strings integers in list
#         for j in range(i+1,len(l)):
#                 if type(l[i])==type(l[j]):
#                     if l[i]>l[j]:
#                         l[i],l[j]=l[j],l[i]
# print(l)

# # ot-->[10, 'Qy', 20, 30, 30, 'jy', 50, 60, 80, 'py', 90]

# l=[30,"py",50,80,30,"jy",20,90,60,"Qy",10]
# for i in range(len(l)-1):
#     if type(l[i])!=int:                                       #sorting only strings in list
#         for j in range(i+1,len(l)):
#             if type(l[j])!=int:
#                 if l[i]>l[j]:
#                     l[i],l[j]=l[j],l[i]
# print(l)
# ot-->[30, 'Qy', 50, 80, 30, 'jy', 20, 90, 60, 'py', 10]



# l=[30,"Py",50,80,30,"Jy",20,90,60,"Qy",10]
# for i in range(len(l)-1):                                       #sorting only strings in list
#         for j in range(i+1,len(l)):
#             if type(l[i])==type(l[j]):
#                 if l[i]>l[j]:
#                     l[i],l[j]=l[j],l[i]
# print(l)



# l=[30,"py",50,80,30,"jy",20,90,60,"Qy",10]
# l1=[]
# l2=[]
# for i in l:
#       if type(i)==str:
#         l1.append(i)
#     elif type(i)==int:
        # l2.append(i)                                          # sorting both integers and strings
# l1.sort(),l2.sort()
# l3=l2+l1
# print(l3)

# ot-->[10, 20, 30, 30, 50, 60, 80, 90, 'Qy', 'jy', 'py']



# l=[1,2,3,[4,5],6,[7,8],9,10]
# l1=[]
# for i in l:
#         if type(i)==int:
#                 l1.append(i)                                  #converting the nested list into list
#         elif type(i)==list:
#                 for h in i:
#                         l1.append(h)
# print(l1)
        
# ot-->[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



# l=[1,2,3,(4,5),6,[7,8],9,{10,11},12]
# l1=[]
# for i in l:
#         if type(i)==int:
                # l1.append(i)                                         #convering nested list into list
#         elif type(i)==tuple or type(i)==list or type(i)==set:
#                 for h in i:
#                         l1.append(h)
# print(l1)


# ot-->[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# l=[1,2,3,{6,7}]
# l1=[4,5,6,(9,5)]
# print(l+l1)
# print(type(l1[3]))


# l=[1,2,3,4,5,6,7,8,9,0,10]
# l1=[]
# n=int(input("n:"))
# for i in range(0,len(l),n):					#converting the single list to multidimunsional list
# 	l1.append(l[i:i+n])		
# print(l1)
# print(l)

# ot-->[[1, 2], [3, 4], [5, 6], [7, 8], [9, 0], [10]]




# print(eval("["+"[1,[2,[3],4],5,6,[7,[8],[9],10]]".replace("[","").replace("]","")+"]"))

# ot-->[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    								   #converting multi dimensional list into single list



# l=[1,[2,[3],4],5,6,[7,[8],[9],10]]
# l1=[]
# def fun(l):
# 	for i in l:
#             if type(i)!=list:
#                     l1.append(i)													 #with out useing bulit-in methods
#             else:
#                  fun(i)

# fun(l)
# print(l1)


# ot-->[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



# l=["MANIREDDY"]
# l1=[]								#converting the string into list
# for i in l:
# 	for j in range(len(i)):
# 		l1.append(i[:j+1])
# print(l1)

# ot-->['M', 'MA', 'MAN', 'MANI', 'MANIR', 'MANIRE', 'MANIRED', 'MANIREDD', 'MANIREDDY']



# l=[1,2,3,4,2,9,3,4,9,5,3,5,4,1,3,2]
# l1=[]
# for i in range(len(l)-1):
#     for j in range(i+1,len(l)):                                  #second maximum value in list
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# for k in l:
#     if k not in l1:
#         l1.append(k)
# print(l1[-2])

# ot-->5

# l=[1,2,3,4,5]
# l1=[3,6,7,8]                                          /# common element in 2 llists
# for i in l:
#     for j in l1:
#         if i==j:
#             print("the common-->",i)
# ot->the common--> 3

# st=input("Enter str1:").upper()
# st1=input("Enter str2:").upper()
# n=int(input("Enter the range:"))
# l=[]
# for i in range(1,n+1):                                    #creating an list by tacking range and elements from user 
#     s=st+str(i)
#     s1=st1+str(i)
#     l.append(s)
#     l.append(s1)
# print(l)

# ot-->['P1', 'Q1', 'P2', 'Q2', 'P3', 'Q3', 'P4', 'Q4', 'P5', 'Q5', 'P6', 'Q6', 'P7', 'Q7', 'P8', 'Q8', 'P9', 'Q9', 'P10', 'Q10']


# def fun(n,f=1):
#         if n>1:
#           return fun(n-1,f*n)    
#         return f
# print(fun(5))


# n=int(input("n :"))
# l=[]
# for i in range(n):
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
# class solution: 
#         def __init__(self,n,l):
#                 self.n=n
#                 self.l=l
#         def ans(self):
#                 self.iint=0
#                 self.str=0
#                 self.com=0
#                 self.flt=0
#                 for i in self.l:
#                         if type(i)==int:
#                                 self.iint=i+self.iint
#                         elif type(i)==str:
#                                 self.str+=1
#                         if type(i)==complex:
#                                 self.com+=1
#                         if type(i)==float:
#                                 self.flt=i+self.flt
#                 print("str-->",self.str)
#                 print("int-->",self.iint)
#                 print("flt-->",self.flt)
#                 print("com-->",self.com)      

# s=solution(n,l)
# s.ans()


# str--> 1
# int--> 1
# flt--> 1.5
# com--> 1


# l=[1,11,21,2,12,21,3,13,31,4,14,41,5,15,51,6,16,61,7,17,71,8,18,81,9,19,91]
# l1=[]
# l2=[]
# l3=[]
# for i in range(0,len(l)-1,3):
#         l1.append(l[i])
# for j in range(1,len(l)-2,3):                                       #arranging the elements in different lists useing 3 loops
#         l2.append(l[j])
# for k in range(2,len(l)-3,3):
#         l3.append(l[k])
        
# print(f"l1-->{l1}\nl2-->{l2}\nl3-->{l3}")   

# ot-->l1-->[1, 2, 3, 4, 5, 6, 7, 8, 9]
# l2-->[11, 12, 13, 14, 15, 16, 17, 18]
# l3-->[21, 21, 31, 41, 51, 61, 71, 81]




# l=[1,11,21,2,12,21,3,13,31,4,14,41,5,15,51,6,16,61,7,17,71,8,18,81,9,19,91]
# l1=[]
# l2=[]
# l3=[]

# for i in range(len(l)): 
#         if i%2==0:
#                 l1.append(l[i])
#         else:
#                 l2.append(l[i])
# print(f"l1--{l1}\nl2-->{l2}")





# import random as rm

# n=int(input("enter the range:"))
# l=[rm.randint(1,100) for i in range(n)]

# def list(l):                                                  # checking prime numbers in a given range of list
#         l1=[]                                                 #  useing random method
#         for i in l:
#                 for j in range(2,i):
#                         if i%j==0:
#                                 break
#                 else:
#                     if i!=1:
#                         l1.append(i)
#         return l1
# print(l)
# print(list(l))

# ot--> enter the range:15
# [16, 83, 17, 3, 50, 3, 13, 89, 5, 42, 22, 83, 56, 42, 54]
# [83, 17, 3, 3, 13, 89, 5, 83]
 
 
 
 
# l=[1,11,21,2,12,21,3,13,31,4,14]
# l2=[]
# l3=[]
# l4=[]
# k=0
# for i in l:
#     if k==0:
#             l2.append(i)                                                           #useing single loop
#     elif k==1:
#         l3.append(i)
#     elif k==2:
#         l4.append(i)
#     k+=1
#     if k>2:
#         k=0
# print(f"l1:{l2}\nl2:{l3}\nl3:{l4}")

# # ot-->l1:[1, 2, 3, 4, 5, 6, 7, 8, 9]
# #     l2[11, 12, 13, 14, 15, 16, 17, 18, 19]
# #     l3[21, 21, 31, 41, 51, 61, 71, 81, 91]

 
      
 
# l=[1,2,3,3,2,1,4,5,5,6,7,8,9,6,7,8,4,3]
# l1=[]                                      #eleminateing the duplicate elements in list with out useing type casting
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)

# ot-->[1, 2, 3, 4, 5, 6, 7, 8, 9]



# import random as rm
# n=int(input("enter the range:"))
# l=[]
# while len(l)<n:
#         c=rm.randint(1,100)                   #saperating even and odd in a list
#         if c not in l:
#                 l.append(c)
# l1=[]
# l2=[]
# for i in l:
#         if i%2==0:
#                 l1.append(i)
#         else:
#                 l2.append(i)
# print(l)
# print(f"even:{l1}\nodd:{l2}")

# enter the range:20
# [32, 63, 97, 42, 8, 31, 87, 20, 56, 28, 61, 46, 55, 83, 58, 26, 90, 10, 7, 82]
# even:[32, 42, 8, 20, 56, 28, 46, 58, 26, 90, 10, 82]
# odd:[63, 97, 31, 87, 61, 55, 83, 7]




# l1=[1,2,3,4,5,4,3,2,1,2,3,8,9,7,6,5,4,3,2,1,2,3,5,6,7,8,9,5,4]
# e=0
# n=int(input("enter a number:"))
# for i in l1:                                                          #counting the given number with out useing count method
#         if n==i:
#                 e+=1
# print(e)


# enter a number:3
# 5




# try:
#         l1=[1,2,3,4,5,4,3,2,1,2,3,8,9,7,6,5,4,3,2,1,2,3,5,6,7,8,9,5,4]
#         print(l1)
#         n=int(input("n:"))
#         for i in range(len(l1)):                                  #removeing the element form list with out useing remove method
#             if l1[i]==n:
#                 l1=l1[:i]+l1[i+1:]
#                 break
#         print(l1)
# except ValueError as value :
#     print(value)
    
# [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 8, 9, 7, 6, 5, 4, 3, 2, 1, 2, 3, 5, 6, 7, 8, 9, 5, 4]
# n:9
# [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 5, 6, 7, 8, 9, 5, 4]





# l1=[1,2,2,3,4,5,6,7,8,9,10]
# l2=[l1[i] for i in range(len(l1)) if i%2==0 and l1[i]%2==0]     #fetchin the even elements from list at even index
# print(l2)


# [2, 4, 6, 8, 10]


# l=[1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 5, 6, 7, 8, 9, 5, 4]
# d={}
# for i in l:
#         l2=[]
#         for j in range(len(l)): 
#                 if i==l[j]:
#                         l2.append(j)
#         d.update({i:l2})      
# print(d)
# print(l2) 
# {1: [0, 8, 18], 2: [1, 7, 9, 17, 19], 3: [2, 6, 10, 16, 20], 4: [3, 5, 15, 27], 5: [4, 14, 21, 26], 8: [11, 24], 7: [12, 23], 6: [13, 22], 9: [25]}




# l=[1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 7, 6, 5, 4, 3, 2, 1, 2, 3, 5, 6, 7, 8, 9, 5,6,9,10]
# a=[]
# b=[]
# c=[]
# for i in range(0,len(l)-2,3):                                        #devideing equally elements in list
#         a.append(l[i])
#         b.append(l[i+1])
#         c.append(l[i+2])
# print(f"a:{a} len:{len(a)}\nb:{b} len:{len(a)}\nc:{c} len:{len(a)}")

# a:[1, 4, 3, 2, 6, 3, 2, 6, 9] len:9
# b:[2, 5, 2, 3, 5, 2, 3, 7, 5] len:9
# c:[3, 4, 1, 7, 4, 1, 5, 8, 6] len:9


# l=[1,2,3,4,5,6,7,7,8,9]
# print(l)
# n=int(input("enter a key :"))                         #finding index of given number without useing built-in-methods
# for i in range(len(l)):
#         if l[i]==n:
#                 print("index of",n,"is",i)
#                 break
# else:
#         print(f"{n} not in list")
        
# [1, 2, 3, 4, 5, 6, 7, 7, 8, 9]
# enter a key :6
# index of 6 is 5


# l=[1,5,2,6,9,10,51,78,32,86,7,23,56,72,55]
# print(l)
# n=int(input("enter 1st num:"))
# n1=int(input("enter 2nd num:"))
# if (n or n1 )not in l:
#         print("eneter valid input")
# o=l.index(n)
# o1=l.index(n1)                                       #finding the elements between given numbers
# k=l[o+1:o1]
# if not k:
#         k=l[o1+1:o]
# print(f"elements:{k}\nlength:{len(k)}")
        

# enter 1st num:5
# enter 2nd num:78
# elements:[2, 6, 9, 10, 51]
# length:5

# enter 1st num:78
# enter 2nd num:5
# elements:[2, 6, 9, 10, 51]
# length:5


# l1=[]
# a=input("enter element :")
# while a:
#         l1.append(a)                                          #tacking number of inputs from user
#         a=input("enter element :")
# print(l1)


# enter element :mani
# enter element :123
# enter element :1.5
# enter element :
# ['mani', '123', '1.5']

# n=int(input("enter the len of list :"))
# l3=[int(input("enter element:")) for i in range(n)]
# class lis:
#         def __init__(self,l,k,dif):
#                 self.l=l
#                 self.k=k
#                 self.dif=dif
#                 self.r1=self.k-self.dif
#                 self.r2=self.k+self.dif
#                 self.l1=[i for i in range(self.r1+1,self.r2)]
#         def my_list(self):
#                 self.l3=[]
#                 for i in self.l:
#                         if i in self.l1:
#                                 self.l3.append(i)
#                 if not self.l3:
#                         return 0
#                 else:
#                         return self.l3
                
# l=lis(l3,int(input("enter key:")),int(input("enter dif:")))
# print(l.my_list())





# enter the len of list :5
# enter element:1
# enter element:2
# enter element:3
# enter element:4
# enter element:5
# enter key:4
# enter dif:2
# [3, 4, 5]


# l=[1,5,3,2,4]


# for i in range(len(l)-1):
#     for j in range(i+1,len(l)):                                  #second maximum value in list
#         if l[i]<l[j]:
#             l[i],l[j]=l[j],l[i]

# print(l)

# l=[1,5,3,2,4]
# print(l)
# for i in range(len(l)-1):
#     for j in range(1,len(l)):
#         if l[i]<l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)



# l=[44,5,778,2,3,56,7,45,6,2,5,2]
# c=0
# while c<2:
#     m=max(l)
#     l.remove(m)
#     c+=1
# print(max(l))




# n=int(input("n :"))
# for i in range(n):
#     for j in range(2*n-1):
#         if i+j>=n-1 and j-i<=n-1:
#             print('*',end=' ')
#         else:
#             print(" ",end=" ")
#     print()


# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     for k in range(i+1):
#         print("*",end=" ")
#     print()


# n=5
# for i in range(n):
#     print("  "*(n-1-i)+" *"*(2*i+1))



# l=[1,1,2,2,2,3]
# l2=[]
# s=[(i,l.count(i)) for i in set(l)]                           #sort the list by element count
# s.sort(key=lambda x: x[1])
# for k,v in s:
#     for j in range(v):
#         l2.append(k) 
# print(l2)

# Output-->[3, 1, 1, 2, 2, 2]



# a=["cat","dog","god","tca","act"]
# d={}
# for i in range(len(a)):
#     w="".join(sorted(a[i]))
#     if w not in d:
#         d[w]=[i+1]
#     else:
#         d[w].append(i+1)
   
# print(d)




