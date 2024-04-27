liste = [] ; dizi = [] ; dizi1 = [] ;dizi2 = [] ;toplamDizi = [] ; K =[]
sayiListesi = ["A","B","C","D","E","F"] ; sayiKarsiligi = ["10","11","12","13","14","15"]
print("Enter 3 Hexadecimal Numbers")
for i in range(3):
    sayi = input("{}. Enter Number:".format(i + 1))
    liste.append(sayi)

def fonk(value1,value2,value3,say):
    for i in value1:
        a = str(i)
        for x in str(a):
            for y in range(len(sayiListesi)):
                if x == sayiListesi[y]:
                    value1 = sayiKarsiligi[y]
    for i in value2:
        a = str(i)
        for x in str(a):
            for y in range(len(sayiListesi)):
                if x == sayiListesi[y]:
                    value2 = sayiKarsiligi[y]
    for i in value3:
        a = str(i)
        for x in str(a):
            for y in range(len(sayiListesi)):
                if x == sayiListesi[y]:
                    value3 = sayiKarsiligi[y]
    toplam = int(value1) + int(value2) + int(value3)
    if int(toplam) > 16:
        kalan = int(toplam) % 16
        carry = int(toplam) // 16
        if say == 0:
            print("Carry(Hand) End :{} , remainder:{}".format(carry, int(kalan)))
            toplam = kalan
            K.append(carry)
            toplamDizi.append(toplam)
        if say == 1 :
            print("Carry(Hand) End :{} , remainder:{}".format(carry, int(kalan)))
            toplam = kalan + K[0]
            K.append(carry)
            toplamDizi.append(toplam)
        if say == 2 :
            print("Carry(Hand) End :{} , remainder:{}".format(carry, int(kalan)))
            toplam = kalan + K[1]
            K.append(carry)
            toplamDizi.append(toplam)
        if  say ==3:
            print("Carry(Hand) End :{} , remainder:{}".format(carry, int(kalan)))
            toplam = kalan + K[2]
            K.append(carry)
            toplamDizi.append(toplam)
    else:
        toplamDizi.append(toplam)
    print("SUM OF NUMBERS : {}".format(toplam))
say = 0
for x in liste:
    a = str(x)
    for i in str(a):
        say += 1
        if say >= 0 and say <= 4:
            dizi.append(i)
        if say > 4 and say <= 8:
            dizi1.append(i)
        if say > 8 and say <= 12:
           dizi2.append(i)
d = [] ; e = [] ; f = [] ; ters = [] ; toplam = ''
for i in dizi[4:0:-1]:
    d.append(i)
d.append(dizi[0])
for i in dizi1[4:0:-1]:
    e.append(i)
e.append(dizi1[0])
for i in dizi2[4:0:-1]:
    f.append(i)
f.append(dizi2[0])

for i in range(4):
    fonk(d[i],e[i],f[i],i)

for i in toplamDizi[4:0:-1]:
    ters.append(i)
ters.append(toplamDizi[0])
for i in ters:
    toplam = toplam + str(i)
print("The sum of these three numbers: {} ".format(toplam))

#toplam1 = ''
#for i in ters:  # sayıların binarykarşılığı hesaplandı
#    a = str(i)
#    for y in range(len(sayiListesi)):
#        if a == sayiKarsiligi[y]:
#            toplam1 = toplam1 + sayiListesi[y]
#print(toplam1)