import math

def is_number(number: int | float) -> bool:
    try:
        return math.isfinite(float(number))
    except ValueError:
        return False


def users_DB():
    users = []
    active_user = None

    def add_user(user: dict):
        users.append(user)

    def get_user(id: int):
        for user in users:
            if user['id'] == id:
                return {
                    key:value
                    for key, value in user.items()
                    if key != 'password'
                }
        return None


    def login(username: str, password: str):
        nonlocal active_user
        for user in users:
            if user['username'] == username and user['password'] == password:
                active_user = user
                return 
        raise ValueError("The credentials are incorrect. Please try again.")
        

    def logout():
        nonlocal active_user
        active_user = None

    def view_accounts():
        accounts = []
        for account in active_user['accounts']:
            accounts.append(
                f"1. Accont number: {account['acct_number']}\n"
                f"2. Balance: {account['balance']}"
            )

        return "\n------------------------------------\n".join(accounts)

    def show_balance(account_number: str) -> str:
        for account in active_user['accounts']:
            if account['acct_number']  == int(account_number):
                return (f"Account number: {account['acct_number']}\n"
                        f"Balance: {account['balance']}") 
    
        raise ValueError("The account was not found. Please try again.")  

    def make_deposit(amount: int | float, account_number: int):
        nonlocal active_user
        if is_number(amount) and is_number(account_number):
            deposit_amount = float(amount)
            for account in active_user['accounts']:
                    if account['acct_number'] == int(account_number):
                        if deposit_amount <= 0:
                            raise ValueError("The amount cannot be lower or equal to zero.")
                        else:
                            account['balance'] += deposit_amount
                            return show_balance(account_number)       
            raise ValueError("The account was not found. Please try again.")
        else:
            raise ValueError("Only numbers are allowed. Please enteder a valid amount.")

    def withdraw_money(amount: int | float, account_number: int):
        nonlocal active_user
        if is_number(amount) and is_number(account_number):
            deposit_amount = float(amount)
            for account in active_user['accounts']:
                    if account['acct_number'] == int(account_number):
                        if deposit_amount <= 0:
                            raise ValueError("The amount cannot be lower or equal to zero.")
                        elif deposit_amount > account['balance']:
                            raise ValueError("The amount cannot be greater than this account's current balance.")
                        else:
                            account['balance'] -= deposit_amount
                            return show_balance(account_number)
            raise ValueError("The account was not found. Please try again.")
        else:
            raise ValueError("Only numbers are allowed. Please enteder a valid amount.")

    return add_user, get_user, login, logout, show_balance, make_deposit, withdraw_money, view_accounts


