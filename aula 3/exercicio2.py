def transformKm():
    km = float(input("Informe o quilômetro: "))
    m = km * 1000
    cm = km * 100000
    print(km, "quilômetros são", m, "metros e", cm, "centimetros")

transformKm()