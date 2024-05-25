import random
z = [random.randint(0,10)for i in range(0,100)]
for i in range(len(z)):
    for j in range(len(z)):
        if z[i]<z[j]:
            z[i],z[j] = z[j],z[i]
print(z)            