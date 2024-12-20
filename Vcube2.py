# n=5
# cnt=0
# i=1
# while cnt<=(2*n)-1:
#     print('* ' *i )
#     if cnt<n-1:
#         i += 1
#     else:
#         i=i-1
#     cnt+=1
# x=[1,2,3]
# x=tuple(x)
# x[0]=2
# print(x)







# s="Raja"
# for i in range(0,len(s)):
#     for j in range(i,len(s)+1):
#         r=s[i:j]
#         if r==r[::-1]:
#             print(r)


# def find_largest_number(numbers):
#     return max(numbers)

# l=[22,56,2,99,15,78,1]
# res=find_largest_number(l)
# print(res)
        
# def is_palindrome(s):
#     s1=""
#     for i in s:
#         s1=s1+i
#     if s==s1:
#         return "palindrome"
#     else: return "not a palindrome"    
    
# s="madam"
# res=is_palindrome(s)
# print(res)



# s = "rfdeejkaaaajoaeiourduuudnfaaaa"
# y = "aeiouAEIOU"

# def extract_substrings(s, vowels):
#     substrings = []
#     current_substring = ""
#     surrounded_by_consonants = True

#     for char in s:
#         if char in vowels:
#             current_substring += char
#             surrounded_by_consonants = False
#         elif not surrounded_by_consonants:
#             if len(current_substring) >=2 and current_substring[0] == current_substring[-1]:
#                 substrings.append(current_substring)
#             current_substring = ""
#             surrounded_by_consonants = True
#         else:
#             surrounded_by_consonants = True

#     return substrings

# result = extract_substrings(s, y)
# print(",".join(result))


# l=[30,"PY",50,80,30,"JY",20,90,60,"QY",10]
# for i in range(len(l)-1):
#     if type(l[i])!=int:                                       #sorting only strings in list
#         for j in range(i+1,len(l)):
#             if type(l[j])!=int:
#                 if l[i]>l[j]:
#                     l[i],l[j]=l[j],l[i]
# print(l)
# # ot-->[30, 'Qy', 50, 80, 30, 'jy', 20, 90, 60, 'py', 10]


# s="i am learning python"
# s1=(input("enter str:"))
# s2=s.split( )
# s3=""
# for i in s2:
#     s1=i[::-1]
#     s3=s3+s1+" "                                      #reversing the strings in the sentences
# print(s3)


# marks = {
#     "sai": {"m": 22, "s": 32},
#     "mani": {"m": 26, "s": 33},
#     "gopi": {"m": 29, "s": 35},
#     "raju": {"m": 25, "s": 32},
#     "Pinky": {"m": 209, "s": 35}
# }

# high = []
# max_marks_s = 0

# # Find the highest marks in subject "s"
# for student, scores in marks.items():
#     if scores["s"] > max_marks_s:
#         max_marks_s = scores["s"]

# # Find students who have the highest marks in subject "s"
# for student, scores in marks.items():
#     if scores["s"] == max_marks_s:  
#         high.append(student)

# print(max_marks_s, high)


# s="Spiderman is a good man"
#     s="Python is a Programing language"
# # s=(input("enter str:"))
# s2=s.split( )
# s3=""
# for i in s2:
#     s1=i[::-1]
#     s3=s3+s1+" "                                      #reversing the strings in the sentences
# print(s3)



# S="we are in vcube sloutions we we we"   # COUNTING THE WORDS IN THE GIVEN SECNTENCE
# s1=S.split()
# print(s1)
# for i in s1:
#     print(i,"=",s1.count(i))

n=input("enter a value:")
try:
    v=int(n)
    print(v,"is int ")
except:
    try:
        v=float(n)
        print(v,"is float")
    except:
        try:
            v=complex(n)
            print(v,"is a complex")
        except:
              try:
                  v=bool(n)
                  print(v,"is bool")
              except:
                  try:
                    v=str(n)
                    print(v,"is str data type")
                  except:
                      print("given is mixex data type")