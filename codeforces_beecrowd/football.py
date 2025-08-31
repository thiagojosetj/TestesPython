import sys

players = input()

if len(players) == 0 or "1" not in players or "0" not in players:
    sys.exit()

if "1111111" in players or "0000000" in players:
    print("YES")
else:
    print("NO")