from cryptography.fernet import Fernet
key = Fernet.generate_key()
fernet = Fernet(key)



import getpass
import datetime
from student_details import studentdetails
from field_select import field_select



def user_panel():
    
    user=[{'User_username': 'krushank', 'User_password': '123'}]

    current_date_time = datetime.datetime.now()
    formatted_date = current_date_time.strftime("%d-%m-%Y")
    formatted_time = current_date_time.strftime("%H:%M:%S")
    
    while(True):
            print()
            print()
            print("----------------------------------------------------------")
            print("            YOU ARE DIRECTED TO USER PANEL                ")
            print("----------------------------------------------------------")
            print()
            flag=0
            print("----------------------------------------------------------")
            print("                       HELLO USER                         ")
            print("----------------------------------------------------------")
            while(True):
                print("-------------------")
                print("|    1. REGISTER   |")
                print("|    2. LOGIN      |")
                print("|    0. EXIT       |")
                print("-------------------")
                
                choice2=int(input("Enter your choice = "))
                
                if(choice2==1):
                    print("------------------------------------------------------------------------------")
                    print("            Firstly Register yourself to solve all your Quries")
                    print("------------------------------------------------------------------------------")
                    try:
                        User_username=input("Enter your username = ")
                        User_password=input("Enter your password = ")
                    
                    except ValueError:
                        print("You have error in entering the Password !!")
                        print("Only Numbers are allowed in the Password")
                        User_username=input("Enter your username = ")
                        User_password=input("Enter your password = ")
                        
                    print("----------------------------------------")
                    print("|     REGISTRATION DONE SUCCESSFULL    |")
                    print("----------------------------------------")
                    
                    encMessage = fernet.encrypt(User_password.encode())
                    
                    user_registeration_set={}
                    user_registeration_set["User_username"]=User_username
                    user_registeration_set["User_password"]=User_password
                    user.append(user_registeration_set)
                    print(user_registeration_set)
                
                elif(choice2==2):
                    print()
                    print("DEAR , USER YOU NEED TO LOGIN")
                    print()
                    Login_user_username =input("Enter your Username = ")
                    Login_user_password =getpass.getpass("Enter your password = ")
                    print("----------------------------------------------------------")
                    
                    for i in user:
                        if(Login_user_username==i["User_username"] and Login_user_password==i["User_password"]):
                            print("")
                            print("<<<<  Log in successful  >>>>")
                            print()
                            print()
                            studentdetails()
                            field_select()
                            flag=1
                            
                            
                                            
                            
                    if(flag==0):
                        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
                        print("         Check your username or password")
                        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
                        
                elif(choice2==0):
                    break