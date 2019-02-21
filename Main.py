mathScores=[60,70,10,20,81,63,41,88,49,56,25,48,1,64,545,548]
print(mathScores[5])
print(mathScores[3:9]) #從第3個到第9個
print(mathScores[-1]) #拿倒數第一個
print(mathScores[:5]) #從第0個拿到第5個
print(mathScores[5:]) #從第5個拿到最後1個
print(mathScores[-6:])
print(len(mathScores)) #長度
print(max(mathScores))
print(min(mathScores))
print(sum(mathScores)/len(mathScores)) #平均

ls=[]
ls.append(4) #append從尾巴放4
print(ls)
ls.insert(1,10)
print(ls) #insert指定要放哪個位置

mathScores=[10,235,8482,52,53,99,18,20,35]
del mathScores[1:3]
print(mathScores)
mathScores.remove(10) #刪掉某數
print(mathScores)
mathScores[2]=1
print(mathScores)
print(2 in mathScores) #看2有沒有在集合裡面
print(10 in mathScores)
print(mathScores.count(10)) #數某數有幾個

ls=['a','b','c']
print(mathScores+ls)

ls=[[1,3],[6,5]] #雙層list
print(ls[0][0]) #第一個0是外層,第二個0是內層
print(ls[1][0])
print(sorted(mathScores)) #由小排到大

#tuple
#tuple1=(1,2,3,4,5)
#tuple2='1','2','3','4','5'
#tuple[3] #取得tuple中的某個元素
#tuple1.index('4')
#print(tuple1+tuple2)

#tuple3=('Lisa',23,'Female')
#name,age,sex=tuple3
#print(name,age,sex)
#print(tuple3[0:2])

#Dictionary
family={}
family['dad']='Homer'
print(family)
family['dad']='Andy'
print(family)

print(family.get('mom'))
print(family.pop('dad')) #把dad丟出來並print

family.update({'mom':'Lisa','son':'Bob'})
print(family)

#Set
