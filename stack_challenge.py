def is_balanced(expression):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack.pop() != bracket_map[char]:
                return False
            else:
             continue
    return not stack

print(is_balanced("({[]})"))   
print(is_balanced("([)]"))     
print(is_balanced("{[()]}"))   
print(is_balanced("{[(])}"))   

    