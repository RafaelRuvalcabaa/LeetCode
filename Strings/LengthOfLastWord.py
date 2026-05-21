def lengthOfLastWord(s):
    counter = 0
    right = len(s) - 1
    while right >= 0 and s[right] == " ":
        right -= 1
    while right >= 0 and s[right] != " ":
        counter += 1
        right -= 1
    return counter
