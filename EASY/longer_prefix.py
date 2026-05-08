def longer(arr): 
    longer_prefix = list(arr[0])
    for i in range(len(arr) - 1):
        new_prefix = [] 
        for j in range(len(arr[i])): 
            if arr[i][j] == arr[i+1][j]:
                new_prefix.append(longer_prefix[j])
            else: 
                break
        longer_prefix = new_prefix 
    return longer_prefix
