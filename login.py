username=[""]
password=[""]
while True:


    udata=int(input("Press 1 to Register or Press 2 To Login:>"))


    def createAccount():
        new_username=input("please enter email:>")
        new_password=input("please enter password:>")
        username[0]=new_username
        password[0]=new_password
        print("Your username is :>",username[0])
        print("Your password is :>",password[0])
        for i in range(len(username)):
            print("to check in username:",username[i])

    def login():

        while True:
            l_username = input("Login>>:Please enter email address:")
            l_password = input("Login>>: Please enter password:>")

            for i in range(len(username)):
                print("to check in username:",username[i])
                if username[i] == l_username:
                    for z in range(len(password)):
                        if password[z] == l_password:
                            print("You are loggin!")


            # if username[0] ==l_username  and password[0]==l_password:
            #     print("you are succefully log in")
            # else:
            #     print("Try agian:> \nYou have left to try!",5-(i+1))

            # i=i+1
            # if i==5:
            #     break

    if udata == 1:
        createAccount()

    else:
        login()
