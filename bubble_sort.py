def new_func():
    coll = [64,87,25,11,90,55,33,81]
    return coll

coll = new_func()
n = len(coll)
for i in range(n):
    for j in range(0, n-i-1):
        if coll[j]>coll[j+1]:
            temp =coll[j]
            coll[j+1]=coll[j]
            coll[j]=temp
            print("we have sorted list:",coll)



