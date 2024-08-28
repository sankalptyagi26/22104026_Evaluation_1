str = input()
dir = {}
dir['a'] = 0
dir['e'] = 0
dir['i'] = 0
dir['o'] = 0
dir['u'] = 0
lis = list(str)
c = 0
for i in lis:
    ch = ''
    if ord(i) >= 65 and ord(i) <= 90:
        ch = chr(ord(i) + 32)
    else:
        ch = i

    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        c += 1
        dir[ch] += 1

print("Count of vowels : " , c)
res = []
for i in dir:
    if dir[i] > 0:
        res.append(i)

print("Unique Vowels : " , res)
