def pr(x = '\n'):
    print(x)
    pass

def prn(x = '\n'):
    print(x)
    pass

def solution(number, k):
    pos = 0

    while pos < len(number):
        if k <= 0:
            break

        cut = pos
        for i in range(k):
            if pos + (i + 1) >= len(number):
                break

            if number[cut] >= number[pos + (i + 1)]:
                break

            if (pos - 1 >= 0):
                if (number[pos - 1] < number[pos + (i + 1)]):
                    cut = pos + (i + 1)
                    break

            cut = pos + (i + 1)

        if cut != pos:
            pr("delete %d number(s) (%d to %d)" % (cut - pos, pos, cut))
            pr("%s -> %s" % (number, number[:pos] + number[cut:]))
            number = number[:pos] + number[cut:]
            k -= (cut - pos)

            if (pos > 0):
                pos -= 1
        else:
            pos += 1

    if k > 0:
        pr("delete %d number(s) (%d to %d)" % (k, len(number) - k, len(number) - 1))
        pr("%s -> %s" % (number, number[:-k]))
        number = number[:-k]

    return number

prn(solution("1924", 2))          # 94
prn(solution("1231234", 3))       # 3234
prn(solution("4177252841", 4))    # 775841
prn(solution("32134", 2))         # 334
prn()
prn(solution("111", 2))           # 1
prn(solution("321", 2))           # 3
prn()
prn(solution("19", 1))            # 9
prn(solution("91", 1))            # 9
prn(solution("919", 2))           # 9
prn()
prn(solution("919", 1))           # 99
prn(solution("199", 1))           # 99
prn(solution("991", 1))           # 99
prn()
prn(solution("889", 1))           # 89
prn(solution("898", 1))           # 98
prn(solution("988", 1))           # 98
prn()
prn(solution("321999", 4))        # 99
prn(solution("321999", 3))        # 999
prn(solution("321999", 2))        # 3999
prn()
prn(solution("3219199", 4))       # 999
prn(solution("3219199", 3))       # 9199
prn(solution("3249199", 2))       # 49199
prn()
prn(solution("32459199", 3))      # 59199
prn(solution("7532688888", 4))    # 788888
