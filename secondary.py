import math, random

def is_number(number: str | int) -> bool:
    try:
        return math.isfinite(float(number))
    except ValueError:
        return False


def users_DB():
    users = []
    active_user = None

    def add_user(user: dict):
        users.append(user)
        return "The user was created successfully"

    def login(username: str, password: str):
        nonlocal active_user
        for user in users:
            if user['username'] == username and user['password'] == password:
                active_user = user
                return "Login successful"
        raise ValueError("Your credentials are incorrect. Please try again.")

    def logout():
        nonlocal active_user
        active_user = None

    def view_accounts() -> str:
        counter = 0
        accounts = []
        if len(active_user['accounts']) != 0:
            for account in active_user['accounts']:
                counter += 1
                accounts.append(f"{counter}. {account['acct_number']}")
            output = "\n".join(accounts)
            return output
        raise ValueError("You have no active accounts. Please create an account to enable this functionality.")

    def create_account() -> str:
        active_user['accounts'].append({
            'acct_number': random.randint(100_000_000,999_999_999),
            'balance': 0
        })

        output = ("Detalles de la nueva cuenta:\n"
                    f"{active_user['accounts'][-1]['acct_number']}")
        return output
    
    def delete_account(account_number:int) -> str:
        if is_number(account_number):
            if len(active_user['accounts']) != 0:
                for account in active_user['accounts']:
                    if account['acct_number'] == int(account_number):
                        if account['balance'] == 0:
                            active_user['accounts'].remove(account)
                            return "The account was eliminated successfully."
                        raise ValueError("This account still has balance and cannot be deleted.")
                raise ValueError("The account was not found. Please check the account number and try again.")
            raise ValueError("You have no active accounts. Please create an account to enable this functionality.")
        raise ValueError("Only numbers are allowed. Please check the account number again.")        
        
    def show_balance(account_number: int) -> str:
        if is_number(account_number):
            if len(active_user['accounts']) != 0:
                for account in active_user['accounts']:
                    if account['acct_number'] == int(account_number):
                        return f"${account['balance']:.2f}"
                raise ValueError("The account was not found. Please check the account number and try again.")
            raise ValueError("You have no active accounts. Please create an account to enable this functionality.")
        raise ValueError("Only numbers are allowed. Please check the account number again.")

    def make_deposit(amount: int | float, account_number: int) -> str:
        if is_number(amount) and is_number(account_number):
            if len( active_user['accounts']) != 0:
                if float(amount) > 0: 
                    for account in active_user['accounts']:
                        if account['acct_number'] == int(account_number):
                            account['balance'] += float(amount)
                            return show_balance(account_number)
                    raise ValueError("The account was not found. Please check the account number and try again.")
                raise ValueError("The deposit amount must greater than zero. Please try again.")
            raise ValueError("You have no active accounts. Please create an account to enable this functionality.")
        raise ValueError("Only numbers are allowed. Please check the account number again.")

    def withdraw_money(amount:int | float, account_number: int):
        if is_number(amount) and is_number(account_number):
            if len(active_user['accounts']) != 0:
                if float(amount) > 0:
                    for account in active_user['accounts']:
                        if account['acct_number'] == int(account_number):
                            if float(amount) <= account['balance']:
                                account['balance'] -= float(amount)
                                return show_balance(account_number)
                            raise ValueError("There is no sufficient balance in this account to complete your withdrawal request.")
                    raise ValueError("The account was not found. Please check the account number and try again.")
                raise ValueError("The deposit amount must greater than zero. Please try again.")
            raise ValueError("You have no active accounts. Please create an account to enable this functionality.")
        raise ValueError("Only numbers are allowed. Please check the account number again.")
    
    return add_user, login, logout, view_accounts, create_account, delete_account, show_balance, make_deposit, withdraw_money

    
                        
                

        
        







                
            
       
            


    



        



