def anagramaa(s, t): 
    if len(s) != len(t):
        return False
    
    conteo_s = {}
    conteo_t = {}

    for i in s:
        conteo_s[i] = conteo_s.get(i, 0) + 1
    for i in t:
        conteo_t[i] = conteo_t.get(i, 0) + 1
    
    if conteo_s == conteo_t:
        return True
    return False 