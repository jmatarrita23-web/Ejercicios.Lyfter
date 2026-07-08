import csv
from pathlib import Path

from models import Category, Transaction


class CsvStorage:
    def __init__(self, data_folder="data"):
        self.data_folder = Path(data_folder)
        self.categories_path = self.data_folder / "categories.csv"
        self.transactions_path = self.data_folder / "transactions.csv"
        self.category_headers = ["name"]
        self.transaction_headers = [
            "title",
            "amount",
            "category",
            "transaction_type",
            "date",
        ]

    def ensure_data_folder_exists(self):
        self.data_folder.mkdir(exist_ok=True)

    def save_categories(self, categories):
        self.ensure_data_folder_exists()
        rows = [category.to_row() for category in categories]
        self._save_csv(self.categories_path, self.category_headers, rows)

    def save_transactions(self, transactions):
        self.ensure_data_folder_exists()
        rows = [transaction.to_row() for transaction in transactions]
        self._save_csv(self.transactions_path, self.transaction_headers, rows)

    def load_categories(self):
        rows = self._load_csv(self.categories_path)
        return [Category.from_row(row) for row in rows]

    def load_transactions(self):
        rows = self._load_csv(self.transactions_path)
        return [Transaction.from_row(row) for row in rows]

    def save_all(self, categories, transactions):
        self.save_categories(categories)
        self.save_transactions(transactions)

    def _save_csv(self, path, headers, rows):
        with path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(rows)

    def _load_csv(self, path):
        if not path.exists():
            return []

        with path.open("r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)
