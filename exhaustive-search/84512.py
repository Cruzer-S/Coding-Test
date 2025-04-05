alphabet = ['A', 'E', 'I', 'O', 'U']

def solution(word):
    digit = ""
    n = 0

    while word != digit:
        if len(digit) < 5:
            digit += "A"
            n += 1
            continue

        index = alphabet.index(digit[-1]) + 1
        if (index >= len(alphabet)):
            while len(digit) > 1 and digit[-1] == 'U':
                digit = digit[:-1]

                if (digit[-1] != 'U'):
                    idx = alphabet.index(digit[-1]) + 1
                    digit = digit[:-1]
                    digit += alphabet[idx]
                    break
        else:
            digit = digit[:-1] + alphabet[index]

        n += 1

    return n

print(solution("UUUUU"))
