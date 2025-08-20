arr = [69, 10, 30, 16, 8, 31, 2, 22]
N = len(arr)

def find_min(l, r):
    if l == r:
        return l
    else:
        mid = (l + r) // 2
        lmin = find_min(l, mid)
        rmin = find_min(mid+1, r)
        if arr[lmin] < arr[rmin]:
            return lmin
        return rmin

idx = find_min(0, N-1)
print(idx, arr[idx])