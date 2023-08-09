# Создайте часть компилятора, осуществляющую лексический анализ ввода языка My Again Shell

import re

patterns = [
    (r'\b(if|else|while|for)\b', 'KEYWORD'),
    (r'\b([a-zA-Z_]\w*)\b', 'IDENTIFIER'),
    (r'\b(\d+\.\d+|\d+)\b', 'NUMBER'),
    (r'"([^"]*)"', 'STRING'),
    (r'(\>|/<|\+|\-|\*|/|\=|!)', 'OPERATOR'),
    (r'(\(|\)|\{|\}|,|;)', 'DELIMITER'),
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


def main():
    # Пример использования
    code = 'if (x > 0) { print("Positive") } else { print("Negative") }'
    tokens = tokenize(code)
    for token, token_type in tokens:
        print(f'Token: {token}, Type: {token_type}')


if __name__ == "__main__":
    main()