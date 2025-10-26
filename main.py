import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel,
                             QListWidget, QComboBox, QLineEdit, QPushButton)
from PyQt6.QtCore import Qt
from formulas import categories
from styles import DARK_THEME, LIGHT_THEME


class PhysicsCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.theme_file = "theme_status.txt"
        self.current_theme = self.load_theme()  # загружаем тему из файла
        self.initUI()

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
        self.category_combo.addItems(categories)
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
        reference_menu.addAction("Константы")
        reference_menu.addAction("Единицы измерения")

        # меню "темы"
        themes_menu = menuBar.addMenu("Темы")
        dark_theme_action = themes_menu.addAction("Темная тема")
        light_theme_action = themes_menu.addAction("Светлая тема")

        dark_theme_action.triggered.connect(lambda: self.apply_theme("dark"))
        light_theme_action.triggered.connect(lambda: self.apply_theme("light"))

        # меню "история"
        history_menu = menuBar.addMenu("История")
        history_menu.addAction("Очистить историю")
        history_menu.addAction("Показать историю")

    def apply_theme(self, theme_name):
        """Применение выбранной темы"""
        self.current_theme = theme_name
        self.save_theme(theme_name)  # сохраняем в файл

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

        # Обновляем стили полей ввода
        for input_field in self.input_fields.values():
            input_field.setStyleSheet(theme["input_field"])

    def update_formulas_list(self):
        # обновление списка формул при смене категории
        category = self.category_combo.currentText()
        self.formula_list.clear()

        if category in categories:
            self.formula_list.addItems(categories[category])

    def on_formula_selected(self, formula_name):
        if not formula_name:
            return

        self.current_formula_name = formula_name
        category = self.category_combo.currentText()

        formula_data = categories[category][formula_name]

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

    def calculate(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PhysicsCalculator()
    window.show()
    sys.exit(app.exec())
