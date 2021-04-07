import math
from math import radians, cos, sin, asin, sqrt

def readfile(namafile):
    global graf, grafsimpul, banyaksimpul, bobot;
    #file = open("./test/"+ namafile + ".txt", "r")
    file = open("./test/inputGraf.txt", "r")
    banyaksimpul = int(file.readline());
    #print("Banyak Simpul : ", banyaksimpul)
    grafsimpul = file.readline()
    graf = file.readlines()
    #print(grafsimpul);
    #print(graf)

def read():
    global posisi, hasilposisi;
    '''
    print(hasilposisi)
    output : [['5', '3'], ['14', '7'], ['10', '3'], ['5', '12'], ['0', '3'], ['1', '9'], ['7', '1'], ['17', '10']]
    '''
    file = open("./test/inputPosisi.txt", "r")
    posisi = file.readlines()

    b = ''
    isi = []
    hasilposisi = []
    posisipersimpul = []
    for i in range(banyaksimpul):
        for j in range(len(posisi[i])):
            if (posisi[i][j] == ','):
                posisipersimpul += isi
                b = ''
                #print("posisipersimpul : ", posisipersimpul)
            elif (posisi[i][j] == '\n'):
                hasilposisi += [posisipersimpul]
                posisipersimpul = []
            elif (posisi[i][j] != ','):
                b += posisi[i][j]
                isi = [b]
                #print("ISI : ", isi)

def ceksimpul():
    global simpul;
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

def isimatriks():
    global hasil;
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
        
    grafberbobot = dict(akhir)

def grafberbobotberpasangan():
    global g;
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
                    continue;
            else:
                continue;

def haversine(lat1, lon1, lattujuan, lontujuan):
    R = 6372.8 * 1000
    dLat = radians(lattujuan - lat1)
    dLon = radians(lontujuan - lon1)
    lat1 = radians(lat1)
    lattujuan = radians(lattujuan)

    a = sin(dLat/2)**2 + cos(lat1)*cos(lattujuan)*sin(dLon/2)**2
    c = 2*asin(sqrt(a))

    return R * c

def jarak(simpultujuan):
    global heuristic, posisitujuan;
    '''
    print(heuristic)
    output : {'jawa': 556131.7128554732, 'sumatra': 622281.6451387275, 'bali': 0.0, 'papua': 1137362.163370625, 'sulawesi': 1112263.4257109463, 'mamuju': 1201005.3323019776, 'ternate': 399667.1726683548, 'kalimantan': 1085576.3721392686}
    '''
    heuristic = [] #heuristic hitung ke node goal
    akhir = []

    posisitujuan = 0
    for i in range(banyaksimpul):
        if (simpultujuan == simpul[i]):
            print("true")
            posisitujuan = i
            break;

    for i in range(banyaksimpul):
        dist = haversine(int(hasilposisi[i][0]), int(hasilposisi[i][1]), int(hasilposisi[posisitujuan][0]), int(hasilposisi[posisitujuan][1]))
        akhir += [(simpul[i], dist)]
        
    heuristic = dict(akhir) 


#Algoritma Utama
#namafile = input("Masukkan file graf : " )
namafile = 0
readfile(namafile)

ceksimpul()
#print(simpul)

isimatriks()
#print(hasil)

grafindict()
#print(grafberbobot)

grafberbobotberpasangan()
#print(g)

read()
#print(hasilposisi)

#hasilposisi1 = [[5, 3], [14, 7], [10, 3], [5, 12], [0, 3], [1, 9], [7, 1], [17, 10]]
#print(hasilposisi1[0][0], hasilposisi1[0][1])

simpulasal = input("Masukkan simpul asal : ")
simpultujuan = input("Masukkan simpul tujuan : ")
jarak(simpultujuan)
#print("Ini heuristic : \n", heuristic)
