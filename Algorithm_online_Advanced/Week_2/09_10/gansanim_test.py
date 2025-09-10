# arr = [69, 30, 10, 2, 16, 8, 32, 21]
# N = len(arr)
# lst = []
# # 병합정렬 : 분할 -> 정복(정렬) -> 병합
#
# # 분할
# mid = N // 2
# print(arr[:mid], arr[mid:])
#
# # 정복
# left = sorted(arr[:mid])
# right = sorted(arr[mid:])
#
# print(left, right)
#
# # 병합
#
# while left and right:
#
#     if left[0] < right[0]:
#         lst.append(left.pop(0))
#
#     else:
#         lst.append(right.pop(0))
#
# lst.extend(left)
# lst.extend(right)
#
# print(lst)

# ==================================================================================

# arr = [69, 30, 10, 2, 16, 8, 32, 21]
# N = len(arr)
#
# def merge_sort(arr):
#     # 기저사례
#     if len(arr) <= 1:
#         return arr
#
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#
#     # 병합
#     lst = []
#
#     while left and right:
#         if left[0] < right[0]:
#             lst.append(left.pop(0))
#
#         else:
#             lst.append(right.pop(0))
#
#     lst.extend(left)
#     lst.extend(right)
#     return lst
#
# sorted_lst = merge_sort(arr)
# print(sorted_lst)

# 퀵 정렬 : 분할 -> 정복(합치는 작업 X)



















