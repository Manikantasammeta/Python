class programs:
    def __init__(self,n):
        self.n=int(n)

    def R90(self):
        for i in range(self.n):
            for j in range(i+1):
                print("*",end=" ")
            print()
    

    def L90(self):
        for i in range(self.n):
            for j in range(self.n+1):
                if i+j>=self.n:
                    print("*",end=" ")
                else: print(" ",end=" ")
            print()
        
    def Reverse_L90(self):
        for i in range(self.n):
            for j in range(self.n):
                if i+j<=self.n-1:
                    print("*",end=" ")
            print()

    def Reverse_R90(self):
        for i in range(self.n):
            for j in range(self.n):
                if i<=j:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    def North_Piramid(self):
        for i in  range(self.n):
            for j in range(self.n+self.n-1):
                if i+j>=self.n-1 and j-i<=self.n-1:
                    print("*",end=" ")
                else: print(" ",end=" ")
            print()

    def East_Piramid(self):
        for i in range(2*self.n-1):
            for j in range(self.n):
                if i>=j and i+j<=2*self.n-2:
                    print("*",end=" ")

            print()

    def South_Piamid(self):
          for i in range(self.n):
            for j in range(2*self.n-i-1):
                if i<=j:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    def West_piramid(self):
        for i in range(2*self.n-1):
            for j in range(2*self.n-1):
                if i<=j and  i+j>=2*self.n-2:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    def Star(self):
        for i in range(self.n):
            for j in range(self.n):
                if i==j or i+j==self.n-1 or i==self.n//2 or j==self.n//2:
                    print("*",end=" ")
                else: print(" ",end=" ")
            print()
    
    def Rombus(self):
        for i in range(self.n):
            for j in range(self.n):
                if i+j==self.n//2 or j-i==self.n//2 or i-j==self.n//2 or i+j==self.n//2+self.n-1:
                    print("*",end=" ")
                else: print(" ",end=" ")
            print()
p=programs(5)
print("1")
p.L90()
print("2")
print()
p.R90()
print("3")
print()
p.Reverse_L90()
print("4")
print()
p.Reverse_R90()
print("5")
print()
p.North_Piramid()
print("6")
print()
p.East_Piramid()
print("7")
print()
p.South_Piamid()
print("8")
print()
p.West_piramid()
print("9")
print()
p.Star()
print("10")
print()
p.Rombus()


p.Star()
print("10")
print()
p.Rombus()