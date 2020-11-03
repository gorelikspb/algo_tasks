def calculate(inputs):
    stack = []
    for a in inputs:
        if a.isdigit():
            stack.append(a)
            continue
        op1, op2 = int(stack.pop()), int(stack.pop())

        if a == '+':
            stack.append(op2 + op1)
        elif a == '-':
            stack.append(op2 - op1)
        elif a == '*':
            stack.append(op2 * op1)
        elif a == '/':
            stack.append(op2 / op1)

    return stack.pop()


inputs = input().split()
print (calculate(inputs))