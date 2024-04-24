#ver1

# tantargyFelosztas=[]
# with open ("./beosztas.txt","r",encoding="UTF-8" ) as fin:
#     for sor in fin:
#         tantargyFelosztas.append(sor.strip())
        
#for elem in tantargyFelosztas:
#    print(f"{elem},")
    
#print(f"A listában {int(len(tantargyFelosztas)/4)} elem van")


#ver2

tanarok=[]
tantargyak=[]
osztalyok=[]
oraszamok=[]

rekord=[]

with open ("./beosztas.txt","r",encoding="UTF-8" ) as fin:
    for sor in fin:
        rekord.append(sor.strip())
        if len (rekord)==4:
            tanarok.append(rekord[0])
            tantargyak.append(rekord[1])
            osztalyok.append(rekord[2])
            oraszamok.append(int(rekord[3]))
            rekord=[]
            
# for i in range(len(tanarok)):
#     print(f"{tanarok[i]}, {tantargyak[i]}, {osztalyok[i]}, {oraszamok[i]}")
print("2.Feladat")    
print(f"A bejegyzések száma: {len(tanarok)}")

print("3.Feladat")
print(f"Az iskolában a heti összóraszám: {sum(oraszamok)}")

def osszegzes(be_tanar, tanarok, oraszamok):
    osszOraszam=0
    for i in range(len(tanarok)):
        if tanarok[i]==be_tanar:
            osszOraszam+=oraszamok[i]
    return osszOraszam

print("4.Feladat")
be_tanar=input("Egy tanár neve=") or "Albatrosz Aladin"
print(f"A tanárok heti órazsáma: {osszegzes(be_tanar, tanarok, oraszamok)}")


def eldontes(beOsztaly, beTantargy,tantargyak, osztalyok):
    i=0
    while (i<len(tantargyak) and not (beTantargy==tantargyak[i] and beOsztaly.split(".")[0]==osztalyok[i].split(".")[0] and "x"in osztalyok[i])):
        i+=1
    return i<len(tantargyak)
        

print("6.Feladat")
beOsztaly=input("Osztály: ") or "10.b"
beTantargy=input("Tantárgy: ") or "kemia"
if eldontes(beOsztaly, beTantargy, tantargyak, osztalyok):
    print("Csoportbontásban tanulják.")
    
else:
    print("Nem csoportbontásban tanulják.")
    
print("7.Feladat")

def megszamol(tanarok):
    tanarokEgyedi=[]
    for tanar in tanarok:
        if tanar not in tanarokEgyedi:
            tanarokEgyedi.append(tanar)
    return len(tanarokEgyedi)
print(f"Az iskolában {megszamol(tanarok)} tanár tanít.")
