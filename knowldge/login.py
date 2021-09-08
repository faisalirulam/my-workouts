def password_check(password):
    specialsym = ["@","#","&","*","$"]
    actual_password="faisal@123"    
    if len(password)<6:
        print("The length of the password is too small. It must contain 8 characers.")
    if len(password)>20:
        print("The length of the password is too large. It must be between 8-20 characters")
    if not any(char in specialsym for char in password):
        print("Password should contain atleast 1 special character like '@,#,&,$,*'.")
    if not any(char.isdigit() for char in password):
        print("Password must contain atleast 1 digit.")
    if not any(char.isalpha() for char in password):
        print("Password must contain at least 1 alphabet.")
    elif (password==actual_password):
        print("Welcome")
    else:
        print("Invalid Password!. Try again")



password = input("Enter your password:")
password_check(password)
