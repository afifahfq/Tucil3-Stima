def readfile(namafile):
    global graf, grafsimpul, banyaksimpul, bobot
    file = open("../test/"+ namafile + ".txt", "r")
    banyaksimpul = int(file.readline())
    print("Banyak Simpul : ", banyaksimpul)
    grafsimpul = file.readline()
    graf = file.readlines()
    #print("grafsimpul:", grafsimpul)
    #print("graf:", graf)

def ceksimpul():
    global simpul
    '''
    print(simpul)
    output : ['jawa', 'sumatra', 'bali', 'papua', 'sulawesi', 'mamuju', 'ternate', 'kalimantan']
    '''
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
    splitsimpul()

def splitsimpul():
    newsimpul = [char for char in simpul[0]]
    simpul.clear()
    simpul.extend(newsimpul)
    #print("newsimpul:", newsimpul)

def isimatriks():
    global hasil
    '''
    print(hasil) -> matriks
    output : [['-1', '2', '-1', '-1', '-1', '1', '-1', '-1'], ['2', '-1', '2', '2', '4', '-1', '-1', '-1'], ['-1', '2', '-1', '-1', '3', '-1', '-1', '1'], ['-1', '2', '-1', '-1', '4', '3', '-1', '-1'], ['-1', '4', '3', '4', '-1', '-1', '7', '-1'], ['1', '-1', '-1', '3', '-1', '-1', '5', '-1'], ['-1', '-1', '-1', '-1', '7', '5', '-1', '6'], ['-1', '-1', '1', '-1', '-1', '-1', '6', '-1']]
    '''
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
    '''
    print(grafberbobot)
    output : {'jawa': ['-1', '2', '-1', '-1', '-1', '1', '-1', '-1'], 'sumatra': ['2', '-1', '2', '2', '4', '-1', '-1', '-1'], 'bali': ['-1', '2', '-1', '-1', '3', '-1', '-1', '1'], 'papua': 
['-1', '2', '-1', '-1', '4', '3', '-1', '-1'], 'sulawesi': ['-1', '4', '3', '4', '-1', '-1', '7', '-1'], 'mamuju': ['1', '-1', '-1', '3', '-1', '-1', '5', '-1'], 'ternate': ['-1', '-1', '-1', '-1', '7', '5', '-1', '6'], 'kalimantan': ['-1', '-1', '1', '-1', '-1', '-1', '6', '-1']}
    '''
    grafberbobot = []
    akhir = []
    for i in range(banyaksimpul):
        akhir += [(simpul[i], hasil[i])]
        #akhir += [(simpul[i], i)]
    
    #print("Akhir:", akhir)
    grafberbobot = dict(akhir)

def grafberbobotberpasangan():
    global g
    '''
    print(g)
    Output : [('jawa', 'sumatra', 2), ('jawa', 'mamuju', 1), ('sumatra', 'bali', 2), ('sumatra', 'papua', 2), ('sumatra', 'sulawesi', 4), ('bali', 'sulawesi', 3), ('bali', 'kalimantan', 1), ('papua', 'sulawesi', 4), ('papua', 'mamuju', 3), ('sulawesi', 'ternate', 7), ('mamuju', 'ternate', 5), ('ternate', 'kalimantan', 6)]
    '''
    g = []
    for i in range(banyaksimpul):
        for j in range(0+i, banyaksimpul):
            if (hasil[i][j] != '-1' and hasil[j][i] != '-1'):
                if (hasil[i][j] == hasil[j][i]):
                    g += [(simpul[i], simpul[j], int(hasil[i][j]))]
                else:
                    continue
            else:
                continue

#Algoritma Utama
namafile = input("Masukkan file graf : " )
readfile(namafile)

ceksimpul()
#print("simpul:", simpul)

isimatriks()
#print("hasil:", hasil)

grafindict()
print(grafberbobot)

grafberbobotberpasangan()
print("g:", g)

#simpulasal = input("Masukkan simpul asal : ")
#simpultujuan = input("Masukkan simpul tujuan : ")

