import collections
import charts
import read_ranking

def get_ranking_Uni(datos, pais):
    result = list(filter(lambda item: item['location'] == pais, datos))
    return result

def get_Cantidades(datos):
    pais = input('Que pais quieres saber su cantidad de estudiantes en las universidades =>')
    datos = list(filter(lambda item:item['location'] == pais, datos))
    universidades = [item['title'] for item in datos]
    cantidades = [float(item['students staff ratio']) for item in datos]
  
    return universidades, cantidades
    