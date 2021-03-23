#Delta  a estrella

def Delta_estrella(ra,rb,rc):
    suma = ra + rb + rc
    resistencia_a = rb * rc / suma
    print(f"resistencia 1 {resistencia_a}")

    resistencia_b = ra * rc / suma
    print(f"resistencia 2 {resistencia_b}")

    resistencia_c = ra * rb / suma
    print(f"resistencia  3 {resistencia_c}")


def Estrella_Delta(r1, r2, r3):
    suma = (r1 * r2) + (r1*r3) + (r2 * r3)
    print(f"la suma es {suma}")

    re_a = suma / r1
    print(f"Reistencia a {re_a}")

    re_b = suma / r2
    print(f"Reistencia b {re_b}")

    re_c = suma /r3    
    print(f"Reistencia a {re_c}")

Estrella_Delta(10,15,30)
