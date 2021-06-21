word = input()
result = [-1]*26

for i in range(26) :
    for idx, w in enumerate(word):
        if i == (ord(w)-97) and result[i] == -1:
            result[i] = idx

for i in result:
    print(i, end = " ")