str = input()
n = int(input())
lis = list(str)
k = 0
for i in range(0 , len(lis)):
    if lis[i] == ',':
        lis[i] = '.'
        continue
    if lis[i] == '.':
        lis[i] = ','
        continue
    if lis[i] == ' ':
        continue
    
    if k < n:
        if ord(lis[i]) >= 65 and ord(lis[i]) <= 90:
            lis[i] = chr(ord(lis[i]) + 32)
        k += 1

    else:
        if ord(lis[i]) >= 97 and ord(lis[i]) <= 122:
            lis[i] = chr(ord(lis[i]) - 32)


ans = ''.join(lis)
print(ans)
