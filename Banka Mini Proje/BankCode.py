import os

savedUsers = {"Kadir":{"password":"22","money":32}}

while True:
    os.system('cls')
    print("Welcome to the Bank System!")
    print("")

    name = input("Username: ")
    password = input("Password: ")

    def checkUser(name,password):
        def CreateNewUser():
            answer = input("No user found with that name! Do you want to create a new User ? (Y/N)")

            if(answer == "Y"):
                job = input("Job: ")
                money = int(input("Money: "))
                savedUsers.update({name:{"password":password,"money":money,"job":job}})
                print(f"User Created ! Username: {name}, Password: {password}")
                input()

            else:
                print("Exited !")
        
        if(name in savedUsers.keys()): ##Bank System is here
            if(("password" , password) in savedUsers[name].items()):
                os.system('cls')
                print(f"Welcome {name}")

                print("Please choose which action do you want to do \n"
                      +"1-Deposit Money \n"
                      +"2-Withdraw Money \n"
                      +"3-Change Password")
                
                answer = input()
                if(answer == "1"):
                    depositMoney = int(input("How much you want to deposit ? \n"))
                    savedUsers[name]["money"] += depositMoney
                    print("Completed! Current Money : {} ".format(savedUsers[name]["money"]))
                    input()
                elif(answer == "2"):
                    while True:
                        withdrawMoney = int(input("How much you wanna withdraw ? \n"))
                        if(withdrawMoney <= savedUsers[name]["money"]):
                            savedUsers[name]["money"] -= withdrawMoney
                            input("Withdraw Completed ! Current money : {}".format(savedUsers[name]["money"]))
                            break
                        else:
                            print("Sorry you dont have enough money for that try again !")
                elif(answer == "3"):
                    if(savedUsers[name]["password"] == input("Please enter current password: ")):
                        newPassword = input("Enter new password: ")
                        newPasswordCheck = input("Enter new password again: ")
                        if(newPassword == newPasswordCheck):
                            savedUsers[name]["password"] = newPassword
                            input("Password changed succesfully")
                        else:
                            input("The password must match with the other one !")
                    else:
                        input("Wrong password ! ")
            else:
                print("Wrong Password")
                input()        
        
        else: CreateNewUser()
   
    checkUser(name,password)
    print(savedUsers)