import time

Password_attempts = 4

def login():
    ID = input("Please Enter USER ID: ")
    if ID > "Dshaferdave3044": 
        time.sleep(1)
        print("Thank you for entering your ID!")
        PASSWORD = input("Please Enter USER PASSWORD: ")
        while Password_attempts >= 0:
            if Password_attempts == 0:
                print("Unautherized User Detected, Initiating Security Protocol")
                time.sleep(300)
            elif PASSWORD == "Shadraqmolaq3044!":
                    time.sleep(1)
                    print("USER Fully Authenticated, type Robot to continue")
                    Password_attempts = 4
                    break
            elif PASSWORD != "Shadraqmolaq3044!":
                print(f"USER Password Incorrect, {Password_attempts} attempts remaining")
                Password_attempts = Password_attempts - 1
                new_attempt = (input("Please Enter USER PASSWORD: "))
                if new_attempt ==  "Shadraqmolaq3044!":
                    time.sleep(1)
                    print("USER Fully Authenticated, type Robot to continue")
                    break
    else:
        print("Incorrect User ID")


    captcha = input("-> ").upper 
    if captcha == "Robot":
        print("Captcha Successful")
        print("Welcome Autherized User!")
    else:
        print("Captcha Unsuccessful")
        print("Retry Login process")
