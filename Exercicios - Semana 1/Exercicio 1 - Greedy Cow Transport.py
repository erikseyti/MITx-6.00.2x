#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:12:50 2020

@author: erik
"""

## Renomear Metodo para agir como uma função.



# cows ={'Maggie': 3, 'Herman': 7, 'Betsy': 9, 'Oreo': 6, 'Moo Moo': 3, 'Milkshake': 2, 'Millie': 5, #         'Lola': 2, 'Florence': 2, 'Henrietta': 9}
cows = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}

# peso total de cada uma das viagens
totalWeight = 10


def greedy_cow_transport(cows, limit):
    
    # indica se uma das vacas já foi selecionada para fazer o transporte
    dicionario_viagem = {}
    # indica a ordem de viagem entre as vacas, e a quantidade de viagens, pelo numero de listas dentro dela
    viagens = []
    # indica o nome das vacas que serão transportada em uma viagem.
    listaViagem = []
    
    while len(dicionario_viagem) < len(cows):
        copias_cow = {k: v for k, v in sorted(cows.items(), key=lambda item: item[1],reverse=True)}
        pesoViagem = limit
        listaViagem = []
        for key, value in copias_cow.items():
            if key not in dicionario_viagem and value <= pesoViagem:
                listaViagem.append(key)
                pesoViagem = pesoViagem - value
                dicionario_viagem[key] = value
        
        # print(listaViagem)
        viagens.append(listaViagem)
    return viagens

# greedy_cow_transport(cows,totalWeight)
    
print(greedy_cow_transport({'Lotus': 10, 'Muscles': 65, 'Clover': 5, 'Patches': 60, 'Milkshake': 75, 'Miss Bella': 15, 'Horns': 50, 'Louis': 45, 'MooMoo': 85, 'Polaris': 20}, 100))
print(greedy_cow_transport({'Betsy': 65, 'Willow': 35, 'Abby': 38, 'Buttercup': 72, 'Dottie': 85, 'Daisy': 50, 'Patches': 12, 'Rose': 50, 'Coco': 10, 'Lilly': 24}, 100))
print(greedy_cow_transport({'Betsy': 39, 'Luna': 41, 'Willow': 59, 'Abby': 28, 'Buttercup': 11, 'Starlight': 54, 'Rose': 42, 'Coco': 59}, 120))

    
        