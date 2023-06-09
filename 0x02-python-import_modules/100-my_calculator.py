#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1
    user_inputs = sys.argv
    if len(user_inputs) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    if user_inputs[2] not in '+-*/':
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    a = int(user_inputs[1])
    b = int(user_inputs[3])
    if user_inputs[2] == '+':
        result = calculator_1.add(a, b)
    elif user_inputs[2] == '-':
        result = calculator_1.sub(a, b)
    elif user_inputs[2] == '*':
        result = calculator_1.mul(a, b)
    elif user_inputs[2] == '/':
        result = calculator_1.div(a, b)
    print('{} {} {} = {}'.format(a, user_inputs[2],  b, result))
