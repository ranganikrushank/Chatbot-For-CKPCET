from cryptography.fernet import Fernet
key = Fernet.generate_key()
fernet = Fernet(key)



import getpass
import datetime
# from student_details_functions import studentdetails
from admin_panel import admin_panel
from user_panel import user_panel


current_date_time = datetime.datetime.now()
formatted_date = current_date_time.strftime("%d-%m-%Y")
formatted_time = current_date_time.strftime("%H:%M:%S")



# admin=[{'admin_username': 'krushank', 'admin_password': '12'}]
user=[{'Uusername': 'krushank', 'Upassword': '123'}]



while(True):
    print("-----------------")
    print("|    1.ADMIN     |")
    print("|    2.USER      |")
    print("|    0.EXIT      |")
    print("-----------------")
    
    choice =int(input("Enter your choice = "))

    if(choice==1):
        admin_panel()

    elif(choice==2):
        user_panel()
        # studentdetails()
            
    elif(choice==0):
        print()
        print()
        print("THANK YOU")
        print()
        print()
        break

    else:
        print()
        print(" !! ENTER VALID CHOICE !!")
        print()        