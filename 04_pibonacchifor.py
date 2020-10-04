def solution(x):
    answer = 0
    num=0
    answer1=0
    for i in range(x+1): ### x가 0일 때 0을 값으로 가지기 위해 x+1
        if i==0: ###만약 x가 0이면 값은 0
            answer=0
        elif i==1: ###만약 x가 1이면 값은 1
            answer=1
        answer1=answer ##미리 answer가 바뀌기전에 answer1에 값을 저장
        answer=answer+num ##answer는 answer+num으로 정의
        num=answer1### num은 answer1 값을 저장
    return answer1 ###answer1을 리턴
### 재귀함수가 아니라 반복문으로 작성함 만약 F2라면 i가 0일때는 0 1일때는 answer가 1이되고
###answer1은 가장 최근 값이었던 1 num는 전전 값이었던 0이 되어 피보나치 수열이 완성 된다.