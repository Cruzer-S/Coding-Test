def solution(s):
    stack = list()

    for b in s:
        if b == '(':
            stack.append(b)
            continue

        if (len(stack) == 0):
            return False

        if (stack[-1] != '('):
            return False

        stack.pop()

    return len(stack) == 0

print(solution("()()"))
print(solution("(())()""(())()"))
print(solution(")()("))
print(solution("(()("))
