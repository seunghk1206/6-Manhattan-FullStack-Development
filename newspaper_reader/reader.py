paper = open("")
Dict = {}
eachLine = 0
#dict
lines = paper.read(eachLine)
for eachWord in lines:
    Dict[eachWord] += 1
