from datetime import datetime


class Category:
    def __init__(self, name):
        if not name or not name.strip():
            raise ValueError("El nombre de la categoria es obligatorio.")
        self.name = name

    def to_row(self):
        return [self.name]

    @classmethod
    def from_row(cls, row):
        return cls(name=row["name"])


class Transaction:
    VALID_TRANSACTION_TYPES = ("income", "expense")

    def __init__(self, title, amount, category, transaction_type, date):
        if not title or not title.strip():
            raise ValueError("El titulo es obligatorio.")

        if not category or not category.strip():
            raise ValueError("La categoria es obligatoria.")

        if transaction_type not in self.VALID_TRANSACTION_TYPES:
            raise ValueError("El tipo de movimiento no es valido.")

        numeric_amount = float(amount)
        if numeric_amount <= 0:
            raise ValueError("El monto debe ser mayor que cero.")

        self.title = title
        self.amount = numeric_amount
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
