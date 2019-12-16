def eval(expression):
    stack = []
    rpn = ""
    for c in expression:
        if c != ' ':
            if c == '+' or c == '-' or c == '*' or c == '/' or c == '(':
                stack.append(c)
            elif c == ')':
                poped = ''
                while poped != '(' and len(stack) != 0:
                    poped = stack.pop()
                    if poped != '(':
                        rpn += poped
            elif str.isdigit(c):
                rpn += c
    while len(stack) != 0:
        poped = stack.pop()
        if poped != '(':
            rpn += poped
    print(rpn)

    for c in rpn:
        if c == '+' or c == '-' or c == '*' or c == '/' or c == '(':
            second_param = stack.pop()
            if len(stack)==0:
                first_param = 0
            else:
                first_param = stack.pop()
            if c == '+':
                stack.append(first_param + second_param)
            elif c == '-':
                stack.append(first_param - second_param)
            elif c == '/':
                stack.append(first_param / second_param)
            elif c == '*':
                stack.append(first_param * second_param)
        else:
            stack.append(int(c))
    res = stack.pop()
    return res


print eval('- (3 + ( 2 - 1 ) )')
#print eval('2 + (3 * 8) - (4 + (4 / (2 + 2)) * 6)')
# -4