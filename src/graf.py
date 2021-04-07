import math
from math import radians, cos, sin, asin, sqrt

def readfile(namafilegraf):
    global graf, grafsimpul, banyaksimpul, bobot
    file = open("./test/"+ namafilegraf + ".txt", "r")
    banyaksimpul = int(file.readline())
    #print("Banyak Simpul : ", banyaksimpul)
    grafsimpul = file.readline()
    graf = file.readlines()
    #print("grafsimpul:", grafsimpul)
    #print("graf:", graf)

def readposisi(namafileposisi):
    global posisi, hasilposisi
    file = open("./test/" + namafileposisi + ".txt", "r")
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
    #print("posisi:", posisi)
    #print("hasilposisi:", hasilposisi)

def ceksimpul():
    global simpul
    simpul = []
    huruf = ''
    isiSimpul = ''
    simpul = grafsimpul.split(',')
    lastnode = simpul[-1][:-1]
    simpul = simpul[:-1]
    simpul.append(lastnode)
    #print("simpul:", simpul)
    #splitsimpul()

def splitsimpul():
    newsimpul = [char for char in simpul[0]]
    simpul.clear()
    simpul.extend(newsimpul)

def isimatriks():
    global hasil
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
    global g
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
    global heuristic, posisitujuan
    heuristic = [] #heuristic hitung ke node goal
    akhir = []

    posisitujuan = 0
    for i in range(banyaksimpul):
        if (simpultujuan == simpul[i]):
            posisitujuan = i
            break

    for i in range(banyaksimpul):
        dist = haversine(int(hasilposisi[i][0]), int(hasilposisi[i][1]), int(hasilposisi[posisitujuan][0]), int(hasilposisi[posisitujuan][1]))
        akhir += [(simpul[i], dist)]
        
    heuristic = dict(akhir) 

class Graph:
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()
    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.graph_dict.setdefault(b, {})[a] = dist
    def connect(self, A, B, distance=1):
        self.graph_dict.setdefault(A, {})[B] = distance
        if not self.directed:
            self.graph_dict.setdefault(B, {})[A] = distance
    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)
    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)

class Node:
    def __init__(self, name:str, parent:str):
        self.name = name
        self.parent = parent
        self.g = 0 # jarak ke node start
        self.h = 0 # jarak heuristic ke node tujuan
        self.f = 0 # Total jarak
    # Compare nodes
    def __eq__(self, other):
        return self.name == other.name
    # Sort nodes
    def __lt__(self, other):
         return self.f < other.f
    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.name, self.f))

def add_to_open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f > node.f):
            return False
    return True

def astar_search(graph, heuristics, start, end):
    open = []
    closed = []
    start_node = Node(simpulasal, None)
    goal_node = Node(simpultujuan, None)
    open.append(start_node)
    #print("start:", start_node)
    
    while len(open) > 0:
        # Sort secara bobot ascending
        open.sort()
        current_node = open.pop(0)
        closed.append(current_node)
        #print("current node:", current_node)
        
        if current_node == goal_node:
            pathweighted = []
            while current_node != start_node:
                pathweighted.append(current_node.name + ': ' + str(current_node.g))
                current_node = current_node.parent
            pathweighted.append(start_node.name + ': ' + str(start_node.g))
            # Return path
            return pathweighted[::-1]
        neighbors = graf.get(current_node.name)
        #print("neighbors :", neighbors)
        for key, value in neighbors.items():
            neighbor = Node(key, current_node)
            if(neighbor in closed):
                continue
            # hitung total bobot
            neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
            neighbor.h = heuristics.get(neighbor.name)
            neighbor.f = neighbor.g + neighbor.h
            if(add_to_open(open, neighbor) == True):
                open.append(neighbor)
    return None

#Algoritma Utama
namafilegraf = input("Masukkan file graf : " )
readfile(namafilegraf)

namafileposisi = input("Masukkan file posisi : " )

ceksimpul()
#print("simpul:", simpul)

isimatriks()
#print("hasil:",hasil)

grafindict()
#print("grafberbobot:", grafberbobot)

grafberbobotberpasangan()
#print("g:",g)

readposisi(namafileposisi)
#print("hasilposisi:", hasilposisi)

simpulasal = input("Masukkan simpul asal : ")
simpultujuan = input("Masukkan simpul tujuan : ")
jarak(simpultujuan)
#print("heuristic:", heuristic)

graf = Graph()
for edge in g :
    graf.connect(edge[0], edge[1], edge[2])

pathweighted = astar_search(graf, heuristic, simpulasal, simpultujuan)
print("solusi:", pathweighted)
print()

path = []
for solution in pathweighted:
    currpath = solution.partition(":")
    #print(currpath)
    path.append(currpath[0])
print(path)