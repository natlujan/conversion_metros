metros = float(input("Metros a convertir: "))

print("Pulgadas 'p'\n")
print("Pies = 'f'\n")
print("Yardas 'y'\n")
conversion = input("Conversión:\n")

conversion.lower()

if conversion == 'p':
    pulgadas = metros * 39.37
    print("La conversión es:", pulgadas)

elif conversion == 'f':
    pies = metros * 3.2808
    print("La conversión es:", pies)

elif conversion == 'y':
    yardas = metros * 1.0936
    print("La conversión es:", yardas)
