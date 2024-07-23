#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 14:33:25 2020

@author: andre
"""

import copy
import pandas as pd

## Função que cria um Pandas Dataframe a partir de uma lista de listas:
def dframe_normal_semdatas(lista_com_os_dados):
    df = pd.DataFrame(data=lista_com_os_dados)
    return df

## Função que cria um Pandas Dataframe a partir de uma listas de listas, 
## porém transpõe linhas por colunas e ajusta os nomes das colunas de 
## acordo com uma lista de strings, onde cada string é uma data:
def dframe_transposto_comdatas(lista_com_os_dados, nomes_colunas):
    df = pd.DataFrame(data=lista_com_os_dados)
    dfdias = copy.deepcopy(df.T)
    dfdias.columns = nomes_colunas
    return dfdias