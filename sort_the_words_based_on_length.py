s=sorted(input().split())
s.sort(key=len)
print(*s)