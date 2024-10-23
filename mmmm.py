# name= input("Enter Name :").upper()
# print()
# print(f"********* WELCOME {name} ***********")
# print()
# print(f"""   ITEMS                 PRICES
#             TOMATO                   25/-
#             KUKUMBER                 50/-
#             POTATO                   40/-
#             CARROT                   35/-
#             """)
# l1=[]
# items={"TOMATO":25,"KUKUMBER":50,"POTATO":40,"CARROT":35}
# r=True
# while r:
#     print("press q to stop buying")
#     item =input("Enterthe iteam :").upper()
#     kg=int(input("Enter the kgs:"))
#     l1.append(item)
#     if item =="Q":
#         r=False
# fu


s=input("Enter your name :").title()
print("MY Name is-->",s)
print("-"*30)
s1=""
s2=""
for i in s:
    if i>"A" and i<"Z":
        y=chr(ord(i)+32)
    elif i.isspace():
        y=chr(32)
    else:
        y=chr(ord(i)-32)
    ass = ord(i)
    s1=s1+"-"+y
    s2 =s2+"-"+str(ass)
    print(f"ASCII  value of {y} is  {ass}")
print()
print()
print(s1)
print(s2)
print("-"*30)
