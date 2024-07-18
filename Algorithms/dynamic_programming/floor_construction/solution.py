from sys import setrecursionlimit

def tile_place_bt(n):
    # 메모이제이션을 위한 배열 초기화
    if n == 1:
        return 1
    if n == 2:
        return 3

    d = [0] * (n + 1)
    d[1] = 1
    d[2] = 3

    # 작은 문제부터 큰 문제로 해결
    for i in range(3, n + 1):
        d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

    # 계산된 결과 반환
    return d[n]

def tile_place_memo(n):
    setrecursionlimit(10 ** 6)
    # 메모이제이션을 위한 배열 초기화
    memo = [-1] * (n + 1)

    # 기본 케이스 정의
    def dp(x):
        if x == 1:
            return 1
        if x == 2:
            return 3
        if memo[x] != -1:
            return memo[x]
        
        # 점화식 적용
        memo[x] = (dp(x - 1) + 2 * dp(x - 2)) % 796796
        return memo[x]

    # 계산된 결과 반환
    return dp(n)

def answer(n):
    d = [0] * (n + 1)

    d[1] = 1
    d[2] = 3
    for i in range(3, n + 1):
        d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

    # 계산된 결과 반환
    return d[n]

if __name__ == '__main__':

    # N 입력
    N = 11

    # 방법의 수 출력
    print(tile_place_bt(N))
    print(tile_place_memo(N)) 
    print(answer(N)) 