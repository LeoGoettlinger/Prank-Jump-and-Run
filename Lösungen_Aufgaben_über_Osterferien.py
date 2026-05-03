""""
i = 0
line = 0

while line <= 9:
    i = 0
    output = ""

    while i  <= line:
        output += str(i) + " "
        i += 1

    print(output.strip())
    line += 1
"""
#####################################################################################################################################
"""
i = 0
line = 0

for i in range(10):
    print("  " * line, end = "")
    for j in range(10 - line):
        print(j, end = " ")
    print()
    line += 1
"""
#####################################################################################################################################
"""
i = 0
for i in range(10):
    for j in range(10 - i):
        print(j, end=" ")
    print()
"""
#####################################################################################################################################
"""
i = 0
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i * j:2}", end=" ")
    print()
"""
#####################################################################################################################################
"""
i = 0

for i in range(1, 10):  
    for j in range(1, i + 1): 
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()  
"""
#####################################################################################################################################

i = 0
height = 9  # Höhe der Pyramide

for i in range(1, height + 1):  # Äußere Schleife für die Zeilen
    print("  " * (height - i), end="")  # Leerzeichen für die zentrierte Einrückung
    for j in range(1, i + 1):  # Aufsteigende Zahlen
        print(j, end=" ")
    for j in range(i - 1, 0, -1):  # Absteigende Zahlen
        print(j, end=" ")
    print()  # Neue Zeile nach jeder Iteration


