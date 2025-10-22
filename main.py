import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel,
                             QListWidget, QComboBox, QLineEdit, QPushButton)
from formulas import categories


class PhysicsCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Физический калькулятор')
        self.setGeometry(100, 100, 1000, 700)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.layout = QHBoxLayout(central_widget)

        # левая панель (список формул по категориям)
        left_panel = QWidget()
        self.left_layout = QVBoxLayout(left_panel)

        self.left_layout.addWidget(QLabel("Формулы по физике"))

        # выбор категории
        self.category_combo = QComboBox()
        self.left_layout.addWidget(QLabel("Категория:"))
        self.left_layout.addWidget(self.category_combo)
        self.category_combo.addItems(categories)
        self.category_combo.currentTextChanged.connect(
            self.update_formulas_list)

        self.formula_list = QListWidget()
        self.left_layout.addWidget(self.formula_list)
        self.formula_list.currentTextChanged.connect(self.on_formula_selected)

        # правая панель (отображение формулы и калькулятора)
        right_panel = QWidget()
        self.right_layout = QVBoxLayout(right_panel)

        # добавление элементов для отображения формулы
        self.formula_name_label = QLabel("Выберите формулу")
        self.formula_name_label.setStyleSheet(
            "font-size: 18px; font-weight: bold;")
        self.right_layout.addWidget(self.formula_name_label)

        self.formula_expression_label = QLabel("")
        self.formula_expression_label.setStyleSheet(
            "font-size: 16px; font-style: italic;")
        self.right_layout.addWidget(self.formula_expression_label)

        self.category_label = QLabel("")
        self.right_layout.addWidget(self.category_label)

        # layout для переменных
        self.variables_layout = QVBoxLayout()
        self.right_layout.addLayout(self.variables_layout)

        # кнопка расчета
        self.calculate_button = QPushButton("Рассчитать")
        self.calculate_button.clicked.connect(self.calculate)
        self.right_layout.addWidget(self.calculate_button)

        # поле для результата
        self.result_label = QLabel("")
        self.result_label.setStyleSheet(
            "font-size: 16px; font-weight: bold; color: #4CAF50;")
        self.right_layout.addWidget(self.result_label)

        # добавление панели в основной layout
        self.layout.addWidget(left_panel, 1)
        self.layout.addWidget(right_panel, 2)

        # создание менюбар
        self.createMenuBar()

        # инициализация
        self.input_fields = {}
        self.current_formula = None

    def createMenuBar(self):
        """создание менюбара"""
        menuBar = self.menuBar()

        # меню "справочник"
        reference_menu = menuBar.addMenu("Справочник")
        reference_menu.addAction("Константы")
        reference_menu.addAction("Единицы измерения")

        # меню "темы"
        themes_menu = menuBar.addMenu("Темы")
        themes_menu.addAction("Сменить тему")

        # меню "история"
        history_menu = menuBar.addMenu("История")
        history_menu.addAction("Очистить историю")
        history_menu.addAction("Показать историю")

    def update_formulas_list(self):
        # обновление списка формул при смене категории
        category = self.category_combo.currentText()
        self.formula_list.clear()

        if category in categories:
            self.formula_list.addItems(categories[category])

    def on_formula_selected(self, formula_name):
        if not formula_name:
            return

        self.current_formula = formula_name
        # нужно получить данные формулы из файла formulas
        # пока что заглушка
        formula_data = self.get_formula_data(formula_name)

        if not formula_data:
            return

        # обновление отображения формулы
        self.formula_name_label.setText(formula_name)
        self.formula_expression_label.setText(formula_data["formula"])
        self.category_label.setText(f"Категория: {formula_data['category']}")

        # чистка старых полей
        while self.variables_layout.count():
            child = self.variables_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        self.input_fields = {}

        # создание поля для переменных
        for var_name, description in formula_data['variables'].items():
            var_layout = QHBoxLayout()

            label = QLabel(f"{var_name}:")
            label.setFixedWidth(80)
            label.setStyleSheet("font-weight: bold;")

            input_field = QLineEdit()
            input_field.setPlaceholderText(description)
            input_field.setStyleSheet("""
                QLineEdit {
                    padding: 8px;
                    border: 2px solid #555;
                    border-radius: 5px;
                    background-color: #2a2a2a;
                    color: white;
                }
                QLineEdit:focus {
                    border-color: #4CAF50;
                }
            """)

            var_layout.addWidget(label)
            var_layout.addWidget(input_field)
            self.variables_layout.addLayout(var_layout)

            self.input_fields[var_name] = input_field

    def get_formula_data(self, formula_name):
        # получение данных формулы (пока заглушка)
        return {
            "formula": "F = m * a",
            "category": self.category_combo.currentText(),
            "variables": {
                "F": "Сила (Н)",
                "m": "Масса (кг)",
                "a": "Ускорение (м/с²)"
            }
        }

    def calculate(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PhysicsCalculator()
    window.show()
    sys.exit(app.exec())
