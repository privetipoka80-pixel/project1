CATEGORIES = {
    "Механика": {
        "Второй закон Ньютона": {
            "formula": "F = m·a",
            "variables": {
                "F": {"unit": "Н", "description": "сила"},
                "m": {"unit": "кг", "description": "масса"},
                "a": {"unit": "м/с²", "description": "ускорение"}
            }
        },
        "Кинетическая энергия": {
            "formula": "Eₖ = mv²/2",
            "variables": {
                "Eₖ": {"unit": "Дж", "description": "кинетическая энергия"},
                "m": {"unit": "кг", "description": "масса"},
                "v": {"unit": "м/с", "description": "скорость"}
            }
        },
        "Потенциальная энергия": {
            "formula": "Eₚ = mgh",
            "variables": {
                "Eₚ": {"unit": "Дж", "description": "потенциальная энергия"},
                "m": {"unit": "кг", "description": "масса"},
                "g": {"unit": "м/с²", "description": "ускорение свободного падения"},
                "h": {"unit": "м", "description": "высота"}
            }
        },
        "Импульс": {
            "formula": "p = mv",
            "variables": {
                "p": {"unit": "кг·м/с", "description": "импульс"},
                "m": {"unit": "кг", "description": "масса"},
                "v": {"unit": "м/с", "description": "скорость"}
            }
        }
    },
    "Термодинамика": {
        "КПД тепловой машины": {
            "formula": "η = (Q₁ - Q₂)/Q₁",
            "variables": {
                "η": {"unit": "%", "description": "коэффициент полезного действия"},
                "Q₁": {"unit": "Дж", "description": "полученная теплота"},
                "Q₂": {"unit": "Дж", "description": "отданная теплота"}
            }
        },
        "Удельная теплота": {
            "formula": "Q = cmΔT",
            "variables": {
                "Q": {"unit": "Дж", "description": "количество теплоты"},
                "c": {"unit": "Дж/(кг·°C)", "description": "удельная теплоёмкость"},
                "m": {"unit": "кг", "description": "масса"},
                "ΔT": {"unit": "°C", "description": "изменение температуры"}
            }
        }
    },
    "Электричество": {
        "Закон Ома": {
            "formula": "I = U/R",
            "variables": {
                "I": {"unit": "А", "description": "сила тока"},
                "U": {"unit": "В", "description": "напряжение"},
                "R": {"unit": "Ом", "description": "сопротивление"}
            }
        },
        "Мощность тока": {
            "formula": "P = UI",
            "variables": {
                "P": {"unit": "Вт", "description": "мощность"},
                "U": {"unit": "В", "description": "напряжение"},
                "I": {"unit": "А", "description": "сила тока"}
            }
        },
        "Энергия конденсатора": {
            "formula": "W = CU²/2",
            "variables": {
                "W": {"unit": "Дж", "description": "энергия"},
                "C": {"unit": "Ф", "description": "ёмкость"},
                "U": {"unit": "В", "description": "напряжение"}
            }
        }
    },
    "Оптика": {
        "Закон преломления": {
            "formula": "n₁sinα = n₂sinβ",
            "variables": {
                "n₁": {"unit": "-", "description": "показатель преломления первой среды"},
                "n₂": {"unit": "-", "description": "показатель преломления второй среды"},
                "α": {"unit": "°", "description": "угол падения"},
                "β": {"unit": "°", "description": "угол преломления"}
            }
        },
        "Формула тонкой линзы": {
            "formula": "1/F = 1/d + 1/f",
            "variables": {
                "F": {"unit": "м", "description": "фокусное расстояние"},
                "d": {"unit": "м", "description": "расстояние до объекта"},
                "f": {"unit": "м", "description": "расстояние до изображения"}
            }
        }
    },
    "Гидродинамика": {
        "Расход жидкости": {
            "formula": "Q = Sv",
            "variables": {
                "Q": {"unit": "м³/с", "description": "расход жидкости"},
                "S": {"unit": "м²", "description": "площадь сечения"},
                "v": {"unit": "м/с", "description": "скорость течения"}
            }
        },
        "Сила Архимеда": {
            "formula": "F = ρgV",
            "variables": {
                "F": {"unit": "Н", "description": "выталкивающая сила"},
                "ρ": {"unit": "кг/м³", "description": "плотность жидкости"},
                "g": {"unit": "м/с²", "description": "ускорение свободного падения"},
                "V": {"unit": "м³", "description": "объём погружённой части"}
            }
        }
    }
}
