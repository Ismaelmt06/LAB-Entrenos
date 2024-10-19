from entrenos import *

def test_lee_entrenos():
    print("Prueba de lee_entreno")
    entrenos = lee_entrenos("data\entrenos.csv")
    print(entrenos[:3])
    print(entrenos[-3:])

def test_tipos_entrenos(entrenos):
    print("Prueba de tipos de entreno")
    print(tipos_entrenos(entrenos))

def test_entrenos_duracion_superior(entrenos):
    print("Prueba de entrenos duración superior")
    print(entrenos_duracion_superior(entrenos, 75))

def test_suma_calorias(entrenos, f_inicio, f_fin):
    print("Prueba de suma de calorías")
    print(suma_calorias(entrenos, f_inicio, f_fin))
if __name__ == "__main__":
    entrenos = lee_entrenos("data\entrenos.csv")
    # test_lee_entrenos()
    # test_tipos_entrenos(entrenos)
    test_entrenos_duracion_superior(entrenos)