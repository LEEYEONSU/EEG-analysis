
line = list(input())
result = ''

for l in line:
    if 'a' <= l <= 'z':
        result += chr(ord(l)+13 if l <= 'm' else ord(l)-13)
    elif 'A' <= l <= 'Z':
        result += chr(ord(l)+13 if l <= 'M' else ord(l)-13)
    else:
        result += l
print(result)