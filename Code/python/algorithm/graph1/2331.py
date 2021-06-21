
A, P = map(int, input().split())
D = [A]
i = 0

while 1:

    Alist = list(str(D[i]))
    tmp = 0
    for x in Alist:
        tmp += int(x) ** P
    
    if D.count(tmp) > 0:
        answer = D.index(tmp)
        break
    else:
        D.append(tmp)
    
    i += 1

print(answer)