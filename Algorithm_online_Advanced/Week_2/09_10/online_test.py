
def binary_search_while(target):
    left = 0                # 검색 시작점
    right = len(arr) - 1    # 검색 끝점
    cnt = 0
    check = ""

    while left <= right:    # 교차가 되면 못 찾은것
        mid = (left + right) // 2
        cnt += 1

        if arr[mid] == target:
            return mid, cnt  # mid 위치에 존재한다고 return

        # target 보다 왼쪽에 있는 경우
        if target < arr[mid]:
            right = mid - 1
            check += 'L'

        # target 보다 오른쪽에 있는 경우
        else:
            left = mid + 1
            check += 'R'
        # 못 찾은경우
        return -1, cnt

arr = [4, 2, 9, 7, 11, 23, 19]

# 이진 검색은 항상 정렬된 데이터에 사용
arr.sort()


print(f'9 = {binary_search_while(9)}번째에 위치') # 처음과 끝을 전달
