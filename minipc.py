import random
print("welcome to your mini terminal PC!")



def setpassword():
    createpass = ""
    while createpass == "":
        createpass = str(input("\nPlease set a password you will remember: "))
    return createpass

def login(password):
    pass_attempt = str
    while pass_attempt != password:
        pass_attempt = input("\nPlease enter your password: ")

    print("\nAccess granted, welcome to your desktop.")

def long_word():
    print("\nPneumonoultramicroscopicsilicovolcanoconiosis")

def homepage(password):

    
    while True:
        chooseapp = str.lower(input("what would you like to do?: \n Change your password (setpass)  \n Print a really long word (long) \n Log out of your mini PC (logout) \n A minigame of flipping a coin (coin) \n A calculator for converting numbers into 8 bit binary (calc)\n"))
        if chooseapp == "long":
            long_word()
            homepage(password)
        elif chooseapp == "setpass":
            password = setpassword()
            homepage(password)
        elif chooseapp == "logout":
            login(password)
            homepage(password)
        elif chooseapp == "coin":
            coin_toss()
            homepage(password)
        elif chooseapp == "calc":
            binary_calc()
            homepage(password)
        
            
            
#calls homepage() after every app so it can return to homepage

def coin_toss():
        
    choice = ""
    while choice != "heads" and choice != "tails":
        choice = str.lower(input("\nHeads or Tails?:\n"))

    flip = random.randint(1,2)

    if flip == 1:
        flip = "heads"
    else:
        flip = "tails"
    if choice == flip:
        print(f"\nThe coin landed on {flip}!, Congratulations you won!")
    else:
        print(f"\nThe coin landed on {flip}!, Sorry you lost!")

    replay = str.lower(input("\nWould you like to play again? (Y/N): "))
    
    while replay != "y" and replay != "n":
        replay = str.lower(input("\nWould you like to play again? (Y/N): "))

    if replay == "y":
        coin_toss()


    
def binary_calc():
    print("\nThis calculator will convert normal denary numbers into binary. This is a 16 bit computer meaning it can handle numbers up to 65,535.")
    denary_input = input("What number would you like to convert?: ")
    denary_int = 99999999999999
    binary_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    i = 1
    
    while True:
        try:
            denary_int = int(denary_input)
            
        except:
            denary_input = input("Please enter a valid number: ")
        else:
            break

    if denary_int > 65535:
        print("The calculator cannot display past the 65,535 limit.")
        denary_int = 65535
            
        
            
            

    while int(denary_int) > 0:
        current = int(denary_int) % 2
        denary_int -= current
        denary_int /= 2
        binary_list[-i] = int(current)
        i += 1

    print(binary_list)
    print("\n")

    


#every homepage is supplied with password to make the login/setpass functions work otherwise they cant access the externally stored password from within the function       

password = setpassword()

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
login(password)

homepage(password)



