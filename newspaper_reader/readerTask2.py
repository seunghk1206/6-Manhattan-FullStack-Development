import itertools
paper = open("/Users/kimseunghyeon/Desktop/개인적인 것들(?)/CSfile/eng_news_2016_10K-sentences.txt", "r", encoding = "utf8")
# "r", UTF-8,, ./newspaper_reader/eng_news_2016_10K-sentences.txt
no_punct = ""
Dict = {}
Lolines = []
noPuncList = []
tempL = []
Ln2 = []
zero = 0
one = 1
#dict
def replace(listAccept, listRecieve, whichOne):
    for each in listAccept:
        listRecieve.append(each.split(whichOne))
    listAccept.clear()
    dummy = list(itertools.chain(*listRecieve))
    listRecieve.clear()
    for i in dummy:
        listRecieve.append(i)
for i in range(10000):
    lines = paper.readline(i)
    Lolines.append(lines)
replace(Lolines, tempL, '\t')
replace(tempL, Lolines, '\n')
replace(Lolines, tempL, ',')
replace(tempL, Lolines, '.')
replace(Lolines, tempL, '-')
replace(tempL, Lolines, ':')
replace(Lolines, tempL, ';')
replace(tempL, Lolines, '1')
replace(Lolines, tempL, '2')
replace(tempL, Lolines, '3')
replace(Lolines, tempL, '4')
replace(tempL, Lolines, '5')
replace(Lolines, tempL, '6')
replace(tempL, Lolines, '7')
replace(Lolines, tempL, '8')
replace(tempL, Lolines, '9')
replace(Lolines, tempL, ')')
replace(tempL, Lolines, '(')
replace(Lolines, tempL, '@')
replace(tempL, Lolines, '"')
replace(Lolines, tempL, "'")
replace(tempL, Lolines, '~')
replace(Lolines, tempL, '`')
replace(tempL, Lolines, '?')
replace(Lolines, tempL, '—')
replace(tempL, Lolines, '’')
replace(Lolines, tempL, '!')
replace(tempL, Lolines, '0')
replace(Lolines, tempL, '|')
replace(tempL, Lolines, '‘')
replace(Lolines, tempL, '/')
replace(tempL, Lolines, '“')
for line in Lolines:
    tempL.append(line.split(' '))
for i in range(len(tempL)//2):
    Ln2.append([tempL[0], tempL[1]])
    tempL.remove(tempL[0])
    tempL.remove(tempL[0])
for each in Ln2:
    try:
        Dict[each[0], each[1]] += 1
    except:
        Dict[each[0], each[1]] = 1
print(Dict)