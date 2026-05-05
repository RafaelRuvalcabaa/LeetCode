def palindrome(arr): 
    for i in range(len(arr)//2): 
        if arr[i] != arr[-1-i]:
            return f"No es palindromo: {arr}" 
        
    return f"Es palindromo: {arr}"
        

print(palindrome([121]))

def anotherpali(arr): 
    if arr != arr[::-1]:
        return False
    else:
        return True
    
def other(arr):
    return arr == arr[::-1]

print(other([121]))