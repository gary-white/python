def is_balanced(s):
    n_left_brace = n_right_brace = 0
    for i in s:
        if i == '(':
            n_left_brace += 1
        elif i == ')':
            n_right_brace += 1
        if n_right_brace > n_left_brace:
            return False

    return True
