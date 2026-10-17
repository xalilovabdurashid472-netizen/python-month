sonlar = list(map(int, input("Sonlarni kiriting: ").split()))
son=set(sonlar)
natija=sorted(son)
print(sonlar)
if len(natija)>2:
        print("Ikkinchi eng katta son:", natija[-2])
else:
            print("Ikkinchi eng katta son mavjud emas")
