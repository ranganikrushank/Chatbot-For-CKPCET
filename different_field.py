import pandas as pd
from questions import computer_query
from questions import mechanical_query
from questions import electrical_query
from questions import civil_query


computer_faculties = pd.read_excel("Computer.xlsx")
civil_faculties = pd.read_excel("Civil.xlsx")
mechanical_faculties = pd.read_csv("mechanical.csv")
electrical_faculties = pd.read_excel("Electrical.xlsx")









def computer_department():
    print()
    print()
    print()
    print()
    print()
    print("                    WELCOME TO COMPUTER DEPARTMENT")
    print()
    print("Computer Engineering is NBA accredited and also it comes under GTU affilation. ")
    print("At present the computer engineering branch is most in demand.")
    print("Here we have most experienced faculties for Computer engineering department")
    print()
    print() 
    while(True):
        print("1. Solve Queries")
        print("2. Map")
        print("3. Faculties")
        print("0. Exit")
        print()
        computerselect=int(input("Enter your choice = "))
        print()
        if(computerselect==1):
            print()
            print("-------------------------------------------------------")
            print("    Enter your all questions to solve your queries")
            print("-------------------------------------------------------")
            computer_query()
            print()
            
        elif(computerselect==2):
            print()
            print("Click on the below given link to know ")
            print("the direction of our college")
            print()
            print("https://maps.app.goo.gl/i4Aumkf27bZcBNyb7")
        
        elif(computerselect==3):
            print()
            print()
            print("-------------------------------------------------------------------------------------------------------------------------")
            print("                                         COMPUTER DEPARTMENT FACULTIES")
            print("-------------------------------------------------------------------------------------------------------------------------")
            # print()
            print(computer_faculties)
            
            
        elif(computerselect==0):
            print()
            print("THANK YOU")
            print("HOPE YOUR ALL QUERIES ARE SOLVED")
            print()
            break
        
        else:
            print()
            print("!! ENTER VALID CHOICE !!")
            print()
            
            

# computer_department()












def civil_department():
    print()
    print()
    print()
    print()
    print()
    print("                    WELCOME TO CIVIL DEPARTMENT")
    print()
    print("Civil engineering department is under GTU affilation.")
    print("And its also NBA accredited")
    print("Here we have a very well experienced faculties which guides and prepares a very bet civil engineers.")
    print("In civil engineering department we have almost every fculty as PHD and with 15+ years of experience")
    print()
    print()
    while(True):
        print("1. Solve Queries")
        print("2. Map")
        print("3. Faculties")
        print("0. Exit")
        print()
        civilselect=int(input("Enter your choice = "))
        print()
        if(civilselect==1):
            print()
            print("-------------------------------------------------------")
            print("    Enter your all questions to solve your queries")
            print("-------------------------------------------------------")
            civil_query()
            print()
            
        elif(civilselect==2):
            print()
            print("Click on the below given link to know ")
            print("the direction of our college")
            print()
            print("https://maps.app.goo.gl/i4Aumkf27bZcBNyb7")
        
        elif(civilselect==3):
            print()
            print()
            print("-------------------------------------------------------------------------------------------------------------------------")
            print("                                         CIVIL DEPARTMENT FACULTIES")
            print("-------------------------------------------------------------------------------------------------------------------------")
            print()     
            print(civil_faculties)
            
            
        elif(civilselect==0):
            print()
            print("THANK YOU")
            print("HOPE YOUR ALL QUERIES ARE SOLVED")
            print()
            break
        
        else:
            print()
            print("!! ENTER VALID CHOICE !!")
            print()
            
            
            



def mechanical_department():
    print()
    print()
    print()
    print()
    print()
    print("                    WELCOME TO MECHANICAL DEPARTMENT")
    print()
    print("Mechanical engineering department is under GTU affilation.")
    print("And its also NBA accredited")
    print("Here we have a very well experienced faculties which guides and prepares a very bet civil engineers.")
    print("In Mechanical engineering department we have almost every faculty as PHD and with 15+ years of experience")
    print()
    print()
    while(True):
        print("1. Solve Queries")
        print("2. Map")
        print("3. Faculties")
        print("0. Exit")
        print()
        Mechanicalselect=int(input("Enter your choice = "))
        print()
        if(Mechanicalselect==1):
            print()
            print("-------------------------------------------------------")
            print("    Enter your all questions to solve your queries")
            print("-------------------------------------------------------")
            mechanical_query()
            print()
            
        elif(Mechanicalselect==2):
            print()
            print("Click on the below given link to know ")
            print("the direction of our college")
            print()
            print("https://maps.app.goo.gl/i4Aumkf27bZcBNyb7")
        
        elif(Mechanicalselect==3):
            print()
            print()
            print("-------------------------------------------------------------------------------------------------------------------------")
            print("                                         MECHANICAL DEPARTMENT FACULTIES")
            print("-------------------------------------------------------------------------------------------------------------------------")
            print()     
            print(mechanical_faculties)
            
            
        elif(Mechanicalselect==0):
            print()
            print("THANK YOU")
            print("HOPE YOUR ALL QUERIES ARE SOLVED")
            print()
            break
        
        else:
            print()
            print("!! ENTER VALID CHOICE !!")
            print()
            
            
            
            
            
            
            
            
            
            
            
def electrical_department():
    print()
    print()
    print()
    print()
    print()
    print("                    WELCOME TO ELECTRICAL DEPARTMENT")
    print()
    print("Electrical engineering department is under GTU affilation.")
    print("And its also NBA accredited")
    print("Here we have a very well experienced faculties which guides and prepares a very bet electrical engineers.")
    print("In electrical engineering department we have almost every faculty as PHD and with 15+ years of experience")
    print()
    print()
    while(True):
        print("1. Solve Queries")
        print("2. Map")
        print("3. Faculties")
        print("0. Exit")
        print()
        electricalselect=int(input("Enter your choice = "))
        print()
        if(electricalselect==1):
            print()
            print("-------------------------------------------------------")
            print("    Enter your all questions to solve your queries")
            print("-------------------------------------------------------")
            electrical_query()
            print()
            
        elif(electricalselect==2):
            print()
            print("Click on the below given link to know ")
            print("the direction of our college")
            print()
            print("https://maps.app.goo.gl/i4Aumkf27bZcBNyb7")
        
        elif(electricalselect==3):
            print()
            print()
            print("-------------------------------------------------------------------------------------------------------------------------")
            print("                                         MECHANICAL DEPARTMENT FACULTIES")
            print("-------------------------------------------------------------------------------------------------------------------------")
            print()     
            print(electrical_faculties)
            
            
        elif(electricalselect==0):
            print()
            print("THANK YOU")
            print("HOPE YOUR ALL QUERIES ARE SOLVED")
            print()
            break
        
        else:
            print()
            print("!! ENTER VALID CHOICE !!")
            print()