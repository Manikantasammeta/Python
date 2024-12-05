# d={6:7,1:2,0:1,8:9,3:4,6:7,4:5,5:6,7:8}
# d1={}
# l=[i for i in d.keys()]
# l.sort(reverse=True)
# for i in l:
#     d1.update({i:d.get(i)})
# print(d1)

# {8: 9, 7: 8, 6: 7, 5: 6, 4: 5, 3: 4, 1: 2, 0: 1}    # reversing dict by keys

# d1={12:45,1:65,98:34,76:34}
# d2={44:54,45:98,65:98,0:34}
# d3={90:1,34:23,5:32,89:56}
# d21={}
# for i in (d1 ,d2): d21.update(i)
    
# print(i)




# dic1={12:45,1:65,98:34,76:34}
# dic2={44:54,45:98,65:98,0:34}
# dic3={90:1,34:23,5:32,89:56}                               # adding the dicits
# dic4 = {}
# for d in (dic1, dic2, dic3):
#   dic4.update(d)
# print(dic4)

# {12: 45, 1: 65, 98: 34, 76: 34, 44: 54, 45: 98, 65: 98, 0: 34, 90: 1, 34: 23, 5: 32, 89: 56}



# d1={"a":21,"b":45,"c":90}
# for i ,j in d1.items():
#     print(i,"->",j)
    
# a -> 21
# b -> 45
# c -> 90

# class myclass:
#     x=100
#     y=200
    
#     def __init__(self):
#         self.a=10
#         self.b=20
        
#     def m1(self):
#         print("i am m1")
        
        
# m=myclass()
# m.m1()
# print(m())




# d={1:2,4:34,7:45,4:89,5:34,56:23,32:56,45:23}
# d1={}
# l=[i for i in d.items()]
# print(l)
# e=l[0][1]
# for i in l:
#     if i[1]<e:
#         l[0]=l[1]
# print(l)
# d1={1:1,2:2,3:3}
# d2={4:4,5:5,6:6,7:7}
# d={}
# for i in d1,d2:
#     d.update(i)
# print(d)

# d={1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}
# n=int(input("enter a number:"))                         #         checkomg the key present in dic or not
# l=[i for i in d.keys()]
# if n in l:
#     print("it is allready present in dict")
# else:
#     print("no notpresent")
    
# enter a number:5
# it is allready present in dict

# l=["123","@@@@","i am mani","    @","abcd","Abcd"]
# for i in l:
#     c=0
#     for j in range(len(i)):
#         if i[j].isalpha():
#             pass
#         if i[j].isspace():
#             pass
#         else:
#             c+=1
#     if c%2==0:
#         print(i)


# d={'b': 3, 'a': 2, 'c': 1}            #sorting the dict with out using any method  DESC Order
# d1={}
# keys = list(d.keys())
# for i in range(len(keys)-1):
#     for j in range(1,len(keys)):
#         if d[keys[i]] < d[keys[j]]:
#             keys[i], keys[j] = keys[j], keys[i]
            
# for i in keys:
#     d1.update({i:d[i]})
# print(d1)

# output:{'b': 3, 'a': 2, 'c': 1}

# d={'b': 3, 'a': 2, 'c': 1}            #sorting the dict with SORT METHOD IN LIST any method  ASC Order
# d1={}                                     #by KEYS
# keys = list(d.keys())
# keys.sort()
# for i in keys:
#     d1.update({i:d[i]})
# print(d,d1)

# output:{'a': 2, 'b': 3, 'c': 1}


# d={'b': 3, 'a': 2, 'c': 1}            #sorting the dict with SORT METHOD IN LIST any method  DESC Order 
# d1={}                                   # by KEYS
# keys = list(d.keys())
# keys.sort(reverse=True)
# for i in keys:
#     d1.update({i:d[i]})
# print(d1)

# output:{'c': 1, 'b': 3, 'a': 2}

