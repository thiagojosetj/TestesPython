n = int(input())

t = list(map(int, input().split()))

count = 1

if n > 0:
    for i in range(n):
        j = 2
        count = 1
        while j <= t[i]:
            if(t[i] % j == 0):
                count += 1
            j += 1
            if(count > 3):
                break
        if count == 3:
            print("YES")
        else:
            print("NO")
else:
    print("NO")