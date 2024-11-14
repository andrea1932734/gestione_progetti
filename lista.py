lista = []

def riempi_lista(lista):
    prodotto = input("inserire prodotto:")
    lista.append(prodotto)

riempi_lista(lista)
riempi_lista(lista)
riempi_lista(lista)


def Stampa_lista(lista):
    print("lista della spesa")
    for i in range(len(lista)):
        print(f"{i + 1}. {lista[i]}")


def rimuovi_lista(lista):
    prodotto = input ("inserisci il prodotto da rimuovere dalla lista:")
    lista.pop(lista.index(prodotto))

rimuovi_lista(lista)
Stampa_lista(lista)


scelta = 1
while(scelta != 0):
    print("-------------------------")
    print("0. Uscita")
    print() 
    print("1. Operazione aggiungi")
    print("2. Operazione visualizza")
    print("3. operazione rimuovi")
    print("...")
    print("...")
    print()
    scelta=int(input("Scegli: "))
    print("------------------------")
 
    if(scelta == 0):
        pass
    elif(scelta == 1):
        print("Operazione --aggiungi--")
        riempi_lista(lista)
        ...
    elif(scelta == 2):
        print("Operazione --visualizza--")
        Stampa_lista(lista)
        ...
    elif(scelta == 3):
        print("Operazione --rimuovi--") 
        rimuovi_lista(lista)
        ...
    ...
    ...
else:
        print("Non capisco...")
        ...
 
print("Soddisfatto o rimborsato!")