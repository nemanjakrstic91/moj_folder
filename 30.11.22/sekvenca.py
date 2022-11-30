

#brojevi.sort()
# brojevi.sort()
# brojevi.reverse()

# print(brojevi)


brojevi = [9,1,3,2,5,8,7]

sortirani_brojevi = [1,2,3,5,7,8,9]

while True:
    izvrsena_zamena = False
    for i in range(1,len(brojevi)):
    
        
        if brojevi[i] < brojevi [i-1]:
            privremena = brojevi[i]
            brojevi[i] = brojevi[i-1]
            brojevi[i-1] = privremena
            izvrsena_zamena = True
    if izvrsena_zamena == False:
        break


print(brojevi)


proizvodi = ["telefon","tv","laptop"]
cena= [ 100,  200,  300]

for i in range(len(proizvodi)):
    print(proizvodi[i],cena[i])




automobili = ["audi","bmw","yugo","citroen","kia","peugeot"]

for i in range(len(automobili)):
    if i == 3:
        print(automobili[i])




proizvodi = [
                ["iphone 6","samsung s 22","xiaomi 11"], 
                ["acer","dell","mecbook"],
                ["ipad","samsung galaxy tab","xiaomy tablet"],
            ]   

telefoni = ["iphone 6","samsung s 22","xiaomi 11"]
laptopovi = ["acer","dell","mecbook"]
tableti = ["ipad","samsung galaxy tab","xiaomy tablet"]


for i in range (len(proizvodi)):
    print(proizvodi[i])
    for j in range(len(proizvodi[i])):
        print(proizvodi[i][j])


hrana = [
            ["cokolada","bombone","palacinke"],
            ["sarma","musaka","kiseli kupus"],
            ["pecena paprika","ajvar","sopska"],
        ]


for kategorija in hrana:
    
    for jelo in kategorija:
        print("naziv:",jelo)


biblioteka = [

]

while True:
    print("Odaberi komandu: 1-unos, 2-prikaz, 3-brisanje, > 3 izlaz")
    komanda = int(input("Unesite komandu: "))

    if komanda == 1:
        # unos knjige, preuzmi podatke
        naslov = input("Unesite naslov: ")
        autor = input("Unesite autora: ")
        isbn = int(input("Unesite isbn: "))
        biblioteka.append([naslov, autor, isbn])
        print("Dodata knjiga")
    if komanda == 2:
        for knjiga in biblioteka:
            for detalj in knjiga:
                print(detalj)
    if komanda == 3:
        #ovde vrsim brisanje
        kljucna_rec = input("Unesite naziv knjige koju zelite da obrisem. ")
        for knjiga in biblioteka:
            #proveravam detalje KNJIGE
            for detalj in knjiga:
                if detalj == kljucna_rec:
                    biblioteka.remove(knjiga)
                    print("Knjiga je obrisana")
    




    

    









