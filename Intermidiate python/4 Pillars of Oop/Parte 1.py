class BankAccount:
    def __init__(self, balance=0):
        self.balance = float(balance)

    def deposit_money(self):
        amount = float(input("¿Cuánto dinero deseas depositar? "))
        self.balance += amount
        return self.balance

    def withdraw_money(self):
        amount = float(input("¿Cuánto dinero desea retirar? "))

        if self.balance < amount:
            print("Fondos insuficientes")
        else:
            self.balance -= amount

        return self.balance
    
class SavingsAccount(BankAccount):
    def __init__(self, min_balance=50, balance=0):
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw_money(self):
        amount = float(input("¿Cuánto dinero desea retirar? "))

        if self.balance - amount < self.min_balance:
            raise ValueError(
                f"El saldo no puede quedar por debajo de {self.min_balance}"
            )

        self.balance -= amount
        return self.balance
            