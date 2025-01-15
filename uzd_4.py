def prasi_preci():
#Prasa lietotājam ievadīt preces nosaukumu un cenu
    while True:
        nosaukums = input("Prece (vai 'exit'): ")
        if nosaukums.lower() == 'exit':
            break
        try:
            cena = float(input(f"Cena {nosaukums}: "))
            if cena < 0:
                print("Cena nevar būt negatīva.")
            else:
                return {"nosaukums": nosaukums, "cena": cena}
        except ValueError:
            print("Nepareiza cena. Ievadi skaitli.")

def veido_sarakstu():
#Veido iepirkumu sarakstu
    saraksts = []
    while True:
        prece = prasi_preci()
        if prece is None:
            break
        saraksts.append(prece)
    return saraksts

def radi_sarakstu(saraksts):
#Parāda iepirkumu sarakstu un kopējo summu
    if not saraksts:
        print("Saraksts ir tukšs.")
        return

    print("Iepirkumu saraksts:")
    summa = 0
    for prece in saraksts:
        print(f"- {prece['nosaukums']}: {prece['cena']:.2f} EUR")
        summa += prece['cena']
    print(f"----------------------")
    print(f"Kopā: {summa:.2f} EUR")

# Programmas galvenā daļa
mans_saraksts = veido_sarakstu()
radi_sarakstu(mans_saraksts)