def studentdetails():
    
    student_details_list=[]
    print()
    print("-------------------------------------------------------------------------")
    print("        Please Enter your details to proceed with your queries")
    print("-------------------------------------------------------------------------")
    print()
    
    try:
        student_name=input("Enter your name = ")
    except ValueError:
        print("Only Alphabets are allowed")
        student_name=input("Enter your name = ")
        
        
    try:
        student_phone=int(input("Enter your phone number = "))
    except:
        print("Only Numbers are allowed taht also upto 10 digits")
        student_phone=int(input("Enter your phone number = "))
    
    
    student_email=input("Enter your email id = ")
    
    try:
        parents_name=input("Enter fathers name = ")
    except ValueError:
        print("Only Alphabets are allowed")
        parents_name=input("Enter fathers name = ")
        
    try:    
        parents_phone=int(input("Enter your parents phone number = "))
    except ValueError:
        print("Only Numbers are allowed taht also upto 10 digits")
        parents_phone=int(input("Enter your parents phone number = "))
    
    
    try:
        hsc_marks=int(input("Enter your 12th marks if got = "))
    except ValueError:
        print("Only Digits are allowed of only upto 2 Digits")
        hsc_marks=input("Enter your 12th marks if got = ")
        
        
    
    try:
        gujcet_marks=int(input("Enter your gujcet marks = "))
    except ValueError:
        print("Only Digits are allowed of only upto 2 Digits")
        gujcet_marks=input("Enter your gujcet marks = ")
        
        
        
    try:
        interested_field=input("Enter your interested field = ")
    except ValueError:
        print("Only Alphabets are allowed")
        interested_field=input("Enter your interested field = ")
        
    print()

    student_details_set={}

    student_details_set["Student_name"]=student_name
    student_details_set["Student_phone_number"]=student_phone
    student_details_set["Student_email_id"]=student_email
    student_details_set["Parents_name"]=parents_name
    student_details_set["Parents_phone"]=parents_phone
    # student_details_set["Parents_emailid"]=parents_emailid
    student_details_set["hsc_marks"]=hsc_marks
    student_details_set["gujcet_marks"]=gujcet_marks
    student_details_set["interested_field"]=interested_field

    student_details_list.append(student_details_set)

    print("-------------------------------------------------------------------------")
    print("                  PLEASE CHECK YOUR ENTERED DETAILS ")
    print("-------------------------------------------------------------------------")

    print("        Your First Name              :- ",student_name)
    print("        Student's Phone Number       :- ",student_phone)
    print("        Studnet's Email              :- ",student_email)
    print("        Parents Name                 :- ",parents_name)
    print("        Parent's Phone Number        :- ",parents_phone)
    print("        Student's 12 Percentage      :- ",hsc_marks)
    print("        Student's GUJCET Marks       :- ",gujcet_marks)
    print("        Student's Interested Field   :- ",interested_field)
    print("------------------------------------------------------------------")
    # print(student_details_list)
    
    
    
# studentdetails()