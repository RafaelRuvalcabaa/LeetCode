def plusOne(digits):
    right = len(digits) - 1
    while right >= 0:
        if digits[right] == 9:
            digits[right] = 0
            right -= 1
        else:
            digits[right] += 1
            return digits
    digits.insert(0, 1)
    return digits
