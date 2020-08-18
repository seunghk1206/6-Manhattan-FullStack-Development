DataPaper = open("C:/Users/seunghyeon/Documents/GitHub/python_enhanced/CNNproject/datasets_228_482_diabetes.txt", "r", encoding = "utf8")
splitL = [[DataPaper.readline(each)] for each in range(768)]
print(splitL)
#Pregnancies = [each[0] for each in splitL]
#Glucose = [each]
#Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome