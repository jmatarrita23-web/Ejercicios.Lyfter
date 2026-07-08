import tempfile
import unittest

from finance_manager import FinanceManager
from storage import CsvStorage
from validation import validate_amount


class FinanceManagerTests(unittest.TestCase):
    def create_temporary_manager(self):
        temporary_folder = tempfile.TemporaryDirectory()
        storage = CsvStorage(temporary_folder.name)
        finance_manager = FinanceManager(storage)
        return finance_manager, temporary_folder

    def test_add_category(self):
        finance_manager, temporary_folder = self.create_temporary_manager()
        with temporary_folder:
            success, _ = finance_manager.add_category("Comida")

            self.assertTrue(success)
            self.assertEqual(["Comida"], finance_manager.get_category_names())

    def test_rejects_duplicate_category(self):
        finance_manager, temporary_folder = self.create_temporary_manager()
        with temporary_folder:
            finance_manager.add_category("Comida")
            success, message = finance_manager.add_category("comida")

            self.assertFalse(success)
            self.assertIn("ya existe", message)

    def test_rejects_transaction_without_categories(self):
        finance_manager, temporary_folder = self.create_temporary_manager()
        with temporary_folder:
            success, message = finance_manager.add_expense("Almuerzo", "35", "Comida")

            self.assertFalse(success)
            self.assertIn("categoria", message)

    def test_calculates_balance(self):
        finance_manager, temporary_folder = self.create_temporary_manager()
        with temporary_folder:
            finance_manager.add_category("General")
            finance_manager.add_income("Salario", "1000", "General")
            finance_manager.add_expense("Compra", "125.50", "General")

            self.assertEqual(874.50, finance_manager.calculate_balance())

    def test_loads_saved_csv_data(self):
        temporary_folder = tempfile.TemporaryDirectory()
        with temporary_folder:
            first_manager = FinanceManager(CsvStorage(temporary_folder.name))
            first_manager.add_category("Trabajo")
            first_manager.add_income("Pago", "500", "Trabajo")

            second_manager = FinanceManager(CsvStorage(temporary_folder.name))

            self.assertEqual(["Trabajo"], second_manager.get_category_names())
            self.assertEqual(500.00, second_manager.calculate_total_income())

    def test_rejects_invalid_amount(self):
        success, message = validate_amount("-10")

        self.assertFalse(success)
        self.assertIn("mayor que cero", message)


if __name__ == "__main__":
    unittest.main()
