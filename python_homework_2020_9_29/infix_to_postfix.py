from stack_class import stack


def compare_oper(oper):
    if oper == "(":
        return 0
    elif oper == "+" or oper == "-":
        return 1
    elif oper == "*" or oper == "/":
        return 2


def infix_to_postfix(math):
    math_list = []
    operators_stack = stack()
    result = ""

    for i in math:
        if i in "+-*/()":
            if i == "(":
                operators_stack.push(i)
            elif i in "+-*/":
                if operators_stack.isEmpty():
                    operators_stack.push(i)
                else:
                    if compare_oper(i) >= compare_oper(operators_stack.peek()):
                        operators_stack.push(i)
                    else:
                        while True:
                            if operators_stack.peek() == "(" or operators_stack.isEmpty():
                                break
                            else:
                                math_list.append(operators_stack.pop())
                        operators_stack.push(i)
            else:
                while True:
                    if operators_stack.peek() == "(" or operators_stack.isEmpty():
                        break
                    else:
                        math_list.append(operators_stack.pop())
                operators_stack.pop()
        else:
            math_list.append(i)

    while not operators_stack.isEmpty():
        math_list.append(operators_stack.pop())

    for term in math_list:
        result += term

    return result


# run
math = "3+(2*4+7)/4"
print(infix_to_postfix(math))
