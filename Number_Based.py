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