# d={'b': 3, 'a': 2, 'c': 1}            # sorting the dict with SORT METHOD IN LIST Asc Order
# d1={}                                  # by VALUES
# val = list(d.values())
# val.sort()
# for i in range(len(val)):
#     for key, value in d.items():
#         if value == val[i]:
#             d1[key] = value
# print(d1)

# output:{'c': 1, 'a': 2, 'b': 3}






# d={'b': 3, 'a': 2, 'c': 1}            # sorting the dict with SORT METHOD IN LIST  Desc
# d1={}                                  # by VALS
# val = list(d.values())
# val.sort(reverse=True)
# for i in range(len(val)):
#     for key, value in d.items():
#         if value == val[i]:
#             d1[key] = value
# print(d1)

# output:{'b': 3, 'a': 2, 'c': 1}



#             #  WITH  OUT SORT METHOD IN LIST  Desc
# d1={}                                  # by VALUES
# val = list(d.values())
# for i in range(len(val)):
#     for j in range(1,len(val)):
#         if val[i]<val[j]:
#             val[i],val[j]=val[j],val[i]
# for i in range(len(val)):
#     for key, value in d.items():
#         if value == val[i]:
#             d1[key] = value
# print(d1)

# output:{'b': 3, 'c': 1, 'a': 2}


# d={'b': 3, 'a': 2, 'c': 1}            #  WITH  OUT SORT METHOD IN LIST ASC
# d1={}                                  # by VALUES
# val = list(d.values())
# for i in range(len(val)):
#     for j in range(1,len(val)):
#         if val[i]>val[j]:
#             val[i],val[j]=val[j],val[i]
# for i in range(len(val)):
#     for key, value in d.items():
#         if value == val[i]:
#             d1[key] = value
# print(d1)
# output:{'c': 1, 'b': 3, 'a': 2}

# d={'b': 3, 'a': 2, 'c': 1}            #  WITH  OUT SORT METHOD IN LIST ASC
# d1={}                                  # by KEYS
# key = list(d.keys())
# for i in range(1,len(key)):
#     for j in range(0,len(key)):
#         if ord(key[i])<ord(key[j]):
#             key[i],key[j]=key[j],key[i]    
# print(key)        
# for i in key:
#     d1.update({i:d[i]})
# print(d1)

# output:{'a': 2, 'b': 3, 'c': 1}


# d={'b': 3, 'a': 2, 'c': 1}            #   WITH OUT SORT METHOD IN LIST ASC
# d1={}                                  # by KEYS
# key = list(d.keys())
# for i in range(len(key)):
#     for j in range(1,len(key)):
#         if key[i]<key[j]:
#             key[i],key[j]=key[j],key[i]            
# for i in key:
#     d1.update({i:d[i]})
# print(d1)
# output:{'c': 1, 'a': 2, 'b': 3}


# d = {"a": 20, "b": 10, "c": 30, "e": 40}
# d1 = {"a": 20, "b": 10, "d": 0, "f": 40}
# d2 = {}

# output:{'a': 40, 'b': 20, 'c': 30, 'e': 40, 'd': 0, 'f': 40}

# for key in d.keys():
#     if key in d1:
#         d2[key] = d[key] + d1[key]
#     else:
#         d2[key] = d[key]

# for key in d1.keys():
#     if key not in d:
#         d2[key] = d1[key]

# print(d2)


# output:{'a': 40, 'b': 20, 'c': 30, 'e': 40, 'd': 0, 'f': 40}


# d={"j":10,"a":20,"b":30,"c":20,"d":40,"e":30,"f":30}
# l1=[i for i in d.keys()]
# l2=[i for i in d.values()]
# l3=[]
# for i in l2:
#     if i not in l3:
#         l3+=[i]
        
# d1={}
# print(l3)
# for i in range(0,len(l3)):
#     c=l2.count(l3[i])
#     if c>1 :
#         d1.update({l1[i]:l3[i]*c})
#     else:
        
