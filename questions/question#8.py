a = int(input())
LoP = []
for i in range(a):
    x = input()
    LoP.append(x)
for each in range(a):
    x = LoP[each].count('(')
    y = LoP[each].count(')')
    if x == y:
        print("YES")
    else:
        print("NO")