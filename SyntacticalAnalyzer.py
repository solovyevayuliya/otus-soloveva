from LexicalAnalyzer import tokenize

def parse_expression(tokens):
    # Рекурсивная функция для анализа выражения

    # Базовый случай - одиночное значение
    if len(tokens) == 1:
        return tokens[0]

    # Поиск оператора с наивысшим приоритетом
    priorities = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '=': 3, '!': 3}
    highest_priority = -1
    highest_priority_index = -1

    for i, (token, token_type) in enumerate(tokens):
        if token_type == 'OPERATOR':
            priority = priorities[token]
            if priority > highest_priority:
                highest_priority = priority
                highest_priority_index = i

    # Если нет операторов, значит это простое значение
    if highest_priority_index == -1:
        return tokens[0]

    # Разделение выражения на левую и правую части
    left_tokens = tokens[:highest_priority_index]
    right_tokens = tokens[highest_priority_index + 1:]

    operator = tokens[highest_priority_index][0]

    # Рекурсивный вызов для левой и правой частей
    left_expression = parse_expression(left_tokens)
    right_expression = parse_expression(right_tokens)

    # Возвращаем словарь, представляющий операцию
    return {'operator': operator, 'left': left_expression, 'right': right_expression}


def parse_code(code):
    tokens = tokenize(code)
    return parse_expression(tokens)
