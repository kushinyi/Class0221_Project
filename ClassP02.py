gradesTuple=((5,14,7),(23,36,28),(88,80,92))
print('Mathgrades:',gradesTuple[2])
print('AvgMath:',sum(gradesTuple[2])/len(gradesTuple[2]))
print('AvgEnglish:',sum(gradesTuple[1])/len(gradesTuple[1]))
print('AvgChinese:',sum(gradesTuple[0])/len(gradesTuple[0]))
gradesScience=((94,90,96),) #新增自然成績
print(gradesTuple+gradesScience)