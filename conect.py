import networkx as NX
def compute_shortest_path_fast(a,b,N,A,largo):
    G = NX.DiGraph()
    G.add_nodes_from(N)
    for (i,j) in A:
        G.add_edge(i,j, weight = largo[(i,j)])
    print("Conectados los nodos "+str(a)+"\t"+str(b))
    yay=NX.shortest_path_length(G,a,b, weight="weight")
    print(yay)
    return yay

import csv

#### For Secure Points #####

idsecure = []
V = []
D = []
C = []

for d in csv.DictReader(open('secure_points.csv'), delimiter=','):
    idsecure.append(int(d['id']))
    V.append(int(d['V']))
    D.append(int(d['D']))
    C.append(int(d['C']))

#print("id_secure= ", idsecure)
#print("V = ", V)
#print("D =", D)
#print("C =", C)

#### For Demographics ####

iddemo = []
lon = []
lat = []
demanda = []

for b in csv.DictReader(open("demographic.csv", "r"), delimiter=","):
    iddemo.append(int(b['id']))
    lon.append(float(b["lon"]))
    lat.append(float(b['lat']))
    demanda.append(int(b['demanda']))
    
#print("id_demo= ", iddemo)
#print("lon = ", lon)
#print("lat =", lat)
#print("demanda =", demanda)
    

#### For A ####

head = []
tail = []

for c in csv.DictReader(open("arcos_def.csv", "r"), delimiter=","):
    head.append(int(c["head"]))
    tail.append(int(c["tail"]))
    
#print("head =", head)
#print("tail", tail)
  
#### Create arc tuples #####

A=[]
for i in range(len(head)):
    A.append(tuple((head[i], tail[i])))

#for j in range(len(A)):
#    print(A[j])

#### Calculate Distances #####

distances=[]
for l in range(len(A)):
    distances.append(abs(A[l][0]-A[l][1]))
#    print(distances[l])
    

####### Create Distance Dictionary ########

largotuples=[]
for k in range(len(A)):
    largotuples.append(tuple((A[k], distances[k])))
#    print(largotuples[k])
    
largo=dict(largotuples)
#print(largo)

#### Create node list ####

N=[]
for i in range(len(head)):
    if head[i] not in N:
        N.append(head[i])
#print(N)
    

for a in range(1,10):
    for b in range(1,10):
        if a != b:
            compute_shortest_path_fast(a,b,N,A,largo)
        
    