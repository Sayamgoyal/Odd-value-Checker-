var1 = ['orange',"apple","banana"] 
def quantity_less_than_one(var1):
    var2 = [] 
    for j in var1: 
        var2.append(var1.count(j)) 
    for i in var1: 
        if var1.count(i) < max(var2): 
            print(i) 
def quantity_more_than_one(var1):
    var2 = [] 
    for j in var1: 
        var2.append(var1.count(j)) 
    for i in var1: 
        if var1.count(i) > min(var2): 
            print(i) 
def odd_value(var1):
    var2 = []
    for i in range(min(var1),max(var1)+1,2):
        var2.append(i)
    print(var2)
    if var1 != var2:
        for j,k in zip(range(len(var1)),range(len(var2))):
            if var1[j] != var2[k]:
                print(var1[j])
                break
def OddStringChecker(var1):
    min_value_string = min(var1, key=var1.count)
    print(min_value_string)
def OddIntChecker(var1):
    for i in var1:
        if type(i) == type('string'):
            continue
        if type(i) == type(1):
            print(i)
            
def Analyzer(var1):
    try:
        quantity_less_than_one(var1)
    except:
        print("NoAnomalyError")
    try:
        quantity_more_than_one(var1)
    except:
        print("NoAnomalyError")
    try:
        odd_value(var1)
    except:
        print("NoAnomalyError")
    try:
        OddStringChecker(var1)
    except:
        print("NoAnomalyError")
    try:
        OddIntChecker(var1)
    except:
        print("NoAnomalyError")
Analyzer(var1)