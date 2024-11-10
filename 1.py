# l=[0,1,2,4,1,4]

# for i in range(0,len(l),2):
#     for j in range(1,len(l)-1,2):
#         for k in range(2,len(l)-2,2):
#             if l[i]>l[j]<l[k]:
#                 print("True")
#                 break
# else:
#     print("false")

# n=int(input())
# val=0
# for i in range(n):
#     val1=val
#     for j in range(n+i):
#         if i+j>=n-1:
#             if j>n-1:
#                 val-=1
#                 print(val,end=" ")
#             else:
#                 val+=1
#                 print(val,end=" ")
#                 # val+=1
#         else:
#             print(" ",end=" ")
#     print()
#     val=val1
        
# n=5
# z=n
# for i in range(5-1,0,-1):
#     z=z*i
#     print(i)
# print(z)

# n=5
# def fun(n):
#     if n>1:
#         return n*fun(n-1)
#     return n
# print(fun(n))

# n=145
# s=0

# while n>0:
#     r=n%10
#     y=1
#     for i in range(r,0,-1):
#         y=y*i
#     s=s+y
#     n=n//10
# print(s)

# n=5
# val=ord("A")
# for i in range(n):
#     a=val
#     for j in range(i+1):
#         print(chr(val),end=" ")
#         val+=1
#     print()
#     val=a
# n=5
# val=ord("A")+n-1
# for i in range(n):
#     a=val
#     for j in range(n):
#         if i%2==0:
#             print(chr(val),end=" ")
#             val+=1
#         else:
#             print(chr(val),end=" ")
#             val+=1
#         if val>ord("Z"):
#             val=ord("A")
#     print()
#     val=a+n 

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or j==n-1 or i==n-1 or i==j or i+j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# n=5
# for i in range(n):
#     for j in range(n//2+1):
#         if i+j<=n-1 and i>=j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=5
# val=ord("A")
# e=True
# for i in range(n):
#     a=val
#     for j in range(n):
#         if i%2==0:
#             if e:
#                 print(chr(val),end=" ")
#             else:
#                 print(chr(val+32),end=" ")
#             val+=1
#         else:
#             if e:
#                 print(chr(val),end=" ")
#             else:
#                 print(chr(val+32),end=" ")
#             val-=1
#         e=not(e)
#     print()
#     val=a+2*n-1 if i%2==0 else a+1

# n=5
# for i in range(n):
#     val=1
    
#     for j in range(n+i):
#         if i+j>=n-1 :
#             print("",val,end="")
#             if j<n-1:
#                 val+=1
#             else:
#                 val-=1
#         else:
#             print(" ",end=" ")
#     print()

# n=int(input("enter a number :"))
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(2*i-1):
#         if j==0 or j==2*i-2:
#             print("*",end=" ")
#         else:
#             if i==n:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#     print()


# n=int(input("enter number :"))
# s=0
# for i in range(0,len(str(n))+1,2):
#         s+=int(str(i))
# print(s)





# class A:
#     x=20
#     def __init__(self,n):
#         self.x=30
        
    
# d=A(5)
# print(d.x)





# n=int(input("enter :"))
# x=0
# y=1
# while x<n:
#     y=y+x
#     print(y)
#     x+=1




# s="aabbbccde"
# d={}
# for i in s:
#     d.update({i:s.count(i)})
# print(d)
# l=[i for i in d.values()]
# l.sort()
# for i in l[::-1]:
#     p=d.get(i)
#     print(i,p)
    
# def pri(num):
#     for d in range(2,num):
#         if num%d==0:
#             return False
#     else:
#         return True
# n=int(input("enter :"))
# # print(pri(int(input("enter:"))))
# num=2
# count = 0
# num = 2
# _sum = 0
# while count < n:
#     if pri(num):
#         print(num)
#         _sum =_sum+ num
#         count += 1
#     num += 1
# print(_sum)


 
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:                       # primt
#              return False
#     return True

# def sum_of_first_n_primes(n):
#     count = 0
#     num = 2
#     prime_sum = 0
#     while count < n:
#         if is_prime(num):
#             prime_sum += num
#             count += 1
#         num += 1
#     return prime_sum

# n = 100
# print(f"The sum of the first {n} prime numbers is: {sum_of_first_n_primes(n)}")

# class Car:
#     def start_engine(self):
#         print("Engine started")

# class Driver:
#     def drive(self, car):
#         print("Driving the car")
#         car.start_engine()

# # Creating instances of Car and Driver
# car = Car()
# driver = Driver()







# # Sending a message to the Car object through the Driver object
# driver.drive(car)

# l2=[[0]*2]*2
# l=[[0, 0], [0, 0]]

# print(l)
# l[0][0]=1
# print(l)
# print(l[0][0]+l[1][0])


# s1="vcubesolutions"
# s2="rrrsolutions"
# s3=s1+s2
# l=[i for i in s3]
# l.sort()
# print(*l)

a=20
print(bin(a))
t=a<<2
print(t)

