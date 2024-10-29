# n=int(input("enter number:"))
# if n>0:
    
#     if n%2==0:
#         print(n," is even")
#     else:
#         print(n,"is odd")
# else:
#     print(n,"must be grater then zero")



# n=int(input("n:"))
# if n>=10 and n<=99:
#     if n%10==0:
#         print(f'{n} is divisibel by 10')
#     else:
#         print(f'{n} is  not divisibel by 10')
# else:
#     print( )


# s=input("enter str :")
# if (s>="A" and s<="Z") or (s>="a" and s<="z"):
#     if s in ['a','e','i','o','u','A','E','I','O','U']:
#         print(s,"is a  vowel")
#     else:
#         print(s,"is not a vowel")
# else:
#     print(s,"is not a character")


# s=input("enter str :").upper()
# if s.isalpha():
#     if s in ['A','E','I','O','U']:
#         print(s,"is a  vowel")
#     else:
#         print(s,"is not a vowel")
        
# else:
#     print(s,"is not a character")


# s=input("enter srt :")
# if s.isalpha(): 
#     if s.isupper():
#         val =ord(s)-64
#         print(val)
#     else:
#         print(s,"is lower ")
# else:
#     print(s,"is not a alpha")


# s=input("enter str :")
# c=0
# for i in s:
#     if i.isalpha():
#         c+=1
        
# print("the len of str is -->",c)

# s=input("enter str :")
# c=0
# while s!=None:
#     c+=1
#     s=s[1::]
# print(c)


# p=int(input("base:"))
# q=int(input("power:"))
# c=1
# while q!=0:
#     c*=p
#     q-=1
# print(c)

# n=int(input("enter age:"))

# if (n>=5 and n<=10) or n>55:
#     print("True")
# else:
#     print("False")


# def valuation(age,ill):
#     if (age>=5 and age<=10) or (age>=55 and ill):
    
#         return  False
#     else:
#         return False
    
    
# print(valuation(int(input("enter the age :")),input("true/false")))


# s=input("enter input")
# l=[]
# for i in s:
#     if (i in ['a','e','i','o','u','A','E','I','O','U'] and i.isalpha):
#         l.append(i)
# print(l)
# print(set(l))


# x=10
# y=10

# if x==y:
#     print("true")
# else:
#     print("False")
    
# if x is y:
#     print("True")
# else:
#     print("false")
    
    

# n=int(input("len of list:"))
# l=[int(input("enter ele: ")) for i in range(n)]
# print(l)
# l1=[]  
# for j in l:
#     l1.insert(0,j)

# print(l1)

# n=int(input("len of list:"))
# l=[int(input("enter ele: ")) for i in range(n)]
# print(l)
# c=0
# n1=int(input("enter val:"))
# o=int(input("o:"))
# for i in range(len(l)):
#     if n1==l[i]:
#         c+=1
#         if c==o:
#             print(i)
#             break   
# else:
#     print("ele no in list")


# n=int(input("len of list:"))
# l=[int(input("enter ele: ")) for i in range(n)]
# print(l)


# def happy(l):
#     even=0
#     odd=0
#     for i in l:
#         if i%2==0:
#             even+=i
#         else:
#             odd+=i
#     if even>odd:
#         return "Hello"
#     else:
#         return "Hi"
    
# print(happy(l))

 
# n=int(input("n: "))
# l=[]
# for i in range(n):
#     l.append(i*2+1)
# print(l)

# n=int(input("enter :"))
# for i in range(n):
#     print(i*2,end=" ")

 
# n=int(input("enter :"))
# for i in range(n*2):
#     if i%2==0:
#         print(i,end=" ")


# n=int(input("enter len  of dict :"))
# l1=[input("enter key:") for i in range(n)]
# l2=[input("enter val:") for i in range(n)]
# d={}
# for i in range(len(l1)):
#     d.setdefault(l1[i],l2[i])
# print(d)

# n=int(input("enter the len of list"))
# l1=[[input("enter the name:"), float(input("enter marks :"))] for i in range(n)]
# print(l1)
# maxx =l1[0][1]
# for i in range(n):
#     r=l1[i][1]
#     if r >maxx:
#         maxx =r
#         c=i
# # print(f' name is --> {l1[c][0]}')
# s1={1,2,3,4}
# s2={3,4,5,6}

# s3=s1.intersection(s2)
# s1.intersection_update(s2)
# print(s3)
# # print(s1)

# d={1:10,2:20,3:30,4:40}
# print(d.fromkeys(1,10))

# def table(n):
#     for i in range(1,11):
#         print(f"{n} x ",i,"==",i*n)
        
# table(int(input("enter number")))

# n=int(input("enter n :"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i,end=" ")



# n=int(input("enter how many elements :"))
# l=[int(input("enter the element :")) for i in range(n)]
# m =min(l)
# fact=[]
# for i in l:
#     s=set()                                            #GCD OF GIVEN NUMBERS
#     for j in range(1,m+1):
#         if i%j==0:
#             s.add(j)
#     fact.append(s)
# r1=fact[0]
# for i in range(1,len(fact)):
#     r1=r1.intersection(fact[i])
# print(f"The GCD of the of  {l} is-->  {max(r1)}")


# s=input("Enter the direction :").upper()
# l=0
# r=0
# for i in range(len(s)):                       #Direction probleam
#     if s[i]=='R':
#         r+=1
#         l-=1
#     if s[i]=="L":
#         l+=1
#         r-=1
# if l>=2 or r>=2:
#     print("SAVE")
# else:
#     print("NOT SAVE ")












# n=int(input("enter number :"))
# s=0
# while n>0:
#     if n%2==0:
#         s=s+n
#     n=n-1
# print(s)

     