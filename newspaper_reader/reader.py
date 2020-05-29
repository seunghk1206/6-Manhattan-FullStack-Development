paper = open("./newspaper_reader/eng_news_2016_10K-sentences.txt", "r", encoding = "utf8")
# "r", UTF-8
no_punct = ""
Dict = {}
Lolines = []
noPuncList = []
#dict
def PuncRemove(st):
    punctuations = '''!@#$%^&*()_-=+[]:;"'<>,./?'''
    for i in st.lower():
        if i in punctuations:
            st = st.replace(i, " ")
    return st
for i in range(10000):
    lines = paper.readline(i)
    Lolines.append(lines)
for i in range(len(Lolines)):
    noPuncList.append(PuncRemove(Lolines[i]))
noIntList = []
dsd = ''.join([i for i in noPuncList if not i.isdigit()])
noIntList.append(dsd)
noNewLineList = []
for each in noIntList:
    noNewLineList.append(each.split('\t'))
for each in noNewLineList:
    noNewLineList[noNewLineList.index(each)] = noNewLineList[noNewLineList.index(each)].split('\n')
for each in range(len(noNewLineList)):
    dummy = list(noNewLineList[each].split(" "))
    for eachWord in dummy:
        try:
            Dict[eachWord] += 1
        except:
            Dict[eachWord] = 1
print(Dict)
# readline