# base case:
# n = 1: if the wrong one, 0; else 1
# n = 3: evaluate the expression then do n=1
# n > 3: add two recursive calls: one with just the first value, second with first expression


def solution(b, expr):
    first_val = expr[0]
    if len(expr) == 0 or len(expr) % 2 == 0:
        return 0
    if len(expr) == 1:
        return b & first_val
    if len(expr):
        version1, version2 = 0
        first_op = expr[1]
        second_val = expr[2]
        first_eval = 0
        if first_op == '&':
            first_eval = first_val & second_val
            if first_val != 0 or b != 1:
                version1 = solution(b, expr[2:])
            if first_val == 0 and b == 0:
                version1 += solution(1, expr[2:])
        elif first_op == '|':
            first_eval = first_val | second_val
            if b == 0 and first_val == 1:
                version1 = 0
            else:
                version1 = solution(b, expr[2:])
        elif first_op == '^':
            first_eval = first_val ^ second_val
            if first_val == 0:
                version1 = solution(b, expr[2:])
            else:
                version1 = solution(not b, expr[2:])
        expr[2] = first_eval
        version2 = solution(b, expr[2:])
        return version1 + version2


print(solution(0, [1, '^', 0, '|', 0, '|', 1]))