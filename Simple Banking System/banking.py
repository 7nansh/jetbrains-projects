import random
import math
import sqlite3


class Bank:

    def __init__(self):
        self.current_account = dict()
        self.exit = False
        self.conn = sqlite3.connect("card.s3db")
        self.cur = self.conn.cursor()
        self.table_exists = self.cur.execute("""
            SELECT name FROM sqlite_master WHERE type='table' AND name='card';
        """).fetchone()
        if self.table_exists is None:
            self.cur.execute("""
                create table card (
                     id INTEGER,
                     number TEXT,
                     pin TEXT,
                     balance INTEGER
                 );
            """)
            self.conn.commit()
        while not self.exit:
            self.main_menu()

    def main_menu(self):
        print("1. Create an account")
        print("2. Log into account")
        print("0. Exit")
        option = input()
        if option == "1":
            self.create_account()
        elif option == "2":
            self.login_to_account()
        else:
            self.bye()

    def create_account(self):
        account = dict()
        account["card_num"] = "400000" + "".join(random.sample("0123456789", 9))
        account["card_num"] = [int(i) for i in account["card_num"]]
        card_num_idx = [i if i % 2 == 0 else i for i in range(len(account["card_num"]))]
        calc_card_num = [account["card_num"][i]*2 if i % 2 == 0 else account["card_num"][i] for i in card_num_idx]
        calc_card_num = [i-9 if i > 9 else i for i in calc_card_num]
        sum_of_card_num = sum(calc_card_num)
        account["card_num"].append((int(math.ceil(sum_of_card_num / 10.0)) * 10) - sum_of_card_num)
        account["card_num"] = [str(i) for i in account["card_num"]]
        account["card_num"] = "".join(account["card_num"])
        account["PIN"] = "".join(random.sample("123456789", 4))
        account["balance"] = 0
        self.current_account = account
        self.cur.execute(f"insert into card values\
         ({int(account['card_num'])}, {account['card_num']}, {account['PIN']},{account['balance']})")
        self.conn.commit()
        print("\nYour card has been created")
        print("Your card number:")
        print(account["card_num"])
        print("Your card PIN:")
        print(f"{account['PIN']}\n")
        self.main_menu()

    def login_to_account(self):
        logged_in_account = dict()
        print("\nEnter your card number:")
        card_num = input()
        get_account = self.get_account_from_database(card_num)
        if get_account is not None:
            logged_in_account = self.map_account_to_current_account(*get_account)
        print("Enter your PIN:")
        pin_num = input()
        if not logged_in_account:
            print("\nWrong card number or PIN!\n")
            self.main_menu()
        if logged_in_account:
            if logged_in_account["PIN"] == pin_num:
                print("\nYou have successfully logged in!\n")
                self.logged_in_menu(logged_in_account)
            else:
                print("\nWrong card number or PIN!\n")
                self.main_menu()

    def logged_in_menu(self, logged_in_account):
        self.map_account_to_current_account(*self.get_account_from_database(logged_in_account["card_num"]))
        print("1. Balance")
        print("2. Add income")
        print("3. Do transfer")
        print("4. Close account")
        print("5. Log out")
        print("0. Exit")
        option = input()
        if option == "1":
            print(f"\nBalance: {logged_in_account['balance']}\n")
            self.logged_in_menu(logged_in_account)
        elif option == "2":
            print("\nEnter income:")
            amount = int(input())
            amount += self.current_account["balance"]
            self.add_income(amount, self.current_account["card_num"])
            print("Income was added!\n")
            self.logged_in_menu(self.current_account)
        elif option == "3":
            self.do_transfer()
            self.logged_in_menu(self.current_account)
        elif option == "4":
            self.cur.execute(f"DELETE FROM card WHERE number={self.current_account['card_num']}")
            self.conn.commit()
            self.current_account = dict()
            print("\nThe account has been closed!\n")
            self.main_menu()
        elif option == "5":
            print("\nYou have successfully logged out!\n")
            self.current_account = dict()
            self.main_menu()
        elif option == "0":
            self.bye()

    def bye(self):
        print("\nBye!")
        exit(0)
        # self.exit = True

    def get_account_from_database(self, card_num):
        self.cur.execute(f"SELECT number, pin, balance FROM card WHERE number = {card_num}")
        account = self.cur.fetchone()
        return account

    def map_account_to_current_account(self, card_num, pin, balance):
        self.current_account["card_num"] = card_num
        self.current_account["PIN"] = pin
        self.current_account["balance"] = balance
        return self.current_account

    def add_income(self, amount, card_num):
        self.cur.execute(f"UPDATE card SET balance = {amount} WHERE number = {card_num}")
        self.conn.commit()

    def do_transfer(self):
        print("\nTransfer")
        print("Enter card number:")
        card_num = input()
        card_num_c = [int(ch) for ch in str(card_num)][::-1]
        transfer_to = self.get_account_from_database(card_num)
        if card_num == self.current_account["card_num"]:
            print("You can't transfer money to the same account!\n")
            self.logged_in_menu(self.current_account)
        elif (sum(card_num_c[0::2]) + sum(sum(divmod(d*2, 10)) for d in card_num_c[1::2])) % 10 != 0:
            print("Probably you made a mistake in the card number. Please try again!\n")
            self.logged_in_menu(self.current_account)
        elif transfer_to is None:
            print("Such a card does not exist.\n")
            self.logged_in_menu(self.current_account)
        else:
            print("Enter how much money you want to transfer:")
            amount = int(input())
            if amount > self.current_account["balance"]:
                print("Not enough money!\n")
                self.logged_in_menu(self.current_account)
            self.add_income(transfer_to[2] + amount, card_num)
            self.add_income(self.current_account["balance"] - amount, self.current_account["card_num"])
            print("Success!\n")
            self.logged_in_menu(self.current_account)


b = Bank()
