def solution(L, x):
    answer = []
    for i in range(len(L)):
        if max(L) < x:
            L.insert(len(L), x)
        elif L[i] > x:
            L.insert(i, x)
            break

    answer = L
    return answer