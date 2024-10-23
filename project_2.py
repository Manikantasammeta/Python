class bike:
    Brand="HONDA"
    Model="F7"
    def __init__(self,name,color,extra_fitting):
        self.name=name
        self.color=color
        self.extra_fitting=extra_fitting
        print()
        print(f"""
                  Bike Brand    : {bike.Brand}
                  model         : {bike.Model}
                  Model         : {self.name}
                  Color         : {self.color}
                  Extra_fitting : {self.extra_fitting}""")
        print("*"*50)

b=bike("Honda","red","double lights")
m=bike("Honda1","GReen","with out ligth")
