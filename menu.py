import registration
import login
# my first menu 
def menu():
    while True:
        print("Welcome To Our Application")

        choice = int(input("""
        1- Register
        2- Log in
        3- Exit
        """))

        if choice == 1:
            registration.register()
            
        elif choice == 2:
            login.login()
        elif choice == 3:
            exit()



menu()