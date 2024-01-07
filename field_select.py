from different_field import computer_department
from different_field import civil_department
from different_field import mechanical_department
from different_field import electrical_department



def field_select():
    while(True):                            
        print()
        print("Please Select Your Intrested Field -- So that we can guide you respectively ")
        print()
        print("1. Computer Engineering")
        print("2. Electrical Engineering")
        print("3. Civil Engineering")
        print("4. Mechanical Engineering")
        print("0. Exit")
        print()
        print()
        fieldselect=int(input("Enter your Selected Field Number  = "))
        print()
        if(fieldselect==1):
            computer_department()
            
        elif(fieldselect==2):
            electrical_department()
            
        elif(fieldselect==3):
            civil_department()
        
        elif(fieldselect==4):
            mechanical_department()
            
        elif(fieldselect==0):
            print()
            print("THANK YOU")
            break
            print()
            
        else:
            print()
            print("!! ENTER VALID CHOICE !!")
            print()
            
            
# field_select()