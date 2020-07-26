def evaluate_rpn(expression):
    intermediate_results = []
    delimiter = ','
    operators = {
        '+': lambda y, x: x + y, '-': lambda y, x: x - y, '*': lambda y, x: x * y, '/': lambda y, x: x / y
    }

    for token in expression.split(delimiter):
        if token in operators:
            intermediate_results.append(operators[token](intermediate_results.pop(), intermediate_results.pop()))
        else:
            intermediate_results.append(int(token))

    return intermediate_results[-1]


def evaluate_prn(expression):
    expression = expression[::-1]
    return evaluate_rpn(expression)


if __name__ == '__main__':
    print(evaluate_rpn("3,4,+,2,*,1,+"))
    print(evaluate_prn("+,1,*,2,+,4,3"))
