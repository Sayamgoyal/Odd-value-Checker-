var1 = [1,1,2,2,3,4,4]
def quantity_less_than_one(var1):
    var2 = []
    for i in var1:
        var2.append(var1.count(i))
        if var1.count(i) < max(var2):
            print(i)
    