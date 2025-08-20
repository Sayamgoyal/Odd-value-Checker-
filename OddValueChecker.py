var1 = [1,3,5,6,7,9] 
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
def even_number_check(var1):
    var2 = []
    for n in range(1,max(var1)+1,2):
        var2.append(n)
        for i in var1:
            if i != n:
                print(i,n)
                break
                
        
            
even_number_check(var1)