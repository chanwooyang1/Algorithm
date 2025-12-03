def solution(myString, pat):
    lower_mystring = myString.lower()
    lower_pat = pat.lower()
    
    return 1 if lower_pat in lower_mystring else 0