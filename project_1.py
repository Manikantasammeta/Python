class pyspiders:
    def __init__(self,*c):
        s=0
        for i in c:
            match i.upper():
                case "PYTHON":s+=self.python()
                case "WEB" :s+=self.web()
                case "FULL STACK" :
                    s+=self.python() 
                    s+=self.web()
                    s+=self.sql()
                case "SQl" : s+=self.sql()

                case _:
                    print("IVC")
                    break
            print(f"TOTAL DAYS  :  {s} Days")

    def python(self):
        print("""
                     PYTHON 
                Basics  : 30  Days
                Ooops   : 20  Days
                advance : 20 Days
                Pro     : 90 Days
                __________________
                total   :  160 Days
                __________________ """)
        return 160 


    def web(self):
        print("""
                     WEb 
                HTML  : 15  Days
                CSS   : 30  Days
                JS    : 15  Days
             _____________________
              total   : 50  Days
             _____________________""")
        return 50


    def sql(self):
        print("""
                     SQl
                BAsics    :  15  Days
                Functions :  15  Days
                Joins     :  20  Days
               ______________________
                  total   : 50  Days
               ______________________""")
        
        return 50
 









p=pyspiders("full stack")

