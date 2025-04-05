def solution(phone_book):
    book = dict()
    
    for p in phone_book:
        i = len(p)
        j = 0

        cur = book
        while (j < i):
            d = p[j]
            if d in cur:
                if len(cur[d]) == 0:
                    return False
                if j + 1 == i:
                    return False
            else:
                cur[d] = dict()

            cur = cur[d]
            j += 1

    return True

print(solution(["1195524421", "119", "97674223"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))
