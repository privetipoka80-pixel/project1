import json
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QLabel, QTableWidget,
                             QTableWidgetItem, QPushButton,
                             QHBoxLayout, QComboBox)
from PyQt6.QtCore import Qt
from const.constans import PHYSICS_CONSTANTS, PHYSICS_UNITS


class HistoryDialog(QDialog):
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db
        self.setWindowTitle("История вычислений")
        self.setFixedSize(600, 400)

        layout = QVBoxLayout()

        # таблица
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(
            ["Формула", "Входные данные", "Результат", "Время"])
        self.table.horizontalHeader().setStretchLastSection(True)
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_history()

    def load_history(self):
        """Загружаем историю в таблицу"""
        history = self.db.get_history()
        self.table.setRowCount(len(history))

        for row, record in enumerate(history):
            id, formula_name, inputs_json, result, timestamp = record
            inputs = json.loads(inputs_json)  # преобразуем обратно из JSON

            # форматируем входные данные в красивую строку
            inputs_str = ", ".join([f"{k} = {v}" for k, v in inputs.items()])

            self.table.setItem(row, 0, QTableWidgetItem(formula_name))
            self.table.setItem(row, 1, QTableWidgetItem(inputs_str))
            self.table.setItem(row, 2, QTableWidgetItem(result))
            self.table.setItem(row, 3, QTableWidgetItem(timestamp))

        self.table.resizeColumnsToContents()


class ConstantsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Физические постоянные")
        self.setFixedSize(700, 500)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        title = QLabel("Физические постоянные")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        self.constants_table = QTableWidget()
        self.constants_table.setColumnCount(4)
        self.constants_table.setHorizontalHeaderLabels(
            ["Константа", "Значение", "Единица", "Описание"])
        self.constants_table.horizontalHeader().setStretchLastSection(True)

        layout.addWidget(self.constants_table)

        # Кнопка закрытия
        close_btn = QPushButton("Закрыть")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)

        self.setLayout(layout)

        # заполняем таблицу
        self.fill_constants_table()

    def fill_constants_table(self):
        row = 0
        for category, constants in PHYSICS_CONSTANTS.items():
            # добавляем строку с категорией
            self.constants_table.insertRow(row)
            category_item = QTableWidgetItem(category)
            category_item.setBackground(Qt.GlobalColor.lightGray)
            self.constants_table.setItem(row, 0, category_item)
            row += 1

            for name, data in constants.items():
                self.constants_table.insertRow(row)
                self.constants_table.setItem(row, 0, QTableWidgetItem(name))
                self.constants_table.setItem(
                    row, 1, QTableWidgetItem(data["value"]))
                self.constants_table.setItem(
                    row, 2, QTableWidgetItem(data["unit"]))
                self.constants_table.setItem(
                    row, 3, QTableWidgetItem(data["description"]))
                row += 1


class UnitsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Единицы измерения")
        self.setFixedSize(700, 500)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        title = QLabel("Единицы измерения")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        self.units_table = QTableWidget()
        self.units_table.setColumnCount(4)
        self.units_table.setHorizontalHeaderLabels(
            ["Единица", "Обозначение", "Величина", "Определение"])
        self.units_table.horizontalHeader().setStretchLastSection(True)

        layout.addWidget(self.units_table)

        # Кнопка закрытия
        close_btn = QPushButton("Закрыть")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)

        self.setLayout(layout)

        # Заполняем таблицу
        self.fill_units_table()

    def fill_units_table(self):
        row = 0
        for category, units in PHYSICS_UNITS.items():
            # Добавляем строку с категорией
            self.units_table.insertRow(row)
            category_item = QTableWidgetItem(category)
            category_item.setBackground(Qt.GlobalColor.lightGray)
            self.units_table.setItem(row, 0, category_item)
            row += 1

            # Добавляем единицы этой категории
            for name, data in units.items():
                self.units_table.insertRow(row)
                self.units_table.setItem(row, 0, QTableWidgetItem(name))
                self.units_table.setItem(
                    row, 1, QTableWidgetItem(data["symbol"]))
                self.units_table.setItem(
                    row, 2, QTableWidgetItem(data["quantity"]))
                self.units_table.setItem(
                    row, 3, QTableWidgetItem(data["definition"]))
                row += 1


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("О программе")
        self.setFixedSize(300, 200)

        layout = QVBoxLayout()

        title = QLabel("Физический Калькулятор")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")

        version = QLabel("Версия 1.0")
        info = QLabel("Расчет физических формул\n\nPyQt6 + Python")

        close_btn = QPushButton("Закрыть")
        close_btn.clicked.connect(self.close)

        layout.addWidget(title)
        layout.addWidget(version)
        layout.addWidget(info)
        layout.addWidget(close_btn)

        self.setLayout(layout)


class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setWindowTitle("Настройки")
        self.setFixedSize(250, 150)

        layout = QVBoxLayout()

        title = QLabel("Настройки программы")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")

        layout.addWidget(QLabel("Точность вычислений:"))
        self.precision_combo = QComboBox()
        self.precision_combo.addItems(["2", "4", "6", "8", "10"])

        if hasattr(parent, 'calculation_precision'):
            current_precision = parent.calculation_precision
        else:
            current_precision = 6

        self.precision_combo.setCurrentText(str(current_precision))

        buttons_layout = QHBoxLayout()
        ok_btn = QPushButton("OK")
        cancel_btn = QPushButton("Отмена")

        ok_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)

        buttons_layout.addWidget(ok_btn)
        buttons_layout.addWidget(cancel_btn)

        layout.addWidget(title)
        layout.addWidget(self.precision_combo)
        layout.addLayout(buttons_layout)

        self.setLayout(layout)