#         d1.update({l1[i]:l3[i]})
# print(d1)

# d = {"j": 10, "a": 20, "b": 30, "c": 20, "d": 40, "e": 30, "f": 30,"s":100}
# l1 = [i for i in d.keys()]
# l2 = [i for i in d.values()]
# l3 = []
# for i in l2:
#     if i not in l3:
#         l3 += [i]

# d1 = {}
# for i in range(len(l3)):
#     c = l2.count(l3[i])
#     if c > 1:
#         d1[l1[l2.index(l3[i])]] = l3[i] * c
#     else:
#         d1[l1[l2.index(l3[i])]] = l3[i]

# print(d1)

# Marks={"Raju":{"Eng":0,"Phy":90,"Math":46},
#        "pinky":{"Phy":45,"Eng":65,"Math":0},
#        "Sita":{"Math":46,"Eng":50,"Phy":45},
#        "Mahesh":{"Eng":0,"Phy":19,"Math":99}}
# students=list(Marks.keys())
# print(students)
# print(Marks.items())

# Score=[]
# for name,mrk in Marks.items():                        # highest Marks
#     m=0
#     for sub,scr in mrk.items():
#         m=m+scr
#     Score.append(m)
    
# std_ind=Score.index(min(Score))
# std_ind2=Score.index(max(Score))

# print("least marks->",students[std_ind],min(Score))
# print("highest marks->",students[std_ind2],max(Score))


# students=list(Marks.keys())
# Math_marks= [Marks[student]["Math"] for student in students] 
# Pyh_marks=[Marks[student]["Phy"] for student in students]         #tabular format
# eng_marks=[Marks[student]["Eng"] for student in students] 
# print(f"name    math    phy eng")
# for i in zip(students,Math_marks,Pyh_marks,eng_marks):
#     print(f"{i[0]}  {i[1]}  {i[2]}  {i[3]}")

# for name,mrk in Marks.items():
#     for sub,score in mrk.items():         who got zero '0'
#         if score==0:
#             print(name,sub)

# students = list(Marks.keys())
# print(students)
# math_scores = [Marks[student]["Math"] for student in students]  
# print(math_scores)
# #who got same marks in the math
# result = []
# for i in range(len(math_scores)):
#     for j in range(i + 1, len(math_scores)):
#         if math_scores[i] == math_scores[j]:
#             result.append((students[i], students[j]))
# print(result)

# pinky=0
# raju=0
# for name,marks in Marks.items():         # Avg between raju and pinky
#     m=0
#     for sub,mrk in marks.items():
#         m+=mrk
#     if name=="pinky":
#         pinky=m
#     if name=="raju":
#         raju=m
# print(abs(raju-pinky)/3)

# raju_total = sum(Marks["Raju"].values())
# pinky_total = sum(Marks["pinky"].values())

# total=abs(raju_total-pinky_total)
# print(total/3)

# c=0
# nam=""
# for k,v in Marks.items(): 
#     m=0
#     for j in v.values():                      #highest marks 
#         m+=j
#     if m>c:
#         nam=k
#         c=m    
# print(nam,c)

#output -->Sita 141

# std={"mani":{"age":15,"sub":{"Math":90,"sci":85,"eng":88}},
#      "reddy":{"age":25,"sub":{"Math":50,"sci":15,"eng":28}}
#      }

# std.update({"gopi":{"age":21,"sub":{"math":22,"sci":88}}})










# std["mani"]["age"]=99

# for i in std.values():
#     avg=0
#     for sub,scr in i["sub"].items():
#         avg+=scr
#     print(avg//3)


d={"a":{"d":20,"c":{"e":None},"f":{"g":20,"h":None}},"i":{"j":None,"k":{"l":30,"m":None}}}

def fun(d1):
    
    for k,v in d1.items():
        if type(v)==dict:
            fun(v)
        if v==None:
            print(k)
    
                     
                     
fun(d)
                            