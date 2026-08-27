from secondary import users_DB
import random

def main():
    (
    add_user, 
    login, 
    logout, 
    view_accounts, 
    create_account,
    delete_account, 
    show_balance, 
    make_deposit, 
    withdraw_money) = users_DB()

    is_main_running = True

    while is_main_running:
        print("*"*30)
        print("1. Create user\n"
            "2. Login\n" 
            "3. Exit")
        print("*"*30)
        user_choice_main = input("Please choose an option from the menu above: ")
        match user_choice_main:
            case "1": 
                username = input("Please enter your desired username: ")
                password = input("Please set a password: ")
                result = add_user({
                                    'username': username,
                                    'password': password,
                                    'accounts': [{
                                        'acct_number': random.randint(100_000_000,999_999_999),
                                        'balance': 0
                                    }] 
                                })
                print(result)
            case "2":
                username = input("Please enter your username: ")
                password = input("Please enter your password: ")
                try:
                    print(login(username=username, password=password))
                    is_user_loggedin = True
                    while is_user_loggedin:
                        print("*"*30)
                        print("1. View balance\n" 
                        "2. Make deposit\n" 
                        "3. Withdraw money\n"
                        "4. View my accounts\n" 
                        "5. Create an account\n"
                        "6. Delete an account\n"
                        "8. Logout")              
                        print("*"*30)
                        get_loggedin_user_choice = input("Please choose an option from the menu above: ")
                        match get_loggedin_user_choice:
                            case "1":
                                get_account_number = input("Please enter the account nuber you would like to see the balance for: ")
                                try:
                                    print(show_balance(get_account_number))
                                except ValueError as error:
                                    print(error)
                            case "2":
                                get_account_number_deposit = input("Please enter the account number where the money should be deposited: ")
                                deposit_amount = input("Please enter the amount you would like to deposit: ")
                                try:
                                    print(make_deposit(account_number=get_account_number_deposit, amount=deposit_amount))
                                except ValueError as error:
                                    print(error)
                            case "3":
                                get_account_number_withdrawal = input("Please enter the account number from where the funds should be taken: ")
                                withdraw_amount = input("Please enter the amount you would like to withdraw: ")
                                try:
                                    print(withdraw_money(account_number=get_account_number_withdrawal, amount=withdraw_amount))
                                except ValueError as error:
                                    print(error)
                            case "4":
                                try:
                                    print(view_accounts())
                                except ValueError as error:
                                    print(error)
                            case "5":
                                print(create_account())
                            case "6":
                                get_account_number_delete = input("Please enter the account number you would like to delete: ")
                                try:
                                    print(delete_account(get_account_number_delete))
                                except ValueError as error:
                                    print(error)
                            case "8":
                                is_user_loggedin = False
                                logout()
                except ValueError as error:
                    print(error)
            case "3":
                is_main_running = False

        

main()
        







