# n="12345"
# for i in range(len(n)):
#     for j in range(len(n)):
#         if i==j or i+j==len(n)-1:
#             print(n[j],end=" ")
 
            
#         else:
#             print(" ",end=" ")
#     print()
    
import re

th= open("re.txt","r")
w=th.readlines()
for i in w:
    for j in i.split():
        matc=re.search(r'[a-zA-Z0-9._%+-]+@gmail\.com',j)
        if matc:
            print(j,end=" ")