import time
import random
import os

write = open("output.csv", "w+", encoding='utf-8')
write.write("Nombre de génération, Nombre d'étapes, x, y, z, seuil")
write.write('\n')

generation = 0
target = 10000
count = 0
moyenne_n = []

while generation < target:
    seuil = random.randint(3000,30000)
    x = random.randint(0,10000)
    y = random.randint(0,10000)
    z = random.randint(0,10000)

    a = random.randint(0,100)
    b = random.randint(0,100)
    c = random.randint(0,100)

    alpha = 0
    beta = 0
    delta = 0
    n = 0
    validité = 0

    if count >= 5:
        count = 0

    while n < 10000000000:
        if n > 100000:
            validité = 1
            break
        x = x + a + alpha
        y = y + b + beta
        z = z + c + delta

        coeff = int((x+y+z)/seuil * 100)

        if coeff > 0 and coeff < 80:
            alpha += 3
            beta += 3
            delta += 3
        elif coeff > 80 and coeff <= 99:
            alpha += 1
            beta += 1
            delta += 1
        elif coeff == 100:
            break
        elif coeff > 100 and coeff < 200:
            alpha -= 1
            beta -= 1
            delta -= 1
        elif coeff > 200:
            alpha -= 10
            beta -= 10
            delta -= 10
        elif coeff < 0:
            alpha += 10
            beta += 10
            delta += 10
        n += 1
    #print("Il a fallu ", n, "étapes pour arriver à la stabilité")
    #print("Les coefficients sont : ")
    #print("x : ", x)
    #print("y : ", y)
    #print("z : ", z)
    #print("seuil : ", seuil)
    #print("validité : ", validité)
    moyenne_n.append(n)


    if validité == 0:
        write.write(str(generation))
        write.write(",")
        write.write(str(n))
        write.write(",")
        write.write(str(x))
        write.write(",")
        write.write(str(y))
        write.write(",")
        write.write(str(z))
        write.write(",")
        write.write(str(seuil))
        write.write('\n')
        generation += 1
    else:
        generation += 1

    pourcentage = (generation / target) * 100
    print(int(pourcentage))
    count += 1

final_m_n = sum(moyenne_n) / len(moyenne_n)
print("La moyenne finale de nombre d'étapes est : ", final_m_n)