a = int(input())
LoP = []
LoP2 = []
countA = 0
countB = 0
for i in range(a):
    x = input()
    LoP.append(x)

for each in range(a):
    if LoP[each][0] == ')':
        print("NO")
    else:
        for i in LoP[each]:
            if i == '(':
                try:
                    LoP.remove(i)
                    LoP.remove(')')
                except:
                    if len(LoP) == 0:
                        print("YES")
                    else:
                        print("NO")
                    break
#
'''
))((()))
()(())
'''