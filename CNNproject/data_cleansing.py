def chain2D(L):
    return [eachOb for each in L for eachOb in each]
DataPaper = open("C:/Users/seunghyeon/Documents/GitHub/python_enhanced/CNNproject/datasets_228_482_diabetes.txt", "r", encoding = "utf8")
chainedL = chain2D([each.split(',') for each in [DataPaper.readline(each) for each in range(768)]])
#Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
#9