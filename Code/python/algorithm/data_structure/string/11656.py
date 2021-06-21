
word = input()
list = []

for i in range(len(word)):
    list.append(word[i:])

print("\n".join(sorted(list)))