def readfile(namafile):
    global graf, grafsimpul, banyaksimpul, bobot;
    file = open("./test/"+ namafile + ".txt", "r")
    banyaksimpul = int(file.readline());
    #print("Banyak Simpul : ", banyaksimpul)
    grafsimpul = file.readline()
    graf = file.readlines()
    #print(grafsimpul);
    #print(graf)

def ceksimpul():
    global simpul;
    simpul = []
    huruf = ''
    isiSimpul = ''
    for i in range(len(grafsimpul)):
        for j in range(len(grafsimpul[i])):
            if (grafsimpul[i][j] == ','):
                simpul += [huruf]
                huruf = ''
            elif (grafsimpul[i][j] == '\n'):
                simpul += [huruf]
            elif (grafsimpul[i][j] != ','):
                huruf += grafsimpul[i][j]

def isimatriks():
    global hasil;
    b = ''
    isi = []
    hasil = []
    bobotpersimpul = []
    for i in range(banyaksimpul):
        for j in range(len(graf[i])):
            if (graf[i][j] == ','):
                bobotpersimpul += isi
                b = ''
                #print("BOBOTPERSIMPUL : ", bobotpersimpul)
            elif (graf[i][j] == '\n'):
                hasil += [bobotpersimpul]
                bobotpersimpul = []
            elif (graf[i][j] != ','):
                b += graf[i][j]
                isi = [b]
                #print("ISI : ", isi)    

def grafindict():
    global grafberbobot
    grafberbobot = []
    akhir = []
    for i in range(banyaksimpul):
        akhir += [(simpul[i], hasil[i])]
        #akhir += [(simpul[i], i)]
        
    grafberbobot = dict(akhir)

def grafberbobotberpasangan():
    global g;
    g = []
    for i in range(banyaksimpul):
        for j in range(0+i, banyaksimpul):
            if (hasil[i][j] != '-1' and hasil[j][i] != '-1'):
                if (hasil[i][j] == hasil[j][i]):
                    g += [(simpul[i], simpul[j], int(hasil[i][j]))]
                else:
                    continue;
            else:
                continue;

#Algoritma Utama
namafile = input("Masukkan file graf : " );
readfile(namafile)

ceksimpul()
#print(simpul)

isimatriks()
#print(hasil)

grafindict()
#print(grafberbobot)

grafberbobotberpasangan()
#print(g)

