from datetime import datetime


class Category:
    def __init__(self, name):
        self.name = name

    def to_row(self):
        return [self.name]

    @classmethod
    def from_row(cls, row):
        return cls(name=row["name"])


class Transaction:
    def __init__(self, title, amount, category, transaction_type, date):
        self.title = title
        self.amount = float(amount)
        self.category = category
        self.transaction_type = transaction_type
        self.date = date

    @classmethod
    def create(cls, title, amount, category, transaction_type):
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        return cls(
            title=title,
            amount=amount,
            category=category,
            transaction_type=transaction_type,
            date=current_date,
        )

    def to_row(self):
        return [
            self.title,
            f"{self.amount:.2f}",
            self.category,
            self.transaction_type,
            self.date,
        ]

    @classmethod
    def from_row(cls, row):
        return cls(
            title=row["title"],
            amount=row["amount"],
            category=row["category"],
            transaction_type=row["transaction_type"],
            date=row["date"],
        )
