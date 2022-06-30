arr = [2,4,3]
diff_arr = [0]
counter = 0

def solution(arr):
    for i in range (1,len(arr)):
        counter = 0
        for j in range(i,-1,-1):
            if arr[i] < arr[j]:
                counter -= abs(arr[i]-arr[j])
            if arr[i] > arr[j]:
                counter += abs(arr[i]-arr[j])
        diff_arr.append(counter)
    return diff_arr

print(solution(arr))