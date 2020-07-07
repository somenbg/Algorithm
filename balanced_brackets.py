inp = '()[]{()adjsad}'

def balance_checker(str):

    open_char = ['(', '[', '{', ]
    close_char = [')', ']', '}', ]
    fifo_stack = [] 


    for char in str:
        if char in open_char:
            fifo_stack.append(char)
        else:
            if len(fifo_stack) == 0:
                return False
            if char in close_char:
                last_open_bracket = fifo_stack.pop()

                if not compare_bracket(last_open_bracket, char):
                    return False

    if len(fifo_stack) != 0:
        return False
    else:
        return True


def compare_bracket(open_bracket, close_bracket):
    if open_bracket == '(' and close_bracket == ')':
        return True
    elif open_bracket == '[' and close_bracket == ']':
        return True
    elif open_bracket == '{' and close_bracket == '}':
        return True
    else:
        return False


balance_checker(inp)