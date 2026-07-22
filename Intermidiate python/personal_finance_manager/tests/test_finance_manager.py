import tempfile
import unittest

from finance_manager import FinanceManager
from models import Category, Transaction
from storage import CsvStorage, StorageError
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

    def test_rejects_non_numeric_amount(self):
        finance_manager, temporary_folder = self.create_temporary_manager()
        with temporary_folder:
            finance_manager.add_category("General")

            success, message = finance_manager.add_income("Pago", "abc", "General")

            self.assertFalse(success)
            self.assertIn("numero valido", message)

    def test_rejects_transaction_without_title(self):
        finance_manager, temporary_folder = self.create_temporary_manager()
        with temporary_folder:
            finance_manager.add_category("General")

            success, message = finance_manager.add_expense("", "25", "General")

            self.assertFalse(success)
            self.assertIn("titulo", message)

    def test_rejects_transaction_without_category(self):
        finance_manager, temporary_folder = self.create_temporary_manager()
        with temporary_folder:
            finance_manager.add_category("General")

            success, message = finance_manager.add_expense("Compra", "25", "")

            self.assertFalse(success)
            self.assertIn("categoria", message)

    def test_rejects_transaction_with_unknown_category(self):
        finance_manager, temporary_folder = self.create_temporary_manager()
        with temporary_folder:
            finance_manager.add_category("General")

            success, message = finance_manager.add_expense("Compra", "25", "Fantasma")

            self.assertFalse(success)
            self.assertIn("no existe", message)

    def test_storage_saves_and_loads_categories_directly(self):
        temporary_folder = tempfile.TemporaryDirectory()
        with temporary_folder:
            storage = CsvStorage(temporary_folder.name)

            storage.save_categories([Category("Servicios")])
            loaded_categories = storage.load_categories()

            self.assertEqual(["Servicios"], [category.name for category in loaded_categories])

    def test_storage_rejects_categories_file_with_wrong_headers(self):
        temporary_folder = tempfile.TemporaryDirectory()
        with temporary_folder:
            storage = CsvStorage(temporary_folder.name)
            storage.ensure_data_folder_exists()
            storage.categories_path.write_text("wrong\nComida\n", encoding="utf-8")

            with self.assertRaises(StorageError):
                storage.load_categories()

    def test_transaction_rejects_invalid_transaction_type(self):
        with self.assertRaises(ValueError):
            Transaction("Pago", "10", "General", "transfer", "2026-07-11 10:00")


if __name__ == "__main__":
    unittest.main()
