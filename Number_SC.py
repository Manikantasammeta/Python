class Number_Series:


    def __init__(self,n):
        self.n=n







    def Even (self):
        for i in range(self.n*2-1):
            if i%2==0:
                print(i,end="   ")
    def Odd(self):
        for i in range(self.n*2):
            if i%2==1:
                print(i,end="   ")
    def Factorial(self):
        while self.n>0:
            f=1
            for i in range(self.n,1,-1):
                f=f*i
            print(f,end="  ")
            self.n-=1

    def Prime_Number(self):
        while self.n>0:
    
    
    
            
    # def Strong_Number(self):
    #     s=0
    #     while self.n>0:
    #         rem=n%10
    #         f=1
    #         for i in range(rem,1,-1):
    #             f=f*i
    #             s=s+f
    #             self.n=self.n//10
    #             print(s,end="  ")

n=Number_Series(5) 
n.Even()
print()
n.Odd()
print()
n.Factorial()
print()
n.Strong_Number()
 