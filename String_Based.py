#                ALL THE PYTHON CODE ARE COMMENTED. IF YOU WANT TO RUN AND EXECUTE THE CODE,JUST UNCOMMENT THE CODE. 
#                THE RESPECTIVE OUTPUT WILL BE DISPLAYED AT THE BOTTOM OF THE CODE. CHECK IT ONCE.









# s=input("Enter srt :")
# i=int(input("No :"))
# g=[]
# d=len(s)                                          #fetching the letters by tacking the user input
# for j in range(d):
#     if (j+1)%i==0:
#         g.append(s[j])
#     else:
#         continue
# print(*g)
#
#                      out put
# Enter srt :manireddy
# No :3
# n e y
# Enter srt :manireddy
# No :2
# a i e d



# s=input("Enter Str :")
# Captial_letters=[]
# Small_Letters=[]
# for i in s:
#     if ord(i)<ord("Z"):
#         Captial_letters.append(i)
#     else: Small_Letters.append(i)                                  #saperating the capital and small values for user
# print("Captial_letters :",*Captial_letters)
# print("Small_Letters :",*Small_Letters)

#           out put :

# Enter Str :ManiReddy
# Captial_letters : M R
# Small_Letters : a n i e d d y

# Enter Str :MANIreddy     
# Captial_letters : M A N I
# Small_Letters : r e d d y


# n=input("enter string:").upper()
# for i in range(len(n)):
#     if n[i].isalpha():                    #the string decoading
#         d=ord(n[i])
#         h=d-2
#         while h<ord("A"):
#             h=h+26
#         print(chr(h),end="")
#     else:
#         print(n[i],end="")


# enter string:mani@kanta123
# KYLG@IYLRY123



# n=input("enter str :")
# o=0
# for i in range(len(n)):
#     if n[i] in "AEIOUaeiou":                                     # counting the number of ovels in goven string
#         o+=1
#         # print(n[i],end=" ")
# print(o)


# enter str :mani kanta reddy sammeta
# 8



# n=input("enter str:")
# srt=0
# spl=0
# num=0

# for i in n:
#     if i.isalpha():                                         # finding thr str, num,spl-ch in given string
#         srt+=1
#     elif i.isnumeric():
#         num+=1 
#     else:
#         spl+=1
# print(f"str:{srt}\nnum:{num}\nspl:{spl}")

# enter str:mani kanta reddy @1234@
# str:14
# num:4
# spl:5



# n=input("enter str:")
# sc=False
# ul=False
# up=False
# num=False
# for i in n:
#     if "a"<=i<="z":                                         # Checking the string is valid ro not
#         ul=True
#     elif "A"<=i<="Z":
#         up=True
#     elif "0"<=i<="9":
#         num=True
#     else:
#         sc=True
# if len(n)>8 and sc and ul and up and num:
#     print("valid")
# else:
#     print("not valid")


# enter str:Manireddy@123
# valid
# enter str:mani
# not valid





# s="ManiKanta"
# s2=""
# for i in s:
#     if "A"<=i<="Z":
#         s2+=chr(ord(i)+32)                                                #swapcase 
#     elif "a"<=i<="z":
#         s2+=chr(ord(i)-32)
#     else:
#         s2+=i
        
# print(s2)


# mANIkANTA


# s="python"
# s2=""
# for i in s:                                       #reversing the string
#     s2=i+s2
# print(s2)



# s="Spiderman is a good man"
# s=(input("enter str:"))
# s2=s.split( )
# s3=""
# for i in s2:
#     s1=i[::-1]
#     s3=s3+s1+" "                                      #reversing the strings in the sentences
# print(s3)






# namredipS si a doog nam 



# s="i am mani"
# s1=""
# s3=""
# for i in s:
#     if i!=" ":
#         s3=i+s3
#     else:
#         s1+=s3+i
#         s3=""
# else: s1+=s3
# print(s1)



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


# ot-->
# 2
# ['ba', 'ab']

# enter str:abc
# 6
# ['cba', 'acb', 'abc', 'cab', 'bac', 'bca']

# 24
# ['mnai', 'ianm', 'iamn', 'main', 'nami', 'anmi', 'iman', 'inam', 'anim', 'amin', 'niam',
#  'mian', 'inma', 'ainm', 'nima', 'mani', 'aimn', 'nmia', 'naim', 'amni', 'nmai', 'mina', 'imna', 'mnia']




# s="spiderman is a super hero"
# d={"a":"@","i":"!","s":"$","o":"0", " ":"_"}
# h=list(d.keys())
# s1=""
# for i in s:
#     if i.lower() in h:                                        #replaceing the given str with given dict values
#         s1=s1+d.get(i)
#     else:
#         s1=s1+i
# print(s1)

# $p!derm@n_!$_@_$uper_her0


# s="Spiderman is a super hero"
# print(s)
# s1=input("enter str:").upper()
# c=0
# for i in s:                                          #replaceing the string if count of the letter it is even then Upper if it is odd Lower                                           
#     if s1==i.upper():
#         c+=1
# print(c)  
# s2=""     
# for i in s:
#     if i.upper()==s1.upper():
#         if c%2==0:
#             s2=s2+i.upper()
#         else:
#              s2=s2+i.lower()
#     else:
#         s2+=i
# print(s2)

