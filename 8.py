sonlar = list(map(int, input("Sonlarni kiriting: ").split()))
musbat = []
manfiy = []
nollar = []
for son in sonlar:
    if son>0:
        musbat.append(son)
    elif son<0:
        manfiy.append(son)
    else:
        nollar.append(son)
print("Musbat sonlar:", musbat)
print("Manfiy sonlar:", manfiy)
print("Nollar soni:", len(nollar))