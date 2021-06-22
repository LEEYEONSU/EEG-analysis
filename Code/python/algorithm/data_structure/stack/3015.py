
N = int(input())
heights = [int(input()) for _ in range(N)]

stack = []
ans = 0

for h in heights:
    while stack and stack[-1][0] < h :
        ans += stack.pop()[1]

    if not stack :
        stack.append((h, 1))

    else :
        if stack[-1][0] == h:
            cnt = stack.pop()[1]
            ans += cnt

            if stack:
                ans += 1

            stack.append((h, cnt + 1))

        else :
            stack.append((h, 1))
            ans += 1

print(ans)


