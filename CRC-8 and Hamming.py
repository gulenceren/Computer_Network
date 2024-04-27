while True:
    import random
    print("""
        1 => CRC (1)
        2 => HAMMİNG (2)
    """)
    def binaryCevirme(num):
        sayilar = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        binaryKarsiligi = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010","1011", "1100", "1101", "1110", "1111"]
        dizi = [] ; toplam = ''
        for i in num:  # sayıların binarykarşılığı hesaplandı
            for y in range(len(sayilar)):
                if str(i) == sayilar[y]:
                    dizi.append(binaryKarsiligi[y])
                    toplam = toplam + binaryKarsiligi[y]
        print("Binary Translated: {}".format(toplam))
        return toplam
    def bozukBitKontrolu(sayi, uret, dizi):
        for i in range(sayi):
            if int(uret) == i:
                x = sayi - i
                if int(dizi[x]) == 0:
                    dizi[x] = 1
                else:
                    dizi[x] = 0
                break
        sonuc1 = ''
        for i in dizi:
            sonuc1 = sonuc1 + str(i)
            sonuc1 = sonuc1 + ' '
        print(" CORRUPT DATA => {}".format(sonuc1))
    def crcBaslangicKontrolu(dizi, islemDizisi, olusanDizi): # Başlangıç kontrolü yani crc ile ilk hessaplama
        for i in range(len(dizi)):
            a = islemDizisi[i]
            if a == dizi[i]:
                b = 0
                olusanDizi.append(b)
            else:
                b = 1
                olusanDizi.append(b)
    def yaz(dizi):
        toplam = ' '
        for i in dizi:
            toplam = toplam + str(i)
            toplam = toplam + ' '
        return toplam
    secim = input("Please Make a Choice ")
    if secim == "1" or secim == "CRC" or secim == "crc":
        print("--------------CRC METHOD and ERROR DETECTION-------------")
        num = input("HexaDecimal Enter a Number (32 Bit. For example F0F0F0F0F0F0) ")
        crc8 = ["1", "0", "0", "0", "0", "0", "1", "1", "1"]
        crc0 = ["0", "0", "0", "0", "0", "0", "0", "0", "0"]
        islemDizisi = [];toplam1 = ''; crcToplam = '';  olusanDizi = []
        toplam = binaryCevirme(num)
        for i in toplam:  # girilen 32 bitlik sayının binary karşılığını bit bit listeye aktarma ve boşluklu ekrana yazdırma
            islemDizisi.append(str(i))
            toplam1 = toplam1 + str(i)
            toplam1 = toplam1 + ' '
        toplam1 = toplam1 + '  '
        for i in range(len(crc8) - 1):  # Derecesi en yüksek olan - 1 kadar 0 konulur
            islemDizisi.append('0')
            toplam1 = toplam1 + '0 '
        print("DATAWORD   => {}".format(toplam1))
        crcToplam = yaz(crc8)
        print("Crc-8      => {}".format(crcToplam))
        crcBaslangicKontrolu(crc8,islemDizisi,olusanDizi) # Başlangıç kontrolü yani crc ile ilk hessaplama
        sayac = 9
        while sayac <= len(islemDizisi) - 1:  # İlk bit kontrol edilerek crc-8 ya da 000... lanmış hali ile crc hesaplama kodları
            s = olusanDizi[1]
            olusanDizi.remove(0)
            olusanDizi.append(int(islemDizisi[sayac]))
            dizi1 = []
            for k in olusanDizi:
                dizi1.append(k)
            olusanDizi = []
            if s == 1:
                for j in range(len(crc8)):
                    x = dizi1[j]
                    z = crc8[j]
                    if x == int(z):
                        olusanDizi.append(0)
                    else:
                        olusanDizi.append(1)
            if s == 0:
                for j in range(len(crc8)):
                    x = dizi1[j]
                    z = crc0[j]
                    if x == int(z):
                        olusanDizi.append(0)
                    else:
                        olusanDizi.append(1)
            sayac += 1
        diziToplam = '' ; olusanDizi.remove(0)
        for i in olusanDizi:  # İşlemler sonrasında oluşan crc`i yazdırma kodları
            a = str(i)
            diziToplam = diziToplam + a
        print("Resulting CRC => {}".format(diziToplam))
        sonuc = toplam + diziToplam
        top = yaz(sonuc)
        print(" CODEWORD = DATA + CRC => {}".format(top))
        kontrolDizisi = [] ; olusanDizi = []
        for k in sonuc:
            kontrolDizisi.append(k)
        uret = random.randint(0, len(kontrolDizisi) - 1)
        print("{}.Biti is Sending Corrupted".format(uret))
        bozukBitKontrolu(40, uret, kontrolDizisi)
        print("--------------BEING CHECKED-------------")
        crcBaslangicKontrolu(crc8,kontrolDizisi,olusanDizi) # Başlangıç kontrolü yani crc ile ilk hessaplama
        sayac = 9
        while sayac <= len(kontrolDizisi) - 1:  # İlk bit kontrol edilerek crc-8 ya da 000... lanmış hali ile crc hesaplama kodları
            s = olusanDizi[1] ; olusanDizi.remove(0) ; dizi1 = []
            olusanDizi.append(int(kontrolDizisi[sayac]))
            for k in olusanDizi:
                dizi1.append(k)
            olusanDizi = []
            if s == 1:
                for j in range(len(crc8)):
                    x = dizi1[j]
                    z = crc8[j]
                    if x == int(z):
                        olusanDizi.append(0)
                    else:
                        olusanDizi.append(1)
            if s == 0:
                for j in range(len(crc8)):
                    x = dizi1[j]
                    z = crc0[j]
                    if x == int(z):
                        olusanDizi.append(0)
                    else:
                        olusanDizi.append(1)
            sayac += 1
        diziToplam = '' ; olusanDizi.remove(0)
        for i in olusanDizi:  # İşlemler sonrasında oluşan crc`i yazdırma kodları
            diziToplam = diziToplam + str(i)
        print("Resulting CRC => {}".format(diziToplam)) ; print()
        cikis = input("Press 'q' or 'Q' to Exit. Press Any Key to Continuez ")
        if cikis in ("q", "Q"):
            break
    if secim == "2" or secim == "HAMMİNG" or secim == "hamming":
        print("--------------HAMMING METHOD and ERROR DETECTION-------------")
        num = input("HexaDecimal Enter a Number (28 Bits, e.g. 57ACEFA) ")
        toplam = binaryCevirme(num) ; hamming = [] ; hammingDizi = []
        for i in toplam:  # girilen 32 bitlik sayının binary karşılığını bit bit listeye aktarma ve boşluklu ekrana yazdırma
            a = str(i)
            hamming.append(a)
        hammingDizi = [hamming[0], hamming[1], 'r32', hamming[2], hamming[3], hamming[4], hamming[5], hamming[6],hamming[7], hamming[8],
                       hamming[9],hamming[10], hamming[11], hamming[12], hamming[13], hamming[14], hamming[15], hamming[16], 'r16',
                       hamming[17], hamming[18],hamming[19], hamming[20], hamming[21], hamming[22], hamming[23], 'r8', hamming[24],
                       hamming[25],hamming[26], 'r4',hamming[27], 'r2', 'r1']
        def hammingFonk(hammingDizi):
            top = ''
            for i in hammingDizi:
                top = top + str(i)
                top = top + ' '
            print(" CODEWORD  => {}".format(top))
        def hammingDuzeltme(say, k,
                            hammingDizi):  # 1 lerin sayısı tek ise gelen redünansı 1 yapar değilse 0 yapan kod fonksiyonu
            if say % 2 == 1:
                hammingDizi[k] = 1
            else:
                hammingDizi[k] = 0
            hammingFonk(hammingDizi)
        def hammingR2(sayac, say, kontrolSayi):  # R2 için Kontrol Kodları
            while sayac >= kontrolSayi:
                a = hammingDizi[sayac]
                if str(a) == '1':
                    say += 1
                sayac -= 4  # 4 azaltmasının sebebi önce 28 den başlayıp 4`er kaymaya denk geldiği için 0`a kadar baktı aynı şekilde 31 içinde gecerlidir
            return say
        def hammingR4veDigerleri(sayac, say, kontrolSayi):  # R4 ,R8,R16 ve R32 için Kontrol Kodları
            while sayac > kontrolSayi:
                a = hammingDizi[sayac]
                if str(a) == '1':
                    say += 1
                sayac -= 1
            return say
        hammingFonk(hammingDizi)  # Oluşan Redünans ile gösterilmesi için yazdırma fonksiyonuna gönderilir
        sayac = 31 ; say = 0  # R1 için kontrol edilmesi
        while sayac >= 1:
            a = hammingDizi[sayac]
            if str(a) == '1':
                say += 1
            sayac -= 2
        print("Number 1 for r1 => {}".format(say))
        hammingDuzeltme(say, 33, hammingDizi)
        say = hammingR2(28, 0, 0)  # R2`nin fonksiyona gönderiliş hali
        k = hammingR2(31, say, 0)
        print("Number 1 for r2 => {}".format(k))
        hammingDuzeltme(k, 32, hammingDizi)
        say = hammingR4veDigerleri(29, 0, 26)  # R4`ün fonksiyona gönderiliş hali
        k = hammingR4veDigerleri(22, say, 18)
        say = hammingR4veDigerleri(14, k, 10)
        k = hammingR4veDigerleri(6, say, 2)
        print("Number 1 for r4 => {}".format(k - 1))
        hammingDuzeltme(k, 30, hammingDizi)
        say = hammingR4veDigerleri(25, 0, 18)  # R8`in fonksiyona gönderiliş hali
        k = hammingR4veDigerleri(10, say, 2)
        print("Number 1 for r8 => {}".format(k))
        hammingDuzeltme(k, 26, hammingDizi)
        say = hammingR4veDigerleri(17, 0, 2)  # R16`nın fonksiyona gönderiliş hali
        print("Number 1 for r16 => {}".format(say))
        hammingDuzeltme(say, 18, hammingDizi)
        say = hammingR4veDigerleri(1, 0, -1)  # R32`nin fonksiyona gönderiliş hali
        print("Number 1 for r32 => {}".format(say))
        hammingDuzeltme(say, 2, hammingDizi)
        uret = random.randint(0, len(hammingDizi) - 1)
        print("BAD SENT BIT => {}".format(uret))
        bozukBitKontrolu(34, uret, hammingDizi)
        print("--------------BEING CHECKED-------------") ; dizi = []
        def kontrol(say):
            if say % 2 == 1:
                dizi.append(1)
            else:
                dizi.append(0)
        say = hammingR4veDigerleri(2, 0, -1)  # R32
        kontrol(say)
        say = hammingR4veDigerleri(18, 0, 2)  # R16
        kontrol(say)
        say = hammingR4veDigerleri(26, 0, 18)  # R8
        k = hammingR4veDigerleri(10, say, 2)
        kontrol(k)
        say = hammingR4veDigerleri(30, 0, 26)  # R4
        k = hammingR4veDigerleri(22, say, 18)
        say = hammingR4veDigerleri(14, k, 10)
        k = hammingR4veDigerleri(6, say, 2)
        kontrol(k)
        say = hammingR2(32, 0, 0)  # R2
        k = hammingR2(31, say, 0)
        kontrol(k) ; sayac = 33 ;  say = 0  # R1
        while sayac >= 1:
            a = hammingDizi[sayac]
            if str(a) == '1':
                say += 1
            sayac -= 2
        kontrol(say) ; top = ' '
        for i in dizi:
            top = top + str(i)
        print("ERROR DETECTİON => {}".format(top))
        us = 6 ; sonuc = 0
        for i in dizi:
            for j in range(us):  # us alma
                top = int(i) * (2 ** j)
            sonuc = sonuc + top
            us = us - 1
        print("faulty bit resulting from error detection => {} ".format(sonuc)) ; print()
        cikis = input("Press 'q' or 'Q' Key to Exit. Press Any Key to Continue. ")
        if cikis in ("q", "Q"):
            break