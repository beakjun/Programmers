def solution(L, x):
    answer = -1
    down = 0
    upper = len(L) - 1 ### 인덱스로 사용하기에 길이에 -1
    middle = 0
    while down <= upper: ### 하한이 상한보다 작거나 같을 때
        middle = down + (upper - down) // 2 ### 이진탐색을 구현하기 위해 중간 인덱스를 구함

        if L[middle] == x: ### 만약 리스트의 중간 값이 x와 같다면
            return middle ###답으로 middle의 인덱스 값을 리턴
        elif down == upper: ## down과 upper가 같다면 리스트의 길이가 0이므로
            return -1 ###답으로 -1 즉 에러 리턴
        elif L[middle] < x: ### 리스트의 중간 값이 x 보다 작다면
            down = middle + 1 # 리스트의 중간부분 바로 앞부터 다시 탐색하기 위해 down값 조정
        else:
            upper = middle - 1 ## 반대의 경우 중간부분 바로전 부분 부터 다시 탐색하기 위해 upper값 조정
    return answer