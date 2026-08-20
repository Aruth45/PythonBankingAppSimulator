import random
from secondary import users_DB



def main():
    add_user, get_user, login, logout, show_balance, make_deposit, withdraw_money, view_accounts = users_DB()
    is_running_main = True
    while is_running_main:
        print("*"*30)
        print("1. Create user\n" 
        "2. Login\n" 
        "3. Exit")
        print("*"*30)
        user_choice_main = input("Please select an option from the menu above: ")
        match user_choice_main:
            case "1":
                username = input("Please enter your username: ").replace(' ', '')
                password = input("Please enter your passowrd: ").replace(' ', '')
                add_user({
                    "username": username,
                    "password": password,
                    "id": random.randint(1000, 9999),
                    "accounts": [
                        {
                            "acct_number": random.randint(100_000_000, 999_999_999),
                            "balance": 0
                        }
                    ]
                })
            case "2":
                username = input("Please enter your username: ").replace(' ', '')
                password = input("Please enter your passowrd: ").replace(' ', '')
                try:
                    login(username, password)
                    is_user_loggedin = True
                    while is_user_loggedin:
                        print("*"*30)
                        print("1. View my balance\n" 
                         "2. Make deposit\n" 
                        "3. Withdraw money\n"
                        "4. View my accounts\n" 
                        "5. Logout")
                        print("*"*30)
                        user_choice_loggedin = input("Please choose an option from the menu above: ")
                        match user_choice_loggedin:
                            case "1":
                                try:
                                    account_number = input("Please enter the account number you would like to consult: ")
                                    print(show_balance(account_number))
                                except ValueError as error:
                                    print(error)
                            case "2":
                                try:
                                    acct_number = input("Please enter the account number for the deposit: ")
                                    deposit_amount = input("Please enter the amount to deposit: ")
                                    result = make_deposit(account_number=acct_number, amount=deposit_amount)
                                    print(result)
                                except ValueError as error:
                                    print(error)
                            case "3":
                                try:
                                    acct_number = input("Please enter the account number for the withdrawal: ")
                                    deposit_amount = input("Please enter the amount to deposit: ")
                                    result = withdraw_money(account_number=acct_number, amount=deposit_amount)
                                    print(result)
                                except ValueError as error:
                                    print(error)

                            case "4":
                                print(view_accounts())
                            case "5":
                                logout()
                                is_user_loggedin = False
                except ValueError as error:
                    print(error)
                
            case "3":
                is_running_main = False

main()
            

               
