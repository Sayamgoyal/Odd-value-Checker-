var1 = [2,3,4,6,8] 
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
def even_number_check(var1):
    var2 = []
    for i in range(min(var1),max(var1)+1,2):
        var2.append(i)
    print(var2)
    if var1 != var2:
        for j,k in zip(range(len(var1)),range(len(var2))):
            if var1[j] != var2[k]:
                print(var1[j])
                break
def odd_number_checker(var1):
    var2 = []
    for i in range(min(var1),max(var1)+1,2):
        var2.append(i)
    print(var2)
    if var1 != var2:
        for j,k in zip(range(len(var1)),range(len(var2))):
            if var1[j] != var2[k]:
                print(var1[j])
                break
even_number_check(var1)