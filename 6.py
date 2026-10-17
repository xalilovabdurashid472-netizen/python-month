sonlar = list(map(int, input("Sonlarni kiriting: ").split()))
natija=[]
for son in sonlar:
    if son not in natija:
        natija.append(son)
print(*natija)