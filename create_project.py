import time
# Create_project Function
def create():
    
    while True:
        title = input("Enter your title : ")
        # validation
        while title.isdigit() == True:
            print("Invaild Input, Please Enter your title again")
            title = input()
        details = input("Enter your details : ")
        # validation
        while details.isdigit() == True:
            print("Invaild Input, Please Enter your details again")
            details = input()
        total_target = input("Enter your total_target :")
        # validation
        while total_target.isdigit() == False:
            print("Invaild Input, Please Enter your total_target again")
            total_target = input()
        start_time = input("Enter your start time:")
        # validation
        try:
            start_time = time.strptime(start_time, '%m/%d/%y')
        except:
            print("Invaild input Please enter your start time again")
            start_time = input("Enter your start time :")
        end_time = input("Enter your end time :")
        # validation
        try:
            end_time = time.strptime(end_time, '%m/%d/%y')
        except:
            print("Invaild input Please enter your end time again")
            end_time = input("Enter your end time:")
        
        project_info= f"{title}:{details}:{total_target}:{start_time}:{end_time}"
        with open ("projects.txt","a") as f:
                f.write(project_info + "\n")

           