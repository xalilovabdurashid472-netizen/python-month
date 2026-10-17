
import json

talaba = {
    "ism": "Ali",
    "yosh": 18,
    "ball": 90
}

with open("talaba.json", "w", encoding="utf-8") as file:
    json.dump(talaba, file, ensure_ascii=False, indent=4)

with open("talaba.json", "r", encoding="utf-8") as file:
    malumot = json.load(file)

print("Ism:", malumot["ism"])
print("Yosh:", malumot["yosh"])
print("Ball:", malumot["ball"])
