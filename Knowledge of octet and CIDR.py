print("""
  Menü
    1-> Writing octets of the given IP address
    2-> Calculating network address with given IP address and CIDR information
   """)
sec = int(input("Make Your Menu Selection:"))
if sec == 1:
    oktet = [] ;toplam = '' ; a = 1
    girdi = str(input("IP Address to Enter:"))
    for i in girdi:
        if i == '.' or  i == ' ':
            oktet.append(toplam)
            toplam = ''
        else:
            toplam = toplam + str(i)
    print("Octets of given IP: {}".format(oktet))
    for j in oktet:
        print("{} Binary Mixture of Octet: {:b}".format(a,int(j)))
        a += 1
if sec == 2:
    ıpadresi = [] ; toplam = '';  a = 1 ; ıptoplam = [] ; cıdrdizi =[] ; agıp = []
    adresi = str(input("IP Address to Enter:"))
    cıdr = str(input("CIDR Information of the IP Address to be entered (24/16/8):"))
    for i in adresi:
        if i == '.' or i == ' ':
            ıpadresi.append(toplam)
            toplam = ''
        else:
            toplam = toplam + str(i)
    for j in ıpadresi:
        gecici = "{:b}".format(int(j))
        ıptoplam.append(gecici)
    print("Entered IP {} and the Binary Equivalent of the IP Address: {}".format(ıpadresi,ıptoplam))
    if cıdr == "24":
        cıdr24 = ['255','255','255','0'] ;
        ıpadresi[3]='0'
        for j in cıdr24:
            gecici = "{:b}".format(int(j))
            cıdrdizi.append(gecici)
        print("Binary Equivalent of the entered CIDR Address (255,255,255,255,0): {}".format(cıdrdizi))
        cıdr = ['0', '0', '0', '0']
        def topla(a, b):
            a = a + b
            return a
        for i in range(len(ıpadresi)):
            x = int(cıdr[i])
            y = int(ıpadresi[i])
            agıp.append(topla(x, y))
        print("Network Address After Information Provided: {}".format(agıp))
    if cıdr == "16":
        cıdr24 = ['255', '255', '0', '0']
        ıpadresi[2] = '0' ; ıpadresi[3] = '0'
        for j in cıdr24:
            gecici = "{:b}".format(int(j))
            cıdrdizi.append(gecici)
        print("Binary Equivalent of the Entered CIDR Address(255,255,255,0,0): {}".format(cıdrdizi))
        cıdr = ['0', '0', '0', '0']
        def topla(a, b):
            a = a + b
            return a
        for i in range(len(ıpadresi)):
            x = int(cıdr[i])
            y = int(ıpadresi[i])
            agıp.append(topla(x, y))
        print("Network Address After Information Provided: {}".format(agıp))
    if cıdr == "8":
        cıdr24 = ['255', '0', '0', '0']
        ıpadresi[1] = '0'; ıpadresi[2] = '0'; ıpadresi[3] = '0'
        for j in cıdr24:
            gecici = "{:b}".format(int(j))
            cıdrdizi.append(gecici)
        print("Binary Equivalent of the Entered CIDR Address(255,0,0,0,0): {}".format(cıdrdizi))
        cıdr = ['0', '0', '0', '0']
        def topla(a, b):
            a = a + b
            return a
        for i in range(len(ıpadresi)):
            x = int(cıdr[i])
            y = int(ıpadresi[i])
            agıp.append(topla(x, y))
        print("Network Address After Information Provided: {}".format(agıp))