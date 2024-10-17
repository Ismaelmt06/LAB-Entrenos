from entrenos import *

def test_lee_entrenos():
    print("Prueba de lee_entreno")
    entrenos = lee_entrenos("data\entrenos.csv")
    print(entrenos[:3])
    print(entrenos[-3:])

if __name__ == "__main__":
    # entrenos = entrenos.lee_entrenos()
    test_lee_entrenos()