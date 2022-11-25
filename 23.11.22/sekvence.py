osoba = ["sofija", 20, "plava", True]
print(osoba)

print(osoba[0])
print('godine',osoba[1])


automobili = ["opel","citroen","mercedes"]
print(automobili[2])

for x in range(5,10):
    print(x)

kurs = "python"
print(kurs[0])
print(kurs[1])
print(kurs[2])
print(kurs[3])

duzina = len(kurs)

for x in range(len(kurs)):
    print("na poziciji", x ,kurs,[x])


ustanova = "it academy"

for indeks in range(len(ustanova)):
    print(ustanova[indeks])

print()

primer = "zadatak1"
for index in range(len(primer)):
    print(primer[index])


broj_karaktera = len(primer)
index = 0

while indeks<broj_karaktera:
    print(primer[index])
    index+=1

korisnicko_ime = "admin"
uneto_kor_ime = input("unesi korisnicko ime:")

if korisnicko_ime == uneto_kor_ime.lower():
    print("dobro dosli")
else:
    print('pogresni podaci')




