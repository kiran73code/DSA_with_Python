def isValid(s: str) -> bool:
    map = {"(":")",
            "{":"}",
            "[":"]"
            }
    if len(s) == 1:
        return False
    stack = []
    for c in range(len(s)):
        char = s[c]
        if char in map:
            stack.append(map[char])
        else:
            if len(stack) == 0 :
                return False
            check = stack[-1]
            if check == char :
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    s = "()"
    print(isValid(s))