from datetime import datetime

print("WELCOME TO ATM")
print("ENTER ""1"" FOR BALANCE ENQUERY ")
print("ENTER ""2"" FOR WITHDRAW MONEY")
print("ENTER ""3" " FOR DIPOSIT MONEY")
print("ENTER ""4"" FOR PIN CHANGE")
print()
with open("ATM_PS.txt","r+") as file:
    n=file.read()
    pin=int(n)
with open("atm.txt","r+") as file:
    current_balance=file.read()



   
try:
    n=int(input("ENTER NUMBER:"))
    if n==1:
        s=int(input("ENTER THE PIN :"))
        if s==pin: 
            print("YOUR CURRENT BALANCE IS-->",current_balance)
            ti=open("Atm_hst.txt","a+")
            ti.write(f"YOUR BALANCE IS CHECKED: on {datetime.today().strftime('%y-%m-%d %H:%M:%S')}\n \n")
        else:
            print("INCORRECT PIN PLZ TRY AGAIN")
            
            
    elif n==2:
        e2=int(input("ENTER PIN:"))
        if e2==pin:
            a=int(input("ENTER THE AMOUNT :"))
            amt=int(current_balance)
            if amt-a>=2000:
                amt=amt-a
                ui=str(amt)
                nw_balance=current_balance.replace(current_balance,ui)
                with open("atm.txt","r+") as file:
                    new_balance=file.write(nw_balance)   
                ti=open("Atm_hst.txt","a+")
                ti.write(f"{a} RS/-  DEBETED FROM YOUR ACCOUNT ON {datetime.today().strftime('%y-%m-%d %H:%M:%S')} \n \n")
                print("PLZ TAKE YOUR MONEY")
                print("THE REMAINING MONEY IN YOUR ACCOUNT-->",amt)
            else: print("INNSUFFICNT BALANCE PLZ CHECH YOUR BALANCE")
        else:
            print("INCORRECT PASSWORD PLZ TRY AGAIN")


    elif n==3:
        print("ENTER YOUR PIN")
        r=int(input(("PIN :")))
        if r==pin:
            print("PLZ ENTER YOUR AMOUNT")
            e=int(input("ENTER AMOUNT :"))
            op=int(current_balance)
            balance= e + op
            jo=str(balance)
            mn=current_balance.replace(current_balance,jo)
            with open("atm.txt","r+") as file:
                dp_balance=file.write(mn)
            ti=open("Atm_hst.txt","a+")
            ti.write(f"{e} RS/-  CREDETED TO YOUR ACCOUNT ON {datetime.today().strftime('%y-%m-%d %H:%M:%S')} \n \n")
            print("YOUR MONEY SUCESSFULLY ADDED TO YOR ACCOUNT")
            print("NOW YOUR BALANCE IS -->",balance)
        else:
            print("INCRRECT PIN PLZ TRY AGAIN")
            
            
    elif n==4:
        print("PLZ ENTER YOUR PIN")
        f=int(input("ENTER YOUR PIN :"))
        with open("ATM_PS.txt","r") as file:
          n=file.read()
        pin=int(n)
        if f==pin:
            ok=input("PLZ ENTER YOUR NEW PIN :")
            nw_pass=n.replace(n,ok)
            with open("ATM_PS.txt","r+") as file:
                nk=file.write(nw_pass)
            ti=open("Atm_hst.txt","a+")
            ti.write(f"YOUR PIN '{f}' CHANGED TO '{ok}' ON {datetime.today().strftime('%y-%m-%d %H:%M:%S')} \n \n")
            print("YOUR'S PASSWORD SUCESSFULLY UPDATED")
        else:
            print("INCORRECT PIN PLZ TRY AGAIN")
    else:
        print(" PLZ ENTER A VALID IN PUT")



except:
    print("some thing went wrong plz try again")


