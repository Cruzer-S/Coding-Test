def solution(name):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = 0

    build = ["A"] * len(name)
    name = list(name)

    cursor = 0

    while build != name:
        if build[cursor] != name[cursor]:
            n = alphabet.index(name[cursor])
            answer += min(n, len(alphabet) - n)
            build[cursor] = name[cursor]

            continue

        lmod, rmod = 0, 0
        lapr, rapr = -1, -1

        idx = 1
        while idx <= (len(name) // 2):
            if (build[cursor - idx] != name[cursor - idx]):
                if (lapr == -1):
                    lapr = idx

                lmod = idx

            if (build[(cursor + idx) % len(name)] != name[(cursor + idx) % len(name)]):
                if (rapr == -1):
                    rapr = idx

                rmod = idx

            idx += 1

        if (lmod == 0):
            answer += rapr
            cursor = cursor + rapr
        elif (rmod == 0):
            answer += lapr
            cursor = cursor - lapr
        else:
            if (lmod < rmod):
                answer += lapr
                cursor = cursor - lapr
            elif (lmod > rmod):
                answer += rapr 
                cursor = cursor + rapr
            else:
                if (lapr < rapr):
                    answer += lapr
                    cursor = cursor - lapr
                else:
                    answer += rapr
                    cursor = cursor + rapr

        if cursor >= len(name):
            cursor = cursor % len(name)
        elif cursor < 0:
            cursor = len(name) + cursor

        n = alphabet.index(name[cursor]) 
        answer += min(n, len(alphabet) - n)
        build[cursor] = name[cursor]

    return answer

print(solution("JEROEN")) # 56
print(solution("AAAZZAAAAAAAAAAAZZZZAZA")) # 25 (x) 22 (o)
print(solution("AAAZAAAAAAAAAAAAZZZZZA")) # 18
print(solution("AZAAAAAAAZZZA")) # 10

print(solution("AAAAABAAAA")) # 10

print(solution("A")) # 0
print(solution("AAA")) # 0
print(solution("JAZ")) # 11
print(solution("JAN")) # 23
print(solution("BBBABBB")) # 12
