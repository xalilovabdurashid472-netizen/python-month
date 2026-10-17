with open("matn.txt","r")as f:
    matn=f.read()
    sozlar=matn.split()
    print("Sozlar soni: ",len(sozlar))
