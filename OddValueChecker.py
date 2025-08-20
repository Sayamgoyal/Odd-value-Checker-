var1 = [1,2,3,4,4,5] 
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
            break
quantity_more_than_one(var1)
        
    