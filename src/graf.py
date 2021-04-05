def readfile(namafile):
    global graf, grafsimpul, banyaksimpul, bobot;
    file = open("../test/"+ namafile + ".txt", "r")
    banyaksimpul = int(file.readline());
    #print("Banyak Simpul : ", banyaksimpul)
    grafsimpul = file.readline()
    graf = file.readlines()
    #print(graf);
    #print(bobot)

#Algoritma Utama
namafile = input("Masukkan file graf : " );
readfile(namafile)

simpul = []
for i in range(banyaksimpul):
    simpul += [grafsimpul[i]]

bobotpersimpul = []
b = ''
isi = []
hasil = []
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
            
#print(hasil)

grafberbobot = []
akhir = []
for i in range(banyaksimpul):
    #akhir += [(simpul[i], hasil[i])]
    akhir += [(simpul[i], i)]
    
grafberbobot = dict(akhir)
print(grafberbobot)
print(hasil)





