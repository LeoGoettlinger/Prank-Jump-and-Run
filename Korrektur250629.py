# Aufgabe 1
def produkt_von_bis(von:  int, bis: int) -> int:
    if von > bis:
        return 0
    produkt = 1
    for i in range(von, bis + 1):
        produkt *= i
    return produkt

# Aufgabe 2
von: 0
bis: 3