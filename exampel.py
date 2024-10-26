# s="Vcube@Solutions"
# d={}
# for i in s:
#     c=s.count(i)
#     d.update({i:c})
    
# print(d)


# class A:
#     def method(self):
#         print("A method")

# class B(A):
#     pass

# class C(A):
#     def method(self):
#         print("C method")
        
# class d(A):
#     def method(self):
#         print("this is d method")

# class D(B,d,C):
#     pass

# obj = D()
# obj.method()

# try:
#     n=int(input("enter a number :"))
# except:
#     print("plz enter a integer value input")
    
    
# else:  
#     v=ord("A")
#     for i in range(n):
#         for j in range(n):
#             print(chr(v),end=" ")
#             v+=1
#             while v>ord("Z"):
#                 v=ord("A")
#         print()

n=5
for i in range(1,n+1):
    print((n-i)*" "+i*"* ")
    print()