# import random as rm
# class my_marks:
#     # names=["mani","mahesh","abhinav","abhi","sadha","reddy","pinky","raju","rani","rowdy","roja","sai","siva","gopi","shiva"]
#     # math=[100, 85, 67, 95, 73, 96, 86, 78, 93, 98, 92, 68, 99, 83, 83]
#     # phy=[86, 80, 89, 96, 73, 89, 69, 87, 89, 66, 97, 73, 65, 79, 89]
#     # eng=[88, 77, 98, 88, 71, 71, 96, 69, 73, 83, 77, 95, 96, 66, 67]
#     # che=[80, 98, 88, 92, 88, 74, 66, 82, 73, 91, 81, 78, 75, 88, 78]
#     global mydic
#     mydic={'mani': {'math': 100, 'phy': 86, 'eng': 88, 'che': 80, 'total': 354},
#            'mahesh': {'math': 85, 'phy': 80, 'eng': 77, 'che': 98, 'total': 340}, 
#            'abhinav': {'math': 67, 'phy': 89, 'eng': 98, 'che': 88, 'total': 342}, 
#            'abhi': {'math': 95, 'phy': 96, 'eng': 88, 'che': 92, 'total': 371}, 
#            'sadha': {'math': 73, 'phy': 73, 'eng': 71, 'che': 88, 'total': 305}, 
#            'reddy': {'math': 96, 'phy': 89, 'eng': 71, 'che': 74, 'total': 330}, 
#            'pinky': {'math': 86, 'phy': 69, 'eng': 96, 'che': 66, 'total': 317}, 
#            'raju': {'math': 78, 'phy': 87, 'eng': 69, 'che': 82, 'total': 316}, 
#            'rani': {'math': 93, 'phy': 89, 'eng': 73, 'che': 73, 'total': 328}, 
#            'rowdy': {'math': 98, 'phy': 66, 'eng': 83, 'che': 91, 'total': 338}, 
#            'roja': {'math': 92, 'phy': 97, 'eng': 77, 'che': 81, 'total': 347}, 
#            'sai': {'math': 68, 'phy': 73, 'eng': 95, 'che': 78, 'total': 314}, 
#            'siva': {'math': 99, 'phy': 65, 'eng': 96, 'che': 75, 'total': 335}, 
#            'gopi': {'math': 83, 'phy': 79, 'eng': 66, 'che': 88, 'total': 316}, 
#            'shiva': {'math': 83, 'phy': 89, 'eng': 67, 'che': 78, 'total': 317}}



#     # def list_of_marks(self):

#     #     self.d=dict()
#     #     for i in range(len(self.names)):
#     #         n=self.names[i]
#     #         for j in range(4):
#     #             d1={}
#     #             d1.update({"math":self.math[i]})
#     #             d1.update({"phy":self.phy[i]})
#     #             d1.update({"eng":self.eng[i]})
#     #             d1.update({"che":self.che[i]})
#     #             d1.update({"total":int(self.math[i]+self.phy[i]+self.eng[i]+self.che[i])})
#     #         self.d.update({n:d1})
#     #     return self.d
    
    
    
    
#     def display(self):
#         print("-"*85)
#         print(f"""Name          MATH            PHT             ENG             CHE             TOTAL""")
#         print("-"*85)
#         for i in mydic:
#             print(f"""{i}""")  

# l=my_marks()
# l.display()


# mydic={     'mani': {'math': 100, 'phy': 86, 'eng': 88, 'che': 80, 'total': 354},
#            'mahesh': {'math': 85, 'phy': 80, 'eng': 77, 'che': 98, 'total': 340}, 
#            'abhinav': {'math': 67, 'phy': 89, 'eng': 98, 'che': 88, 'total': 342}, 
#            'abhi': {'math': 95, 'phy': 96, 'eng': 88, 'che': 92, 'total': 371}, 
#            'sadha': {'math': 73, 'phy': 73, 'eng': 71, 'che': 88, 'total': 305}, 
#            'reddy': {'math': 96, 'phy': 89, 'eng': 71, 'che': 74, 'total': 330}, 
#            'pinky': {'math': 86, 'phy': 69, 'eng': 96, 'che': 66, 'total': 317}, 
#            'raju': {'math': 78, 'phy': 87, 'eng': 69, 'che': 82, 'total': 316}, 
#            'rani': {'math': 93, 'phy': 89, 'eng': 73, 'che': 73, 'total': 328}, 
#            'rowdy': {'math': 98, 'phy': 66, 'eng': 83, 'che': 91, 'total': 338}, 
#            'roja': {'math': 92, 'phy': 97, 'eng': 77, 'che': 81, 'total': 347}, 
#            'sai': {'math': 68, 'phy': 73, 'eng': 95, 'che': 78, 'total': 314}, 
#            'siva': {'math': 99, 'phy': 65, 'eng': 96, 'che': 75, 'total': 335}, 
#            'gopi': {'math': 83, 'phy': 79, 'eng': 66, 'che': 88, 'total': 316}, 
#            'shiva': {'math': 83, 'phy': 89, 'eng': 67, 'che': 78, 'total': 317}}



# print("-"*105)
# print(f"""NAME              MATH                PHY                 eng                 che                 total""")
# print("-"*105)
# for i in mydic:
#     print(i)
#     if
            


print("enter 4 values")
c=1
d={}
while c<5:
    s=input(f"ENTER {c} NAME :").upper()
    n=int(input("ENTER SAL:"))
    d.update({s:n})
    c+=1
print("QUIT")
l=[i for i in d.keys()]
l.sort()
d1={}

for i in l:
    h=d.get(i)
    d1.update({i:h})
print("------------------------------")
print(f"""   NAME                               SAL   """)
print("------------------------------")

for i in l:
    print(f"""   {i.ljust(20)}              ${d.get(i)}.00""")
    # print(f"""              ${d.get(i)}.00""")

print("------------------------------")
print()
print()
print()
print()

d3=dict(sorted(d1.items(), key=lambda item: item[1]))
l1=[i for i in d3.keys()]
l2=[i for i in d3.values()]
print(f"HIGH SAL  NAME: {l1[0]}  SAL{l2[0]}")
print(f"LEAST SAL NAME: {l1[-1]} SAL {l2[-1]}")
    
    
    
    
