# l=["B:-1","A:1","B:3","A:5"]
# l1=[]

# for i in range(len(l)-1):
#     for j in range(1,len(l)):
#         if l[i][1] not in l1:
#             if l[i][0]==l[j][0]:
#                 a1=int(l[i][-1])
#                 a2=int(l[j][-1])
#                 if l[i][-2]=="-":
#                     a1=-(a1)
#                 if l[j][-2]=="-":
#                     a1=-(a1)
#                 d=a1+a2
#                 if d>0:
#                     y=str(l[i][0])
#                     lo=y+":"+str(d)
#                     l1.insert(0,(str(lo))) 
#                 elif d==0:
#                     break
# print(l1)
# l1.sort()
# print(l1)            


n=5
a=1
val=ord("A")
for i in range(n):
    for j in range(n):
        if i==j:
            print(a,end=" ")
            a+=1
        if i>=j:
            print(chr(val),end=" ")
            val+1
        else:
            print(" ",end=" ")
    print()