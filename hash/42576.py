def solution(participant, completion):
    pt = dict()
    
    for p in participant:
        if p in pt:
            pt[p] += 1
        else:
            pt[p] = 1
            
    for c in completion:
        if c in pt:
            pt[c] -= 1

            if pt[c] == 0:
                del pt[c]

    return next(iter(pt))
