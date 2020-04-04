#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:12:50 2020

@author: erik
"""


cows ={'Maggie': 3, 'Herman': 7, 'Betsy': 9, 'Oreo': 6, 'Moo Moo': 3, 'Milkshake': 2, 'Millie': 5, 
        'Lola': 2, 'Florence': 2, 'Henrietta': 9}
# cows = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}

# peso total de cada uma das viagens
totalWeight = 10


# indica o numero de vacas dentro do dicionario
numeroVacas = len(cows)

# indica se uma das vacas já foi selecionada para fazer o transporte
dicionario_viagem = {}
# indica a ordem de viagem entre as vacas, e a quantidade de viagens, pelo numero de listas dentro dela
viagens = []
# indica o nome das vacas que serão transportada em uma viagem.
listaViagem = []

while len(dicionario_viagem) < len(cows):
    copias_cow = {k: v for k, v in sorted(cows.items(), key=lambda item: item[1],reverse=True)}
    pesoViagem = totalWeight
    listaViagem = []
    for key, value in copias_cow.items():
        if key not in dicionario_viagem and value <= pesoViagem:
            listaViagem.append(key)
            pesoViagem = pesoViagem - value
            dicionario_viagem[key] = value
    
    
    viagens.append(listaViagem)
print(viagens)

        
    
        