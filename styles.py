# Стили для темной темы
DARK_THEME = {
    "main_window": """
        background-color: #1e1e1e;
        color: white;
    """,

    "title_label": """
        font-size: 16px;
        font-weight: bold;
    """,

    "subtitle_label": """
        font-size: 13px;
        color: #cccccc;
    """,

    "combo_box": """
        QComboBox {
            padding: 8px;
            font-size: 14px;
            background-color: #2a2a2a;
            border: 2px solid #555;
            border-radius: 5px;
            outline: none;
        }
        QComboBox:focus {
            border: 2px solid #555;
        }
        QComboBox:hover {
            border-color: #777;
        }
        QComboBox QAbstractItemView {
            background-color: #2a2a2a;
            border: 1px solid #555;
            selection-background-color: #4CAF50;
            outline: none;
        }
        QComboBox QAbstractItemView::item {
            padding: 8px;
            border-bottom: 1px solid #444;
            outline: none;
        }
        QComboBox QAbstractItemView::item:focus {
            outline: none;
        }
    """,

    "list_widget": """
        QListWidget {
            background-color: #2a2a2a;
            border: 2px solid #555;
            border-radius: 5px;
            outline: none;
        }
        QListWidget:focus {
            border: 2px solid #555;
        }
        QListWidget::item {
            padding: 8px;
            border-bottom: 1px solid #444;
            outline: none;
        }
        QListWidget::item:focus {
            outline: none;
            border: none;
        }
        QListWidget::item:hover {
            background-color: #333333;
        }
        QListWidget::item:selected {
            background-color: #3a3a3a;
        }
    """,

    "formula_name": """
        font-size: 18px;
        font-weight: bold;
    """,

    "formula_expression": """
        font-size: 16px;
        font-style: italic;
        color: #4CAF50;
    """,

    "calculate_button": """
        QPushButton {
            background-color: #4CAF50;
            border: none;
            padding: 10px;
            font-weight: bold;
            border-radius: 5px;
            outline: none;
        }
        QPushButton:focus {
            border: none;
        }
    """,

    "result_label": """
        font-weight: bold;
        color: #4CAF50;
    """,

    "input_field": """
        QLineEdit {
            padding: 8px;
            border: 2px solid #555;
            border-radius: 4px;
            background-color: #2a2a2a;
            outline: none;
        }
        QLineEdit:focus {
            border-color: #4CAF50;
        }
    """
}

# Стили для светлой темы
LIGHT_THEME = {
    "main_window": """
        background-color: #f5f5f5;
        color: #333333;
    """,

    "title_label": """
        font-size: 16px;
        font-weight: bold;
        color: #222222;
    """,

    "subtitle_label": """
        font-size: 13px;
        color: #444444;
        font-weight: bold;
    """,

    "combo_box": """
        QComboBox {
            padding: 8px;
            font-size: 14px;
            background-color: white;
            border: 2px solid #cccccc;
            border-radius: 5px;
            outline: none;
            color: #222222;
        }
        QComboBox:focus {
            border: 2px solid #cccccc;
        }
        QComboBox:hover {
            border-color: #b4bcb4;
        }
        QComboBox QAbstractItemView {
            background-color: white;
            border: 1px solid #cccccc;
            selection-background-color: #b4bcb4;
            outline: none;
            color: #222222;
        }
        QComboBox QAbstractItemView::item {
            padding: 8px;
            border-bottom: 1px solid #eeeeee;
            outline: none;
            color: #222222;
        }
        QComboBox QAbstractItemView::item:focus {
            outline: none;
        }
    """,

    "list_widget": """
        QListWidget {
            background-color: white;
            border: 2px solid #cccccc;
            border-radius: 5px;
            outline: none;
            color: #222222;
        }
        QListWidget:focus {
            border: 2px solid #cccccc;
        }
        QListWidget::item {
            padding: 8px;
            border-bottom: 1px solid #eeeeee;
            outline: none;
            color: #222222;
        }
        QListWidget::item:focus {
            outline: none;
            border: none;
        }
        QListWidget::item:hover {
            background-color: #f5f5f5;
        }
        QListWidget::item:selected {
            background-color: #b4bcb4;
            color: #222222;
        }
    """,

    "formula_name": """
        font-size: 18px;
        font-weight: bold;
        color: #222222;
    """,

    "formula_expression": """
        font-size: 16px;
        font-style: italic;
        color: #2E7D32;
    """,

    "calculate_button": """
        QPushButton {
            background-color: #4CAF50;
            border: none;
            padding: 10px;
            font-weight: bold;
            border-radius: 5px;
            outline: none;
            color: white;
        }
        QPushButton:focus {
            border: none;
        }
    """,

    "result_label": """
        font-weight: bold;
        color: #2E7D32;
    """,

    "input_field": """
        QLineEdit {
            padding: 8px;
            border: 2px solid #cccccc;
            border-radius: 4px;
            background-color: white;
            outline: none;
            color: #222222;
        }
        QLineEdit:focus {
            border-color: #4CAF50;
        }
        QLineEdit::placeholder {
            color: #666666;
        }
    """
}
