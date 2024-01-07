import getpass
import datetime


def admin_panel():
    
    
    admin=[{'admin_username': 'krushank', 'admin_password': '12'}]
    
    current_date_time = datetime.datetime.now()
    formatted_date = current_date_time.strftime("%d-%m-%Y")
    formatted_time = current_date_time.strftime("%H:%M:%S")
    
    
    print()
    print()
    print("DATE :- ",formatted_date)
    print()
    print("TIME :- ",formatted_time) 
    while(True):
        print()
        print()
        print("----------------------------------------------------------")
        print("            YOU ARE DIRECTED TO ADMIN PANEL               ")
        print("----------------------------------------------------------")
        print()
        print("1. LOGIN")
        print("0. EXIT")
        print()
        print()
        choice1=int(input("Enter your choice = "))
        print()
        print()
        if(choice1==1):
            flag=0
            admin_username =input("Enter your username = ")
            admin_password =getpass.getpass("Enter your password = ")
            print("Just checking",admin_password)
            print("----------------------------------------------------------")
                
            for i in admin:
                if(admin_username==i["admin_username"] and admin_password==i["admin_password"]):
                    print()
                    print("--------------------------------------------------------")                    
                    print("       Congratulations",admin_username,"Log in sucessful")
                    print("--------------------------------------------------------")
                                                                                                    
                    flag=1
                                                                    
            if(flag==0):
                print("Your Entered Username or Password is Wrong")
                break
        elif(choice1==0):
            print()
            print()
            print("!! THANK YOU !!")
            print()
            print()
            break
            
        else:
            print()
            print(" !! ENTER VALID CHOICE !!")
            print()