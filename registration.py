import re
import hashlib
#============== Check Function =====================
def check_email(email):
    regex = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    # fullmatch --> because ---> check if all the string follows the pattern
    if re.fullmatch(regex,email):
        return True
    return False

#============== Register Function ==================
def register():
    
    while True:
        fname = input("please enter your first name : ")
        # validation
        if len(fname) == 0 :
            print("empty value")
            continue

        lname = input("please enter your last name : ")
        # validation
        if len(lname) == 0 :
            print("empty value")
            continue
        
        email = input("please enter your email : ")
         # validation
        if check_email(email) == True:
            print("Email : ",email)
        else:
            print("Invalid email")
            continue
  
        password = input("please enter your password : ")
        confirm_p = input("please confirm your password : ")
        # validation
        if confirm_p == password:
            enc = confirm_p.encode()
            # to encyrpt my password
            p_hash = hashlib.md5(enc).hexdigest()
            userinfo= f"{email}:{p_hash}:{fname}:{lname}"

            with open ("log.txt","a") as f:
                f.write(userinfo + "\n")
            print("You have registered successfully")
        else:
            print("You have error , please try again")
               
