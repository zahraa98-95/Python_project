import hashlib
import create_project
import view_projects
import edit_project
import delete_project
#============== login Function ===================
 
def login():
    email = input("please enter your email : ")
    password = input("please enter your password : ")
    auth = password.encode()
    a_hash = hashlib.md5(auth).hexdigest()
    with open("log.txt", "r") as f:
        users=f.readlines()
        for u in users :
            userinfo = u.strip("\n")
 
            userinfo=userinfo.split(":")
            if userinfo[0] == email and userinfo[1] == a_hash:
                print("Logged in Successfully!")
                # project_menu
                while True:
                    choice = int(input("""
                    1.create a project
                    2.view all projects
                    3.edit project
                    4.delete project
                    5.exit
                    """))
                    if choice == 1:
                        create_project.create()
                        
                    elif choice == 2:
                        view_projects.view_all_projects()
                        # print("view")
                    elif choice == 3:
                        edit_project.edit_project()
                        # print("edite")
                    elif choice == 4:
                        # print("delete")
                        delete_project.delete_project()
                    elif choice == 5:
                        exit()
            else:
                continue
                # print("Login failed \n")
                

