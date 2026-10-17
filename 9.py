matn = input("Matn kiriting: ").lower()
sozlar=matn.split()
chastota={}
for soz in sozlar:
    if soz in chastota:
         chastota[soz] += 1
    else:
          chastota[soz] = 1
for soz, soni in chastota.items():
    print(f"{soz} {soni}")
     