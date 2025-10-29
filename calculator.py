import math


class Calculator:
    def calculate(self, formula_data, input_values):
        """
        Универсальный калькулятор для физических формул
        """
        try:
            # получаем название формулы и переменные
            formula_name = list(formula_data.keys())[0]
            formula_info = formula_data[formula_name]
            variables = formula_info['variables']

            # проверяем и преобразуем введенные значения
            calculated_vars = {}
            missing_vars = []

            for var_name in variables.keys():
                value = input_values.get(var_name, '').strip()
                if value:
                    try:
                        # заменяем запятые на точки и преобразуем в число
                        cleaned_value = value.replace(',', '.')
                        calculated_vars[var_name] = float(cleaned_value)
                    except ValueError:
                        return {
                            "success": False,
                            "error": f"Некорректное значение для {var_name}",
                            "result": None
                        }
                else:
                    missing_vars.append(var_name)

            # проверяем что заполнены все переменные кроме одной (которую вычисляем)
            if len(missing_vars) != 1:
                return {
                    "success": False,
                    "error": f"Заполните все поля кроме одного (которое нужно вычислить)",
                    "result": None
                }

            # переменная, которую нужно вычислить
            target_var = missing_vars[0]

            # вычисляем результат в зависимости от формулы
            result = self.solve_formula(
                formula_name, calculated_vars, target_var)

            if result is None:
                return {
                    "success": False,
                    "error": "Не удалось вычислить результат",
                    "result": None
                }

            return {
                "success": True,
                "result": result,
                "target_variable": target_var,
                "error": None
            }

        except Exception as e:
            return {
                "success": False,
                "error": f"Ошибка вычисления: {str(e)}",
                "result": None
            }

    def solve_formula(self, formula_name, known_vars, target_var):
        """
        Решает конкретную формулу
        """
        try:
            if formula_name == "Второй закон Ньютона":
                if target_var == "F":
                    return known_vars["m"] * known_vars["a"]
                elif target_var == "m":
                    return known_vars["F"] / known_vars["a"]
                elif target_var == "a":
                    return known_vars["F"] / known_vars["m"]

            elif formula_name == "Кинетическая энергия":
                if target_var == "Eₖ":
                    return (known_vars["m"] * known_vars["v"] ** 2) / 2
                elif target_var == "m":
                    return (2 * known_vars["Eₖ"]) / (known_vars["v"] ** 2)
                elif target_var == "v":
                    return math.sqrt((2 * known_vars["Eₖ"]) / known_vars["m"])

            elif formula_name == "Потенциальная энергия":
                if target_var == "Eₚ":
                    return known_vars["m"] * known_vars["g"] * known_vars["h"]
                elif target_var == "m":
                    return known_vars["Eₚ"] / (known_vars["g"] * known_vars["h"])
                elif target_var == "g":
                    return known_vars["Eₚ"] / (known_vars["m"] * known_vars["h"])
                elif target_var == "h":
                    return known_vars["Eₚ"] / (known_vars["m"] * known_vars["g"])

            elif formula_name == "Импульс":
                if target_var == "p":
                    return known_vars["m"] * known_vars["v"]
                elif target_var == "m":
                    return known_vars["p"] / known_vars["v"]
                elif target_var == "v":
                    return known_vars["p"] / known_vars["m"]

            elif formula_name == "Закон Ома":
                if target_var == "I":
                    return known_vars["U"] / known_vars["R"]
                elif target_var == "U":
                    return known_vars["I"] * known_vars["R"]
                elif target_var == "R":
                    return known_vars["U"] / known_vars["I"]

            elif formula_name == "Мощность тока":
                if target_var == "P":
                    return known_vars["U"] * known_vars["I"]
                elif target_var == "U":
                    return known_vars["P"] / known_vars["I"]
                elif target_var == "I":
                    return known_vars["P"] / known_vars["U"]

            elif formula_name == "Энергия конденсатора":
                if target_var == 'W':
                    return (known_vars['C'] * known_vars['U'] ** 2) / 2
                elif target_var == 'C':
                    return (2 * known_vars['W']) / (known_vars['U'] ** 2)
                elif target_var == 'U':
                    return math.sqrt((2 * known_vars['W']) / known_vars['C'])

            elif formula_name == 'КПД тепловой машины':
                if target_var == 'η':
                    return ((known_vars['Q₁'] - known_vars['Q₂']) / known_vars['Q₁']) * 100
                elif target_var == 'Q₂':
                    return known_vars['Q₁'] - ((known_vars['η'] / 100) * known_vars['Q₁'])
                elif target_var == 'Q₁':
                    return known_vars['Q₂'] / (1 - (known_vars['η'] / 100))

            elif formula_name == 'Удельная теплота':
                if target_var == 'Q':
                    return known_vars['c'] * known_vars['m'] * known_vars['ΔT']
                elif target_var == 'c':
                    return known_vars['Q'] / (known_vars['m'] * known_vars['ΔT'])
                elif target_var == 'm':
                    return known_vars['Q'] / (known_vars['c'] * known_vars['ΔT'])
                elif target_var == 'ΔT':
                    return known_vars['Q'] / (known_vars['c'] * known_vars['m'])

            elif formula_name == 'Закон преломления':
                sin_a = math.sin(math.radians(known_vars.get('α', 0)))
                sin_b = math.sin(math.radians(known_vars.get('β', 0)))
                n1 = known_vars.get('n₁', 0)
                n2 = known_vars.get('n₂', 0)

                if target_var == 'n₁':
                    return (n2 * sin_b) / sin_a
                elif target_var == 'n₂':
                    return (n1 * sin_a) / sin_b
                elif target_var == 'α':
                    return math.degrees(math.asin((n2 * sin_b) / n1))
                elif target_var == 'β':
                    return math.degrees(math.asin((n1 * sin_a) / n2))

            elif formula_name == 'Формула тонкой линзы':
                if target_var == 'F':
                    return (known_vars['d'] * known_vars['f']) / (known_vars['d'] + known_vars['f'])
                elif target_var == 'd':
                    return (known_vars['F'] * known_vars['f']) / (known_vars['f'] - known_vars['F'])
                elif target_var == 'f':
                    return (known_vars['F'] * known_vars['d']) / (known_vars['d'] - known_vars['F'])

            elif formula_name == 'Расход жидкости':
                if target_var == 'Q':
                    return known_vars['S'] * known_vars['v']
                elif target_var == 'S':
                    return known_vars['Q'] / known_vars['v']
                elif target_var == 'v':
                    return known_vars['Q'] / known_vars['S']

            elif formula_name == 'Сила Архимеда':
                if target_var == 'F':
                    return known_vars['ρ'] * known_vars['g'] * known_vars['V']
                elif target_var == 'ρ':
                    return known_vars['F'] / (known_vars['g'] * known_vars['V'])
                elif target_var == 'g':
                    return known_vars['F'] / (known_vars['ρ'] * known_vars['V'])
                elif target_var == 'V':
                    return known_vars['F'] / (known_vars['ρ'] * known_vars['g'])

            return None

        except Exception:
            return None
