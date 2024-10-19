from collections import namedtuple
import csv
from datetime import datetime
Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')
def lee_entrenos(ruta_csv):
    entrenos = []
    with open(ruta_csv, encoding= 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for tipo, fechahora, ubicacion, duracion, \
            calorias, distancia, frecuencia, compartido in lector:
            fechahora = datetime.strptime(fechahora, "%d/%m/%Y %H:%M")
            duracion = int(duracion)
            calorias = int(calorias)
            distancia = float(distancia)
            frecuencia = int(frecuencia)
            compartido = compartido == 'S'
            tupla = Entreno[tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido]
            entrenos.append(tupla)
        return entrenos

def tipos_entrenos(entrenos):
    tipos = set()
    for e in entrenos:
        tipos.add(e)
    return sorted(list(tipos))
def entrenos_duracion_superior(entrenos, d):
    filtro = []
    for e in entrenos:
        if e.duracion >= d:
            filtro.append(e)
    return filtro

def suma_calorias(entrenos, f_inicio, f_fin):
    suma = 0
    for e in entrenos:
        if (f_inicio <= e.fechaHora <= f_fin):
            suma += e.calorias
    return suma