#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 09:44:43 2020

@author: andre
"""

######################################################################
#   Módulo que contém funções para construir dicionarios auxiliares  # 
#   que serão utilizados para recortar o dataframe que contem todos  #
#   os dados brutos juntos. As chaves são strings que se referem a   #
#   anos, meses ou estaçoes. Cada chave se refere a uma lista de     #
#   strings, onde cada string esta no formato dd/mm/aaaa.            #    
######################################################################

import numpy as np

## Anos em que há arquivos nc:
years = ['2014', '2015']

## Dicionários para guardar listas com as datas de cada ano:
ano14 = {str(years[0]):[]}
ano15 = {str(years[1]):[]}

## Dicionários para guardar listas com as datas de cada mês:
meses14 = {'jan':[], 'fev':[], 'mar':[], 'abr':[], 'mai':[], 'jun':[],
           'jul':[], 'ago':[], 'set':[], 'out':[], 'nov':[], 'dez':[]}
meses15 = {'jan':[], 'fev':[], 'mar':[], 'abr':[], 'mai':[], 'jun':[], 
           'jul':[], 'ago':[], 'set':[], 'out':[], 'nov':[], 'dez':[]}

## Dicionários para guardar listas com as datas de cada estação:
estacoes14 = {'wet':[], 't1a':[], 't1b':[], 'dry':[], 'tr2':[]}
estacoes15 = {'wet':[], 't1a':[], 't1b':[], 'dry':[], 'tr2':[]}

## Função que cria um dicionario de uma só lista, onde os valores são as 
## strings com as datas de 2014:   
def organiza_ano14(dia, mes, ano):
    if ano == '2014':
        ano14['2014'].append(dia+'/'+mes+'/'+ano)
    return ano14

## Função que cria um dicionario de uma só lista, onde os valores são as 
## strings com as datas de 2014:   
def organiza_ano15(dia, mes, ano):
    if ano == '2015':
        ano15['2015'].append(dia+'/'+mes+'/'+ano)
    return ano15
    
## Função que cria um dicionario de listas, onde cada lista é um mês 
## de 2014 e os valores são as strings com as datas de cada mês:       
def organiza_meses14(dia, mes, ano):        
    if mes == '1' and ano == '2014':
        meses14['jan'].append(dia+'/'+mes+'/'+ano)
    if mes == '2' and ano == '2014':
        meses14['fev'].append(dia+'/'+mes+'/'+ano)
    if mes == '3' and ano == '2014':
        meses14['mar'].append(dia+'/'+mes+'/'+ano)
    if mes == '4' and ano == '2014':
        meses14['abr'].append(dia+'/'+mes+'/'+ano)
    if mes == '5' and ano == '2014':
        meses14['mai'].append(dia+'/'+mes+'/'+ano)
    if mes == '6' and ano == '2014':
        meses14['jun'].append(dia+'/'+mes+'/'+ano)
    if mes == '7' and ano == '2014':
        meses14['jul'].append(dia+'/'+mes+'/'+ano)
    if mes == '8' and ano == '2014':
        meses14['ago'].append(dia+'/'+mes+'/'+ano)
    if mes == '9' and ano == '2014':
        meses14['set'].append(dia+'/'+mes+'/'+ano)
    if mes == '10' and ano == '2014':
        meses14['out'].append(dia+'/'+mes+'/'+ano)
    if mes == '11' and ano == '2014':
        meses14['nov'].append(dia+'/'+mes+'/'+ano)
    if mes == '12' and ano == '2014':
        meses14['dez'].append(dia+'/'+mes+'/'+ano)
    return meses14

## Função que cria um dicionario de listas, onde cada lista é um mês 
## de 2015 e os valores são as strings com as datas de cada mês:
def organiza_meses15(dia, mes, ano):
    if mes == '1' and ano == '2015':
        meses15['jan'].append(dia+'/'+mes+'/'+ano)
    if mes == '2' and ano == '2015':
        meses15['fev'].append(dia+'/'+mes+'/'+ano)
    if mes == '3' and ano == '2015':
        meses15['mar'].append(dia+'/'+mes+'/'+ano)
    if mes == '4' and ano == '2015':
        meses15['abr'].append(dia+'/'+mes+'/'+ano)
    if mes == '5' and ano == '2015':
        meses15['mai'].append(dia+'/'+mes+'/'+ano)
    if mes == '6' and ano == '2015':
        meses15['jun'].append(dia+'/'+mes+'/'+ano)
    if mes == '7' and ano == '2015':
        meses15['jul'].append(dia+'/'+mes+'/'+ano)
    if mes == '8' and ano == '2015':
        meses15['ago'].append(dia+'/'+mes+'/'+ano)
    if mes == '9' and ano == '2015':
        meses15['set'].append(dia+'/'+mes+'/'+ano)
    if mes == '10' and ano == '2015':
        meses15['out'].append(dia+'/'+mes+'/'+ano)
    if mes == '11' and ano == '2015':
        meses15['nov'].append(dia+'/'+mes+'/'+ano)
    if mes == '12' and ano == '2015':
        meses15['dez'].append(dia+'/'+mes+'/'+ano)
    return meses15    
        
## Função que cria um dicionario de listas, onde cada lista é uma estação 
## de 2014 e os valores são as strings com as datas de cada estação:
def organiza_estacoes14(dia, mes, ano):
    if ano == years[0]:
        if mes == '1' or mes == '2' or mes == '3' or mes == '4' or mes == '5':
            estacoes14['wet'].append(dia+'/'+mes+'/'+ano)
        elif mes == '6':
            estacoes14['t1a'].append(dia+'/'+mes+'/'+ano)
        elif mes == '7':
            estacoes14['t1b'].append(dia+'/'+mes+'/'+ano)
        elif mes == '8' or mes == '9':
            estacoes14['dry'].append(dia+'/'+mes+'/'+ano)
        elif mes == '10' or mes == '11':
            estacoes14['tr2'].append(dia+'/'+mes+'/'+ano)
        elif mes == '12':
            for i in list(np.arange(1, 16)):
                if dia == str(i):
                    estacoes14['tr2'].append(dia+'/'+mes+'/'+ano)
            for i in list(np.arange(16, 32)):
                if dia == str(i):
                    estacoes15['wet'].append(dia+'/'+mes+'/'+ano)  
    return estacoes14

## Função que cria um dicionario de listas, onde cada lista é uma estação 
## de 2015 e os valores são as strings com as datas de cada estação:
def organiza_estacoes15(dia, mes, ano):                    
    if ano == years[1]:
        if mes == '1' or mes == '2' or mes == '3' or mes == '4' or mes == '5':
            estacoes15['wet'].append(dia+'/'+mes+'/'+ano)
        elif mes == '6':
            estacoes15['t1a'].append(dia+'/'+mes+'/'+ano)
        elif mes == '7':
            estacoes15['t1b'].append(dia+'/'+mes+'/'+ano)
        elif mes == '8' or mes == '9':
            estacoes15['dry'].append(dia+'/'+mes+'/'+ano)
        elif mes == '10' or mes == '11' or mes == '12':
            estacoes15['tr2'].append(dia+'/'+mes+'/'+ano)
    return estacoes15
