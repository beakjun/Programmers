def solution(L, x):
    answer = []
    for i in range(len(L)):
        if L[i] == x: ### 처음부터 하나하나 비교하며 같으면
            answer.append(i) ### i 즉 몇번째인지 찾아냄
    if len(answer) == 0: ### 만약 몇번째 인지 못찾는다 즉 x가 L의 원소가 아닐 때
        return [-1] ### [-1]의 리스트를 답으로 리턴함

    return answer