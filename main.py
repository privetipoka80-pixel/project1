from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QListWidget, QComboBox,
                             QLineEdit, QPushButton, QDialog, QMessageBox, QTableWidgetItem, QTableWidget)
from PyQt6.QtGui import QIcon
from constans import PHYSICS_CONSTANTS, PHYSICS_UNITS
from styles import DARK_THEME, LIGHT_THEME
from formulas import CATEGORIES
from calculator import Calculator
from datetime import datetime
from PyQt6.QtCore import Qt
import sqlite3
import json
import sys
import os


class HistoryDB:
    def __init__(self):
        self.conn = sqlite3.connect('history.db')
        self.create_table()

    def create_table(self):
        """Создаем одну таблицу для истории"""
        self.conn.execute('''CREATE TABLE IF NOT EXISTS history
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          formula_name TEXT,
                          inputs TEXT,
                          result TEXT,
                          timestamp TEXT)''')
        self.conn.commit()

    def add_calculation(self, formula_name, inputs, result):
        """Добавляем запись в историю"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        inputs_json = json.dumps(inputs)  # сохраняем как JSON

        self.conn.execute('INSERT INTO history (formula_name, inputs, result, timestamp) VALUES (?, ?, ?, ?)',
                          (formula_name, inputs_json, str(result), timestamp))
        self.conn.commit()

    def get_history(self):
        """Получаем всю историю"""
        cursor = self.conn.execute(
            'SELECT * FROM history ORDER BY timestamp DESC')
        return cursor.fetchall()

    def clear_history(self):
        """Очищаем историю"""
        self.conn.execute('DELETE FROM history')
        self.conn.commit()


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


class PhysicsCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.theme_file = "theme_status.txt"
        self.current_theme = self.load_theme()  # загружаем тему из файла
        self.db = HistoryDB()  # добавление БД
        self.calculation_precision = 6
        self.set_app_icon()  # иконка приложения
        self.initUI()

    def set_app_icon(self):
        """Устанавливает иконку с правильным путем для exe"""

        base_path = os.path.dirname(os.path.abspath(__file__))

        icon_path = os.path.join(base_path, "texture", "app_icon.png")
        self.setWindowIcon(QIcon(icon_path))

    def load_theme(self):
        """Загрузка темы из файла"""
        try:
            if os.path.exists(self.theme_file):
                with open(self.theme_file, 'r', encoding='utf-8') as f:
                    theme = f.read().strip()
                    return theme if theme in ['dark', 'light'] else 'dark'
            else:
                # если файла нет создаем его с темой по умолчанию
                self.save_theme('dark')
                return 'dark'
        except Exception:
            return 'dark'

    def save_theme(self, theme):
        """Сохранение темы в файл"""
        try:
            with open(self.theme_file, 'w', encoding='utf-8') as f:
                f.write(theme)
        except Exception:
            pass

    def initUI(self):
        self.setWindowTitle('Физический калькулятор')
        self.setGeometry(100, 100, 900, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.layout = QHBoxLayout(central_widget)
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(15, 15, 15, 15)

        # левая панель (список формул по категориям)
        left_panel = QWidget()
        left_panel.setMaximumWidth(300)
        self.left_layout = QVBoxLayout(left_panel)
        self.left_layout.setSpacing(8)

        # заголовок
        title_label = QLabel("Формулы по физике")
        self.left_layout.addWidget(title_label)

        # выбор категории
        category_label = QLabel("Категория:")
        self.left_layout.addWidget(category_label)

        self.category_combo = QComboBox()
        self.left_layout.addWidget(self.category_combo)

        # Список формул
        formulas_label = QLabel("Формулы:")
        self.left_layout.addWidget(formulas_label)

        self.formula_list = QListWidget()
        self.left_layout.addWidget(self.formula_list)

        # правая панель (отображение формулы и калькулятора)
        right_panel = QWidget()
        self.right_layout = QVBoxLayout(right_panel)
        self.right_layout.setSpacing(10)

        # добавление элементов для отображения формулы
        self.formula_name_label = QLabel("Выберите формулу")
        self.right_layout.addWidget(self.formula_name_label)

        self.formula_expression_label = QLabel("")
        self.right_layout.addWidget(self.formula_expression_label)

        self.category_label = QLabel("")
        self.right_layout.addWidget(self.category_label)

        # layout для переменных
        self.variables_layout = QVBoxLayout()
        self.variables_layout.setSpacing(8)
        self.right_layout.addLayout(self.variables_layout)

        # кнопка расчета
        self.calculate_button = QPushButton("Рассчитать")
        self.calculate_button.clicked.connect(self.calculate)
        self.right_layout.addWidget(self.calculate_button)

        # поле для результата
        self.result_label = QLabel("")
        self.right_layout.addWidget(self.result_label)

        # добавление панели в основной layout
        self.layout.addWidget(left_panel)
        self.layout.addWidget(right_panel)

        # создание менюбар
        self.createMenuBar()

        # инициализация
        self.input_fields = {}
        self.current_formula = None
        self.category_combo.addItems(CATEGORIES)
        self.category_combo.currentTextChanged.connect(
            self.update_formulas_list)
        self.formula_list.currentTextChanged.connect(self.on_formula_selected)

        # применяем тему из файла
        self.apply_theme(self.current_theme)
        self.update_formulas_list()

    def createMenuBar(self):
        """создание менюбара"""
        menuBar = self.menuBar()

        # меню "справочник"
        reference_menu = menuBar.addMenu("Справочник")
        constants_action = reference_menu.addAction("Константы")
        units_action = reference_menu.addAction("Единицы измерения")

        constants_action.triggered.connect(self.show_constants)
        units_action.triggered.connect(self.show_units)

        # меню "темы"
        themes_menu = menuBar.addMenu("Темы")
        dark_theme_action = themes_menu.addAction("Темная тема")
        light_theme_action = themes_menu.addAction("Светлая тема")

        dark_theme_action.triggered.connect(lambda: self.apply_theme("dark"))
        light_theme_action.triggered.connect(lambda: self.apply_theme("light"))

        # меню "история"
        history_menu = menuBar.addMenu("История")
        show_history_action = history_menu.addAction("Показать историю")
        clear_history_action = history_menu.addAction("Очистить историю")

        show_history_action.triggered.connect(self.show_history)
        clear_history_action.triggered.connect(self.clear_history)

        # меню "Настройки"
        settings_menu = menuBar.addMenu("Настройки")
        settings_action = settings_menu.addAction("Настройки")
        settings_action.triggered.connect(self.show_settings)

        # меню "Справка"
        help_menu = menuBar.addMenu("Справка")
        about_action = help_menu.addAction("О программе")
        about_action.triggered.connect(self.show_about)

    def show_constants(self):
        """Показать справочник констант"""
        dialog = ConstantsDialog(self)
        dialog.exec()

    def show_units(self):
        """Показать справочник единиц измерения"""
        dialog = UnitsDialog(self)
        dialog.exec()

    def show_about(self):
        """Показать диалог О программе"""
        dialog = AboutDialog(self)
        dialog.exec()

    def show_settings(self):
        """Показать диалог настроек"""
        dialog = SettingsDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            # сохраняем точность
            self.calculation_precision = int(
                dialog.precision_combo.currentText())
            QMessageBox.information(
                self, "Настройки", f"Точность установлена: {self.calculation_precision} знаков")

    def apply_theme(self, theme_name):
        """Применение выбранной темы"""
        self.current_theme = theme_name
        self.save_theme(theme_name)

        theme = DARK_THEME if theme_name == "dark" else LIGHT_THEME

        # применяем стили ко всем элементам
        self.setStyleSheet(theme["main_window"])

        # находим все элементы и применяем стили
        for widget in self.findChildren(QLabel):
            if widget == self.formula_name_label:
                widget.setStyleSheet(theme["formula_name"])
            elif widget == self.formula_expression_label:
                widget.setStyleSheet(theme["formula_expression"])
            elif widget == self.result_label:
                widget.setStyleSheet(theme["result_label"])
            elif "Формулы по физике" in widget.text():
                widget.setStyleSheet(theme["title_label"])
            else:
                widget.setStyleSheet(theme["subtitle_label"])

        self.category_combo.setStyleSheet(theme["combo_box"])
        self.formula_list.setStyleSheet(theme["list_widget"])
        self.calculate_button.setStyleSheet(theme["calculate_button"])

        # обновляем стили полей ввода
        for input_field in self.input_fields.values():
            input_field.setStyleSheet(theme["input_field"])

    def update_formulas_list(self):
        # обновление списка формул при смене категории
        category = self.category_combo.currentText()
        self.formula_list.clear()

        if category in CATEGORIES:
            self.formula_list.addItems(CATEGORIES[category])

    def on_formula_selected(self, formula_name):
        if not formula_name:
            return

        self.current_formula_name = formula_name
        category = self.category_combo.currentText()

        formula_data = CATEGORIES[category][formula_name]

        # обновление отображения формулы
        self.formula_name_label.setText(formula_name)
        self.formula_expression_label.setText(formula_data["formula"])
        self.category_label.setText(f"Категория: {category}")

        # полная очистка
        for i in reversed(range(self.variables_layout.count())):
            item = self.variables_layout.itemAt(i)
            if item.layout():
                # удаление всех виджетов из вложенного layout
                for j in reversed(range(item.layout().count())):
                    widget = item.layout().itemAt(j).widget()
                    if widget:
                        widget.deleteLater()
                item.layout().deleteLater()
            elif item.widget():
                item.widget().deleteLater()

        self.input_fields = {}

        # создание полей для переменных
        for var_name, var_info in formula_data['variables'].items():
            var_layout = QHBoxLayout()

            label = QLabel(f"{var_name}:")
            label.setFixedWidth(80)
            label.setStyleSheet("font-weight: bold; font-size: 13px;")

            input_field = QLineEdit()
            input_field.setPlaceholderText(
                f"{var_info['description']} ({var_info['unit']})")

            # применение текущей темы к полю ввода
            theme = DARK_THEME if self.current_theme == "dark" else LIGHT_THEME
            input_field.setStyleSheet(theme["input_field"])

            var_layout.addWidget(label)
            var_layout.addWidget(input_field)
            self.variables_layout.addLayout(var_layout)

            self.input_fields[var_name] = input_field

        # обновление интерфейса
        self.variables_layout.update()

    def show_history(self):
        """Показываем диалог истории"""
        dialog = HistoryDialog(self.db, self)
        dialog.exec()

    def clear_history(self):
        """Очищаем историю"""
        self.db.clear_history()
        QMessageBox.information(self, "История", "История вычислений очищена")

    # метод для вычисления
    def calculate(self):
        if not hasattr(self, 'current_formula_name'):
            self.result_label.setStyleSheet("color: red; font-size: 12px;")
            self.result_label.setText("Сначала выберите формулу")
            return

        # сбрасываем стили всех полей ввода
        self.reset_input_fields_style()

        # получаем текущую категорию и формулу
        category = self.category_combo.currentText()
        formula_name = self.current_formula_name
        formula_data = {formula_name: CATEGORIES[category][formula_name]}

        # собираем значения из полей ввода
        input_values = {}
        for var_name, input_field in self.input_fields.items():
            input_values[var_name] = input_field.text()

        # вычисляем результат
        calculator = Calculator()
        calculation_result = calculator.calculate(formula_data, input_values)

        # обрабатываем результат
        if calculation_result["success"]:
            result = calculation_result["result"]
            target_var = calculation_result["target_variable"]

            # Создаем копию input_values и добавляем результат
            all_data = input_values.copy()
            all_data[target_var] = f"{result:.{self.calculation_precision}f}"

            self.db.add_calculation(formula_name, all_data, str(result))

            # отображаем результат в соответствующем поле ввода
            if target_var in self.input_fields:
                result_field = self.input_fields[target_var]
                result_field.setText(
                    f"{result:.{self.calculation_precision}f}")

                # применяем зеленый стиль для поле с результатом
                result_field.setStyleSheet("""
                    QLineEdit {
                        background-color: #388e3c;
                        color: #ffffff;
                        border: 2px solid #4caf50;
                        border-radius: 3px;
                        padding: 5px;
                        font-weight: bold;
                    }
                """)

            # очищаем сообщение об ошибке
            self.result_label.setText("")

        else:
            # показываем ошибку красным цветом снизу
            self.result_label.setText(f"Ошибка: {calculation_result['error']}")
            self.result_label.setStyleSheet("color: red; font-size: 12px;")

    def reset_input_fields_style(self):
        """Сбрасывает стили всех полей ввода к обычному"""
        theme = DARK_THEME if self.current_theme == "dark" else LIGHT_THEME
        for input_field in self.input_fields.values():
            input_field.setStyleSheet(theme["input_field"])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PhysicsCalculator()
    window.show()
    sys.exit(app.exec())
