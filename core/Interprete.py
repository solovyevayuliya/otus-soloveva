import re

patterns = [
    (r'\b(\d+\.\d+|\d+)\b', 'NUMBER'),
    (r'\+', 'OPERATOR'),
    (r'\-', 'OPERATOR'),
    (r'\*', 'OPERATOR'),
    (r'\/', 'OPERATOR'),
    (r'\(', 'DELIMITER'),
    (r'\)', 'DELIMITER'),
]


def tokenize(code):
    tokens = []
    code = code.strip()

    while code:
        match = None
        for pattern, token_type in patterns:
            regex = re.compile(pattern)
            match = regex.match(code)
            if match:
                value = match.group(0)
                tokens.append((value, token_type))
                code = code[len(value):].strip()
                break

        if not match:
            raise SyntaxError(f"Invalid syntax: {code}")

    return tokens


def parse_expression(tokens):
    if len(tokens) == 1:
        return float(tokens[0][0])

    priorities = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
    highest_priority = -1
    highest_priority_index = -1

    for i, (token, token_type) in enumerate(tokens):
        if token_type == 'OPERATOR':
            priority = priorities[token]
            if priority > highest_priority:
                highest_priority = priority
                highest_priority_index = i

    if highest_priority_index == -1:
        return float(tokens[0][0])

    left_tokens = tokens[:highest_priority_index]
    right_tokens = tokens[highest_priority_index + 1:]

    operator = tokens[highest_priority_index][0]

    if operator == '(':
        # Находим соответствующую закрывающую скобку
        opening_brackets = 1
        closing_brackets = 0
        i = highest_priority_index + 1

        while opening_brackets != closing_brackets and i < len(tokens):
            if tokens[i][0] == '(':
                opening_brackets += 1
            elif tokens[i][0] == ')':
                closing_brackets += 1

            i += 1

        if opening_brackets != closing_brackets:
            raise SyntaxError("Invalid syntax: mismatched parentheses")

        expression_tokens = tokens[highest_priority_index + 1: i - 1]
        expression_result = parse_expression(expression_tokens)
        return expression_result

    left_expression = parse_expression(left_tokens)
    right_expression = parse_expression(right_tokens)

    if operator == '+':
        return left_expression + right_expression
    elif operator == '-':
        return left_expression - right_expression
    elif operator == '*':
        return left_expression * right_expression
    elif operator == '/':
        return left_expression / right_expression


def evaluate_expression(code):
    tokens = tokenize(code)
    result = parse_expression(tokens)
    return result


# Пример использования
code = '3 * 4 / 2'
result = evaluate_expression(code)
print(result)  # Выводит: 11.0
