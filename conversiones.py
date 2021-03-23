
#Delta  a estrella
def delta_To_estrella(ra,rb,rc):
    suma = ra + rb + rc
    print(f"la suma es {suma}")
    resistencia_a = rb * rc / suma
    print(f"resistencia 1 {resistencia_a}")

    resistencia_b = ra * rc / suma
    print(f"resistencia 2 {resistencia_b}")

    resistencia_c = ra * rb / suma
    print(f"resistencia  3 {resistencia_c}")


#Estrella a Delta
def estrella_To_Delta(r1, r2, r3):
    suma = (r1 * r2) + (r1*r3) + (r2 * r3)
    print(f"la suma es {suma}")

    re_a = suma / r1
    print(f"Reistencia a {re_a}")

    re_b = suma / r2
    print(f"Reistencia b {re_b}")

    re_c = suma /r3    
    print(f"Reistencia a {re_c}")


def resistencia_paralelo(r1,r2,r3):
    suma_r1 = 1/r1 + 1/r1
    rt1 = 1/ suma_r1

    suma_r2 = 1/r2 + 1/60
    rt2 = 1/suma_r2

    suma_r3 = 1/r3 + 1/90
    rt3 = 1/ suma_r3

    print(f"Las resistencias son R1 {rt1}  R2 {rt2} R3 {rt3}")

def paralelo(resistencia: list):
    suma = 0
    for i in resistencia:
        suma += 1/i
    resultado = 1/suma
    print(resultado)

delta_To_estrella(90,30,15)
resistencia_paralelo(30,30,30)
