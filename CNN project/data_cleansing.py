DataPaper = open("./newspaper_reader/eng_news_2016_10K-sentences.txt", "r", encoding = "utf8")
Lolines = [DataPaper.readline(each) for each in range(1, 768)]