# ot-->
# Spiderman is a super hero
# enter str:a
# 2
# SpidermAn is A super hero

# Spiderman is a super hero
# enter str:s
# 3
# spiderman is a super hero


# s=input("enter str:")
# # print(s)
# k=list(s.split())
# j=k[0]                                                           # fetching the longest word from the sentence
# for i in k:
#     if len(i)>len(j):
#         j=i
# print(j)

# enter str:i am mani
# mani

# s=input("enter str:")
# # print(s)
# k=list(s.split())
# j=k[0]                                                            #fetching the smallest word from the sentence
# for i in k:
#     if len(i)<len(j):
#         j=i
# print(j)

# enter str:i am mani
# i


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
   
# ot-->
# no of pass:4
# length od pass :5
# ['IbySF', 'DhHGI', 'w2i8D', '5QLVM'] 





# s="manimai"
# l1=[]
# for i in s:
#     if i not in l1:
#         l1.append(i)                      #unique values of given str in sorted order
# l1.sort()
# print(*l1)

# ot-->
# a i m n




# n=input("enter str:")
# l1=[i for i in set(n) if n.count(i)==1]           #finding the uniqe valus in given str and sorting the str
# l1.sort()
# print("".join(l1))

# enter str:mani
# aimn

# enter str:i am mani
# n



# list1=[1,2,3,4]
# list2=[1,2,3,4]
# list3=[1,2,3,4]
# list4=[1,2,3,4]
# list5=[1,2,3,4]
# list6=[]
# list7=[1,2,3,4]
# list8=[1,2,3,4]
# list9=[1,2,3,4]
# list10=[1,2,3,4]

# l=[list1,list2,list3,list4,list5,list6,list7]



# class my_str:
#     def __init__(self,s):
#         self.s=s
#     def mycount(self):
#         d={}
#         for i in self.s:
#             if i.isalpha():
#                 f=self.s.count(i)
#                 d.update({i:f})
#         return d
    
#     def co(self):
#         d1={}
#         for i in self.s:
#             l1=[]
#             for j in range(len(self.s)): 
#                 if i==self.s[j]:
#                     l1.append(j)
#             d1.update({i:l1})
#         return d1
# d=my_str("i am mani reddy")
# print(d.mycount())
# print(d.co())


# s="mmmaaaanni"
# s1=set(s)
# s2=list(s1)
# s2.sort()
# for i in s2:
#     d=s.count(i)
#     if d>=2:
#         print(i,d)


# def mtr(sr,num):
#     s=""
#     m=len(sr)
#     while m>0:
#         s=s+sr[:4]+"\n"
#         m-=4
#         sr=sr[m:len(sr)]
#     return s
    
# print(mtr(s,n1))


# s=input("enter string")
# n1=int(input("enter range:"))
# s1=""
# c=0
# for i in range(len(s)):
#     if c>n1-1:
#         s1=s1+"\n"
#         c=0
#     s1=s1+s[i]
#     c+=1

# print(s1)
    
# enter stringmanikantareddy 
# enter range:5
# manik
# antar
# eddy

# s="Ab1"
# print("True") if s.isalnum() else print("False")
# print("True") if s.upper() else print("False")
# print("True") if s.lower() else print("False")


# from num2words import num2words

# print(num2words(int(input("ente a number : "))))      # INT TO SPELLING CONVERSION

# def number_to_words(num):
#     below_20 = ['', 'one','two','three','four','five','six','seven','eight','nine',
#                  'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
#     tens = ['', '','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
#     thousands = ['','thousand','million','billion']

#     def words(n):
#         if n < 20:
#             return below_20[n]  
#         elif n < 100:
#             if n % 10 == 0:
#                 return tens[n // 10]
#             else:
#                 return tens[n // 10] + ' ' + below_20[n % 10]         # INT TO SPELLING CONVERSION
#         elif n < 1000:
#             if n % 100 == 0:
#                 return below_20[n // 100] + ' hundred'
#             else:
#                 return below_20[n // 100] + ' hundred and ' + words(n % 100)
#         else:
#             for i, v in enumerate(thousands):
#                 if n < 1000 ** (i + 1):
#                     if n % (1000 ** i) == 0:
#                         return words(n // (1000 ** i)) + ' ' + v
#                     else:
#                         return words(n // (1000 ** i)) + ' ' + v + ' ' + words(n % (1000 ** i))
#     if num == 0:
#         return "zero"
#     return words(num)

# number = int(input("Enter a number : "))
# print(number_to_words(number))
 
 
 

 
# import random as rm               # Finding the Possibul Combinations Based on the given String
# s=input("enter: ")
# l=[]
# l1=len(s)
# fac=1

# while l1!=0:
#     fac=l1*fac
#     l1-=1

# while len(l)<fac:
#     s1=""
#     while len(s1)<len(s):
#         c=rm.choice(s)
#         if c not in s1:
#             s1+=c
#     if s1 not in l:
#         l.append(s1)
     
# print(l)
# output:['abc', 'bac', 'bca', 'cab', 'cba', 'acb']