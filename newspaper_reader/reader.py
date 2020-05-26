paper = open("")
Dict = {}
eachLine = 0
#dict
for i in range(10000):
    lines = paper.read(eachLine)
    L1 = list(lines.split(" "))
    for eachWord in L1:
        Dict[eachWord] += 1
