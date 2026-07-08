from models import Category, Transaction
from storage import CsvStorage
from validation import validate_category_form, validate_transaction_form


class FinanceManager:
    def __init__(self, storage=None):
        self.storage = storage or CsvStorage()
        self.categories = []
        self.transactions = []
        self.load_data()

    def load_data(self):
        self.categories = self.storage.load_categories()
        self.transactions = self.storage.load_transactions()

    def save_data(self):
        self.storage.save_all(self.categories, self.transactions)

    def add_category(self, name):
        clean_name = name.strip()
        is_valid, message = validate_category_form(clean_name, self.categories)
        if not is_valid:
            return False, message

        self.categories.append(Category(name=clean_name))
        self.save_data()
        return True, "Categoria agregada correctamente."

    def add_transaction(self, title, amount, category, transaction_type):
        if not self.categories:
            return False, "Debe agregar al menos una categoria antes de registrar movimientos."

        is_valid, message = validate_transaction_form(title, amount, category)
        if not is_valid:
            return False, message

        transaction = Transaction.create(
            title=title.strip(),
            amount=amount,
            category=category,
            transaction_type=transaction_type,
        )
        self.transactions.append(transaction)
        self.save_data()
        return True, f"{self.get_transaction_type_label(transaction_type)} agregado correctamente."

    def add_expense(self, title, amount, category):
        return self.add_transaction(title, amount, category, "expense")

    def add_income(self, title, amount, category):
        return self.add_transaction(title, amount, category, "income")

    def get_category_names(self):
        return [category.name for category in self.categories]

    def get_transaction_rows(self):
        return [
            [
                transaction.date,
                self.get_transaction_type_label(transaction.transaction_type),
                transaction.title,
                f"{transaction.amount:.2f}",
                transaction.category,
            ]
            for transaction in self.transactions
        ]

    def get_transaction_type_label(self, transaction_type):
        labels = {
            "expense": "Gasto",
            "income": "Ingreso",
        }
        return labels.get(transaction_type, transaction_type.capitalize())

    def calculate_total_income(self):
        return sum(
            transaction.amount
            for transaction in self.transactions
            if transaction.transaction_type == "income"
        )

    def calculate_total_expenses(self):
        return sum(
            transaction.amount
            for transaction in self.transactions
            if transaction.transaction_type == "expense"
        )

    def calculate_balance(self):
        return self.calculate_total_income() - self.calculate_total_expenses()
