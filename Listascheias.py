#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 17:26:41 2020

@author: andre
"""

def lista_todos_valores_juntos(lista_aux_com_os_dataframes):
    lista_final = []
    for i, dframe in enumerate(lista_aux_com_os_dataframes):
        ltemp = []
        for (columnName, columnData) in dframe.iteritems():
            for value in list(columnData.values):
                ltemp.append(value)
        lista_final.append(ltemp)
    return lista_final