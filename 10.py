ballar = {
    "Ali": 85,
    "Vali": 92,
    "Sardor": 78,
    "Malika": 95
}
eng_yuqori=max(ballar,key=ballar.get)
ball=ballar[eng_yuqori]
ortacha=sum(ballar.values())/len(ballar)
print(f"Eng yuqori ball {eng_yuqori} - {ball}")
print("Ortacha ball: ",ortacha)