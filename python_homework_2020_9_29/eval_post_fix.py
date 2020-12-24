from stack_class import stack

def eval_post_fx(math):
    math_stack = stack()
    operator = "+-*/"

    for i in math:
        if i in operator:
            num1 = math_stack.pop()
            num2 = math_stack.pop()
            str_math = num2 + i + num1
            
            num3 = math_stack.push(str(eval(str_math)))

        else:
            math_stack.push(i)
    
    return math_stack.pop()

# test
str_math = "82/3-32*+"

print(eval_post_fx(str_math))