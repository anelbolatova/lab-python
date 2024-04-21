class BankAccount:
    def __init__(self, owner_name, account_number, balance=0):
        self._owner_name = owner_name
        self._account_number = account_number
        self._balance = balance

    def get_owner_name(self):
        return self._owner_name

    def set_owner_name(self, owner_name):
        self._owner_name = owner_name

    def get_account_number(self):
        return self._account_number

    def set_account_number(self, account_number):
        self._account_number = account_number

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            print("Недопустимое значение баланса. Баланс не может быть отрицательным.")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Депозит в размере {amount} успешно выполнен.")
        else:
            print("Неверная сумма для депозита.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Снятие средств в размере {amount} успешно выполнено.")
        else:
            print("Недостаточно средств на счете.")

    def __str__(self):
        return f"Имя владельца счета: {self._owner_name}\nНомер счета: {self._account_number}\nБаланс: {self._balance}"

    def __eq__(self, other):
        return self._balance == other.get_balance()

    def __lt__(self, other):
        return self._balance < other.get_balance()

    def __gt__(self, other):
        return self._balance > other.get_balance()

class SavingAccount(BankAccount):
    def __init__(self, owner_name, account_number, interest_rate, balance=0):
        super().__init__(owner_name, account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest_amount = self.balance * (self.interest_rate / 100)
        self.balance += interest_amount
        print(f"Проценты в размере {interest_amount} добавлены к счету.")

account = BankAccount('Anel', '123456789', 5000)
account.deposit(500)
account.withdraw(1000)
print(account.__lt__(BankAccount('Assel', '123456987', 9000)))