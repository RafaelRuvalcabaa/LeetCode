def roma(s):
    values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
    for j in values: 
        print(j, values[j])
    for i in range(len(s)):
        actual = values[s[i]]


roma("IV")