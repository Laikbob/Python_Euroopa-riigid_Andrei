from random import *

def failist_to_dict(f: str):
    riik_pealinn = {}  
    pealinn_riik = {}  
    riigid = []  

    with open(f, 'r', encoding="utf-8-sig") as file:
        for line in file:
            k, v = line.strip().split('-') 
            riik_pealinn[k] = v  
            pealinn_riik[v] = k  
            riigid.append(k)  

    return riik_pealinn, pealinn_riik, riigid

riik_pealinn, pealinn_riik, riigid = failist_to_dict("riigid_pealinnad.txt")

print(riigid)
print(list(riik_pealinn.keys())) 


pealinnad = list(riik_pealinn.values())


while True:
    riik = input("Riik: ")
    if riik == "A": 
        break
    print("Pealinn:", riik_pealinn.get(riik, "Riiki ei leitud")) 


for key, value in riik_pealinn.items():
    print(key + "-" + value)  

def otsi_pealinn(riik_pealinn: dict, riik: str):
    return riik_pealinn.get(riik, "Страна не найдена.")

def otsi_riik(pealinn_riik: dict, pealinn: str):
    return pealinn_riik.get(pealinn, "Столица не найдена.")

def lisa_paru(riik_pealinn: dict, pealinn_riik: dict, riik: str, pealinn: str):
    riik_pealinn[riik] = pealinn
    pealinn_riik[pealinn] = riik
    print(f"Добавлено: {riik} - {pealinn}")