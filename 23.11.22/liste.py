osoba = ["sofija",25,"plava", True]

for x in range(len(osoba)):
    print(osoba,[x])

for osobina in osoba:
    print(osobina)




voce_i_povrce = ["jabuka","beli luk","crni luk","banana","mandarina","lubenica","krastavac"]

for stavka in voce_i_povrce:
    print(stavka)

for i in range(len(voce_i_povrce)):
    print("na indexu:",i,"nalazi se:",voce_i_povrce[i])


for index,vrednost in enumerate(voce_i_povrce):
    print("indeks:",index,"stavka:",vrednost)

automobili = ["citroen","bmw","opel","kia","jugo"]

for pozicija,auto in enumerate(automobili):
    print("pozicija:",pozicija,"auto",auto)
    
    
automobili.append("mercedes")
automobili[2] = "opel corsa"
print(automobili)

del automobili[3]
print(automobili)
automobili.remove("bmw")
print(automobili)
automobili.pop(0)
print(automobili)


automobili = ["citroen","bmw","opel","kia","jugo","peugeot","audi"]

automobili_akcija = []

for i in range(len(automobili)):
    if i == 1 or i == 2 or i == 3:
        automobili_akcija.append(automobili[i])

print(automobili_akcija)

automobili_akcija = automobili[1:4]
print(automobili_akcija)

brojevi =[5,10,15,20,25,30]
parni= []
neparni =[]

for broj in brojevi:
    if broj % 2 == 0:
        parni.append(broj)
    else:
        neparni.append(broj)

print(parni,neparni)
    
        
        