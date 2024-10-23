import random as re


class persion:
    def __init__ (self,name,panno,age,dob):
        self.name=name
        self.age=age
        self.dob=dob
        self.panno=panno

class P1(persion):
    def __init__(self,name,panno,age,dob,gender):
        super().__init__(name,panno,age,dob)
        self.gender=gender 


    def display(self):
        print(f"""
                    PANCARD
                NAME    :   {self.name}
                AGE     :   {self.age}
                GENDER  :   {self.gender}
                BOB     :   {self.dob}
                PAN NO  :   {self.panno}""")





p1=P1("MANI","KLJ7654BG",21,"14-04-1999","F")

p1.display()