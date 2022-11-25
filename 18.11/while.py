sekunde= 10

import random

# while sekunde > 0:
#     print(sekunde)
#     sekunde-= 1


baterija= 90

while baterija> 0:
    print("mozes koristiti telefon",baterija)
    baterija -= random.randint(5,20)


print("baterija je prazna")


for broj in range(11):
    if broj == 2:
        continue
    print(broj)
    

