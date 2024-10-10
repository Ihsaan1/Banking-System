print("*******WELCOME TO OUR BANK*******")

user_name = input(("Please enter your name: "))

balance = 1000
op = True

while op: #student completes while loop
    print("\n\n Choose 1 for Deposit \n Choose 2 for Withdraw \n Choose 3 for Check Balance \n Choose Q or q to Exit: ")
    choice = input("Please choose transactions:")

    if choice == "1": #user chooses 'deposit'
         #student completes while loop
         user_deposit = int(input('enter the amount you would like to deposit: '))
         balance = balance + user_deposit
        
    elif choice == "2":
       #student completes while loop
       user_withdraw = int(input('enter the amount you would like to withdraw: '))

       if user_withdraw > balance:
           print('It is not possible to withdraw beyond the account balance.')
       else:
           balance = balance - user_withdraw

           
       
    elif choice == "3":
        print(balance)
        #student does this part too
      
    elif choice == 'q' or 'Q':  #user chooses 'exit'
        print('Quitting...')
        break


        print("""
    -------------------------------------
   | Thanks for choosing us as your bank |
   | Visit us again!                     |
    -------------------------------------
        """)
        op = False#student does this part too
    else:
        print("Wrong transaction! Try again.")
