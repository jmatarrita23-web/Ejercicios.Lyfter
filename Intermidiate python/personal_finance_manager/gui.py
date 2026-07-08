import FreeSimpleGUI as sg

from finance_manager import FinanceManager


class FinanceManagerGUI:
    def __init__(self):
        sg.theme("LightBlue2")
        self.finance_manager = FinanceManager()
        self.window = self.create_main_window()

    def create_main_window(self):
        table_headings = ["Fecha", "Tipo", "Titulo", "Monto", "Categoria"]
        layout = [
            [sg.Text("Gestor de Finanzas Personales", font=("Arial", 18, "bold"))],
            [
                sg.Table(
                    values=self.finance_manager.get_transaction_rows(),
                    headings=table_headings,
                    key="-TRANSACTIONS_TABLE-",
                    auto_size_columns=False,
                    col_widths=[18, 10, 22, 10, 18],
                    justification="left",
                    num_rows=10,
                    expand_x=True,
                    expand_y=True,
                )
            ],
            [
                sg.Text("Ingresos: Q0.00", key="-TOTAL_INCOME-", size=(18, 1)),
                sg.Text("Gastos: Q0.00", key="-TOTAL_EXPENSES-", size=(18, 1)),
                sg.Text("Balance: Q0.00", key="-BALANCE-", size=(18, 1)),
            ],
            [
                sg.Button("Agregar categoria"),
                sg.Button("Agregar gasto"),
                sg.Button("Agregar ingreso"),
                sg.Button("Salir"),
            ],
        ]
        window = sg.Window("Gestor de Finanzas Personales", layout, finalize=True, resizable=True)
        self.update_summary(window)
        return window

    def run(self):
        while True:
            event, _ = self.window.read()

            if event in (sg.WIN_CLOSED, "Salir"):
                self.finance_manager.save_data()
                break

            if event == "Agregar categoria":
                self.open_category_window()
            elif event == "Agregar gasto":
                self.open_transaction_window("expense")
            elif event == "Agregar ingreso":
                self.open_transaction_window("income")

        self.window.close()

    def open_category_window(self):
        layout = [
            [sg.Text("Nombre de la categoria")],
            [sg.Input(key="-CATEGORY-", size=(30, 1))],
            [sg.Button("Guardar"), sg.Button("Cancelar")],
        ]
        category_window = sg.Window("Agregar categoria", layout, modal=True)

        while True:
            event, values = category_window.read()
            if event in (sg.WIN_CLOSED, "Cancelar"):
                break

            if event == "Guardar":
                success, message = self.finance_manager.add_category(values["-CATEGORY-"])
                if success:
                    sg.popup(message, title="Exito")
                    self.update_table()
                    break
                sg.popup_error(message, title="Error")

        category_window.close()

    def open_transaction_window(self, transaction_type):
        if not self.finance_manager.categories:
            sg.popup_error(
                "No hay categorias disponibles. Agregue una categoria antes de registrar movimientos.",
                title="Error",
            )
            return

        window_title = "Agregar gasto" if transaction_type == "expense" else "Agregar ingreso"
        category_names = self.finance_manager.get_category_names()
        layout = [
            [sg.Text("Titulo")],
            [sg.Input(key="-TITLE-", size=(35, 1))],
            [sg.Text("Monto")],
            [sg.Input(key="-AMOUNT-", size=(20, 1))],
            [sg.Text("Categoria")],
            [sg.Combo(category_names, key="-CATEGORY-", readonly=True, size=(30, 1))],
            [sg.Button("Guardar"), sg.Button("Cancelar")],
        ]
        transaction_window = sg.Window(window_title, layout, modal=True)

        while True:
            event, values = transaction_window.read()
            if event in (sg.WIN_CLOSED, "Cancelar"):
                break

            if event == "Guardar":
                success, message = self.finance_manager.add_transaction(
                    values["-TITLE-"],
                    values["-AMOUNT-"],
                    values["-CATEGORY-"],
                    transaction_type,
                )
                if success:
                    sg.popup(message, title="Exito")
                    self.update_table()
                    break
                sg.popup_error(message, title="Error")

        transaction_window.close()

    def update_table(self):
        self.window["-TRANSACTIONS_TABLE-"].update(
            values=self.finance_manager.get_transaction_rows()
        )
        self.update_summary(self.window)

    def update_summary(self, window):
        window["-TOTAL_INCOME-"].update(
            f"Ingresos: Q{self.finance_manager.calculate_total_income():.2f}"
        )
        window["-TOTAL_EXPENSES-"].update(
            f"Gastos: Q{self.finance_manager.calculate_total_expenses():.2f}"
        )
        window["-BALANCE-"].update(
            f"Balance: Q{self.finance_manager.calculate_balance():.2f}"
        )
