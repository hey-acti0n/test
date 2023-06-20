def f(s):
    ok=True
    l=len(s)//2
    for i in range(l):
        if s[i]!=s[len(s)-i-1]:
            ok=False
    return ok


s=input()
print(f(s))