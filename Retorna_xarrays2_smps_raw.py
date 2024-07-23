#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 16:12:49 2021

@author: andre
"""

#import xarray
import numpy as np

# OBS: o '.where(drop=False)' funciona corretamente sim, o que ele faz é colocar NaN onde a condição dada para ele não é satisfeita. O 
# '.where(drop=True)' faz isso, mas ao invés de colocar NaN ele exclui a linha mesmo, mudando assim o tamanho do vetor. Ou seja, é melhor
# usar o '.where(drop=False)' mesmo!
def arrays(netcdf, variavel1, dimensao2, corte='PM2,5'):
    dimensoes = list(netcdf.dims)
    ###################################### GASES ##################################################
    ### Oxides of Nitrogen Analyzer:
    if variavel1 == 'no' or variavel1 == 'nox' or variavel1 == 'noy':
        raw1 = netcdf[variavel1]
    ### Carbon Monoxide Analyzer:
    elif variavel1 == 'co' or variavel1 == 'co_dry':
        raw1 = netcdf[variavel1]
        #raw1 = netcdf[variavel1].where((netcdf.gas_temperature>=26.0) & (netcdf.gas_temperature<=40.0) & \
        #                          (netcdf[variavel1]>-1) & (netcdf[variavel1]<3), drop=False)
    elif variavel1 == 'n2o' or variavel1 == 'n2o_dry':
        #raw1 = netcdf[variavel1].where((netcdf.gas_temperature>=26.0) & (netcdf.gas_temperature<=40.0) & \
        #                          (netcdf[variavel1]>-1) & (netcdf[variavel1]<50), drop=False)
        raw1 = netcdf[variavel1]
    ### Ozone Monitor:
    elif variavel1 == 'o3':
        raw1 = netcdf[variavel1]
        
    ###################################### AEROSSOIS ##################################################
    ### Aetalômetro:
    elif variavel1 == 'equivalent_black_carbon':
        #raw1 = netcdf[variavel1].sel(wavelength=str(netcdf[dimensao2].values[6])).where((netcdf.sample_flow_rate>1) & 
        #                                                                                  (netcdf.sample_flow_rate<8), drop=False)
        raw1 = netcdf[variavel1].sel(wavelength=str(netcdf[dimensao2].values[6]))
    ### CPCf e CPC:
    elif variavel1 == 'concentration':
        raw1 = netcdf[variavel1].where((netcdf.qc_concentration!=1) & (netcdf.qc_concentration!=2) & \
                                  (netcdf.qc_concentration!=5) & \
                                  (netcdf.qc_concentration!=6) & (netcdf.qc_concentration!=7) & \
                                  (netcdf.qc_concentration!=8) & (netcdf.qc_concentration!=9) & \
                                  (netcdf.qc_concentration!=10) & (netcdf.qc_concentration!=11) & \
                                  (netcdf.qc_concentration!=12) & (netcdf.qc_concentration!=13) & \
                                  (netcdf.qc_concentration!=14) & (netcdf.qc_concentration!=15) & \
                                  (netcdf.qc_concentration!=16) & (netcdf.qc_concentration!=17), drop=False)
    ### Nefelômetro (M1 e S1):
    elif variavel1 == 'Bs_B_Dry_Neph3W' and corte == 'PM2,5':
        #raw1 = netcdf[variavel1].where((netcdf.qc_Bs_B_Dry_Neph3W==0) & (netcdf.RH_Neph_Dry<70.0) & (netcdf[variavel1]<=1000.0) & \
        #                          (netcdf.impactor_state==1), drop=False)
        raw1 = netcdf[variavel1].where((netcdf.qc_Bs_B_Dry_Neph3W==0) & (netcdf.impactor_state==1), drop=False)
    elif variavel1 == 'Bs_G_Dry_Neph3W' and corte == 'PM2,5':
        #raw1 = netcdf[variavel1].where((netcdf.qc_Bs_G_Dry_Neph3W==0) & (netcdf.RH_Neph_Dry<70.0) & (netcdf[variavel1]<=1000.0) & \
        #                          (netcdf.impactor_state==1), drop=False)
        raw1 = netcdf[variavel1].where((netcdf.qc_Bs_G_Dry_Neph3W==0) & (netcdf.impactor_state==1), drop=False)
    elif variavel1 == 'Bs_R_Dry_Neph3W' and corte == 'PM2,5':
        #raw1 = netcdf[variavel1].where((netcdf.qc_Bs_R_Dry_Neph3W==0) & (netcdf.RH_Neph_Dry<70.0) & (netcdf[variavel1]<=1000.0) & \
        #                          (netcdf.impactor_state==1), drop=False)
        raw1 = netcdf[variavel1].where((netcdf.qc_Bs_R_Dry_Neph3W==0) & (netcdf.impactor_state==1), drop=False)
    elif variavel1 == 'Bs_B_Dry_Neph3W' and corte == 'PM10':
        #raw1 = netcdf[variavel1].where((netcdf.qc_Bs_B_Dry_Neph3W==0) & (netcdf.RH_Neph_Dry<70.0) & (netcdf[variavel1]<=1000.0) & \
        #                          (netcdf.impactor_state==10), drop=False)
        raw1 = netcdf[variavel1].where((netcdf.qc_Bs_B_Dry_Neph3W==0) & (netcdf.impactor_state==10), drop=False)
    elif variavel1 == 'Bs_G_Dry_Neph3W' and corte == 'PM10':
        #raw1 = netcdf[variavel1].where((netcdf.qc_Bs_G_Dry_Neph3W==0) & (netcdf.RH_Neph_Dry<70.0) & (netcdf[variavel1]<=1000.0) & \
        #                          (netcdf.impactor_state==10), drop=False)
        raw1 = netcdf[variavel1].where((netcdf.qc_Bs_G_Dry_Neph3W==0) & (netcdf.impactor_state==10), drop=False)
    elif variavel1 == 'Bs_R_Dry_Neph3W' and corte == 'PM10':
        #raw1 = netcdf[variavel1].where((netcdf.qc_Bs_R_Dry_Neph3W==0) & (netcdf.RH_Neph_Dry<70.0) & (netcdf[variavel1]<=1000.0) & \
        #                          (netcdf.impactor_state==10), drop=False)
        raw1 = netcdf[variavel1].where((netcdf.qc_Bs_R_Dry_Neph3W==0) & (netcdf.impactor_state==10), drop=False)
    elif variavel1 == 'Bs_G_Dry_Neph3W' and corte == 'no_impactor':
        raw1 = netcdf[variavel1].where((netcdf.qc_Bs_G_Dry_Neph3W==0) & (netcdf.impactor_state==11), drop=False)
    elif variavel1 == 'Bbs_G_Dry_Neph3W' and corte == 'PM2,5':
        raw1 = netcdf[variavel1].where((netcdf.qc_Bbs_G_Dry_Neph3W==0) & (netcdf.impactor_state==1), drop=False)
    elif variavel1 == 'Bbs_G_Dry_Neph3W' and corte == 'PM10':
        raw1 = netcdf[variavel1].where((netcdf.qc_Bbs_G_Dry_Neph3W==0) & (netcdf.impactor_state==10), drop=False)
    elif variavel1 == 'Bbs_G_Dry_Neph3W' and corte == 'no_impactor':
        raw1 = netcdf[variavel1].where((netcdf.qc_Bbs_G_Dry_Neph3W==0) & (netcdf.impactor_state==11), drop=False)
    ### PSAP (M1 e S1):
    elif variavel1 == 'Ba_B_Weiss' and corte == 'PM2,5':
        raw1 = netcdf[variavel1].where((netcdf.qc_Ba_B_Weiss==0) & (netcdf.impactor_state==1), drop=False)
    elif variavel1 == 'Ba_G_Weiss' and corte == 'PM2,5':
        raw1 = netcdf[variavel1].where((netcdf.qc_Ba_G_Weiss==0) & (netcdf.impactor_state==1), drop=False)
    elif variavel1 == 'Ba_R_Weiss' and corte == 'PM2,5':
        raw1 = netcdf[variavel1].where((netcdf.qc_Ba_R_Weiss==0) & (netcdf.impactor_state==1), drop=False)
    elif variavel1 == 'Ba_B_Weiss' and corte == 'PM10':
        raw1 = netcdf[variavel1].where((netcdf.qc_Ba_B_Weiss==0) & (netcdf.impactor_state==10), drop=False)
    elif variavel1 == 'Ba_G_Weiss' and corte == 'PM10':
        raw1 = netcdf[variavel1].where((netcdf.qc_Ba_G_Weiss==0) & (netcdf.impactor_state==10), drop=False)
    elif variavel1 == 'Ba_R_Weiss' and corte == 'PM10':
        raw1 = netcdf[variavel1].where((netcdf.qc_Ba_R_Weiss==0) & (netcdf.impactor_state==10), drop=False) 
    ### AIP1OGRENM1 - VAP que pega dados do Nefelômetro M1 e do PSAP M1 para calcular propriedades intensivas do aerossol:
    elif variavel1 == 'Ba_G_Dry_1um_PSAP3W_1':
        raw1 = netcdf[variavel1].where((netcdf.qc_Ba_G_Dry_1um_PSAP3W_1==0), drop=False)
    elif variavel1 == 'Bs_G_Dry_1um_Neph3W_1':
        raw1 = netcdf[variavel1].where((netcdf.qc_Bs_G_Dry_1um_Neph3W_1==0), drop=False)
    elif variavel1 == 'Bbs_G_Dry_1um_Neph3W_1':
        raw1 = netcdf[variavel1].where((netcdf.qc_Bbs_G_Dry_1um_Neph3W_1==0), drop=False)
    elif variavel1 == 'ssa_G_Dry_1um':
        raw1 = netcdf[variavel1].where((netcdf.qc_ssa_G_Dry_1um==0), drop=False)
    elif variavel1 == 'bsf_G_Dry_1um':
        raw1 = netcdf[variavel1].where((netcdf.qc_bsf_G_Dry_1um==0), drop=False)
    elif variavel1 == 'Bs_angstrom_exponent_BG_Dry_1um':
        raw1 = netcdf[variavel1].where((netcdf.qc_Bs_angstrom_exponent_BG_Dry_1um==0), drop=False)
    elif variavel1 == 'Ba_G_Dry_10um_PSAP3W_1':
        raw1 = netcdf[variavel1].where((netcdf.qc_Ba_G_Dry_10um_PSAP3W_1==0), drop=False)
    elif variavel1 == 'Bs_G_Dry_10um_Neph3W_1':
        raw1 = netcdf[variavel1].where((netcdf.qc_Bs_G_Dry_10um_Neph3W_1==0), drop=False)
    elif variavel1 == 'Bbs_G_Dry_10um_Neph3W_1':
        raw1 = netcdf[variavel1].where((netcdf.qc_Bbs_G_Dry_10um_Neph3W_1==0), drop=False)
    elif variavel1 == 'Bs_B_Dry_1um_Neph3W_1':
        raw1 = netcdf[variavel1].where((netcdf.qc_Bs_B_Dry_1um_Neph3W_1==0), drop=False)
    ### SP2:
    elif variavel1 == 'rBC':
        raw1 = netcdf[variavel1].where(netcdf.qc_rBC==0, drop=False)
    ### UHSAS:
    elif variavel1 == 'utotal_N_conc':
        raw1 = netcdf[variavel1[1:]].where((netcdf.qc_total_N_conc==0), drop=False)
    elif variavel1 == 'udN_dlogDp':
        print('Esse código ainda não foi implementado! Quando for, não esqueça de colocar o [1:] depois do variavel1!')
        return
    elif variavel1 == 'total_SA_conc':
        raw1 = netcdf[variavel1].where((netcdf.qc_total_SA_conc==0), drop=False)
    elif variavel1 == 'total_V_conc':
        raw1 = netcdf[variavel1].where((netcdf.qc_total_V_conc==0), drop=False)
    ### MFRSRAOD1MICH:
    elif variavel1 == 'aerosol_optical_depth_filter1':
        raw1 = netcdf[variavel1].where((netcdf.qc_aerosol_optical_depth_filter1==0), drop=False)
    elif variavel1 == 'aerosol_optical_depth_filter2':
        raw1 = netcdf[variavel1].where((netcdf.qc_aerosol_optical_depth_filter2==0), drop=False)
    elif variavel1 == 'aerosol_optical_depth_filter3':
        raw1 = netcdf[variavel1].where((netcdf.qc_aerosol_optical_depth_filter3==0), drop=False)
    elif variavel1 == 'aerosol_optical_depth_filter4':
        raw1 = netcdf[variavel1].where((netcdf.qc_aerosol_optical_depth_filter4==0), drop=False)
    elif variavel1 == 'aerosol_optical_depth_filter5':
        raw1 = netcdf[variavel1].where((netcdf.qc_aerosol_optical_depth_filter5==0), drop=False)
    ### CCNcol1b1:
    elif variavel1 == 'N_CCN' and dimensoes != ['bound', 'size_bin', 'time']:
        raw1 = netcdf[variavel1].where(netcdf.qc_N_CCN==0, drop=False)
    ### CCN100M1_a1:
    elif variavel1 == 'N_CCN' and dimensoes == ['bound', 'size_bin', 'time']:
        raw1 = netcdf[variavel1]
    ### ACSM:
    elif variavel1 == 'total_organics':
        raw1 = netcdf[variavel1].where((netcdf.qc_total_organics==0), drop=False)
    ### SMPS:
    elif variavel1 == 'total_concentration':
        raw1 = netcdf[variavel1].where((netcdf.status_flag==0), drop=False)
    elif variavel1 == 'number_size_distribution':
        if len(netcdf.diameter_midpoint)==104:
            num_de_diametros_70 = 52
        if len(netcdf.diameter_midpoint)==106:
            num_de_diametros_70 = 53
        elif len(netcdf.diameter_midpoint)==108:
            num_de_diametros_70 = 54
        # Calculando a somabins, que equivale a 100%:
        dados_com_log_bin = []  # Lista de xarrays
        for i in range(len(netcdf.diameter_midpoint)):
            if i != (len(netcdf.diameter_midpoint)-1):
            #if i != 103:
                diamsup = float(netcdf.diameter_midpoint[i+1].values)
                diambin = float(netcdf.diameter_midpoint[i].values)
                #dif = diamsup-diambin
                log = np.log10(diamsup/diambin)
                dadobin = netcdf.number_size_distribution.isel(diameter_midpoint=i).where((netcdf.status_flag==0),drop=False)
                resultbin = dadobin*log
                dados_com_log_bin.append(resultbin)
                if dados_com_log_bin[i].isnull().all() == True:
                    dados_com_log_bin[i] = dados_com_log_bin[i].fillna(0.0)
            else:
                diamsup = float(netcdf.diameter_midpoint[i].values)
                diambin = float(netcdf.diameter_midpoint[i-1].values)
                #diam = float(netcdf.diameter_midpoint[i].values)
                #dif = diamsup-diambin
                log = np.log10(diamsup/diambin)
                dadobin = netcdf.number_size_distribution.isel(diameter_midpoint=i).where((netcdf.status_flag==0),drop=False)
                resultbin = dadobin*log
                dados_com_log_bin.append(resultbin)
                if dados_com_log_bin[i].isnull().all() == True:
                    dados_com_log_bin[i] = dados_com_log_bin[i].fillna(0.0)
        somabins = sum(dados_com_log_bin)
        # Calculando a somabins7, somente referente aos diâmetros menores que 70:
        dados_com_log_bin7 = []  # Lista de xarrays
        for i in range(num_de_diametros_70):
            if i != (num_de_diametros_70-1):
            #if i != 51:
                diamsup7 = float(netcdf.diameter_midpoint[i+1].values)
                diambin7 = float(netcdf.diameter_midpoint[i].values)
                #dif7 = diamsup7-diambin7
                log7 = np.log10(diamsup7/diambin7)
                dadobin7 = netcdf.number_size_distribution.isel(diameter_midpoint=i).where((netcdf.status_flag==0),drop=False)
                resultbin7 = dadobin7*log7
                dados_com_log_bin7.append(resultbin7)
                if dados_com_log_bin7[i].isnull().all() == True:
                    dados_com_log_bin7[i] = dados_com_log_bin7[i].fillna(0.0)
            else:
                diamsup7 = float(netcdf.diameter_midpoint[i].values)
                diambin7 = float(netcdf.diameter_midpoint[i-1].values)
                #diam7 = float(netcdf.diameter_midpoint[i].values)
                #dif7 = diamsup7-diambin7
                log7 = np.log10(diamsup7/diambin7)
                dadobin7 = netcdf.number_size_distribution.isel(diameter_midpoint=i).where((netcdf.status_flag==0),drop=False)
                resultbin7 = dadobin7*log7
                dados_com_log_bin7.append(resultbin7)
                if dados_com_log_bin7[i].isnull().all() == True:
                    dados_com_log_bin7[i] = dados_com_log_bin7[i].fillna(0.0)
        somabins7 = sum(dados_com_log_bin7)
        raw1 = (somabins7*100)/(somabins)
        #dados_com_log_bin = []  # Lista de xarrays
        #for i in range(52):
        #    diamsup = float(netcdf.diameter_midpoint[i+1].values)
        #    diambin = float(netcdf.diameter_midpoint[i].values)
        #    logaritmo = np.log10(diamsup/diambin)
        #    dadobin = netcdf.number_size_distribution.isel(diameter_midpoint=i).where((netcdf.status_flag==0), drop=False)
        #    resultbin = dadobin*logaritmo
        #    dados_com_log_bin.append(resultbin)
        #    if dados_com_log_bin[i].isnull().all() == True:
        #        dados_com_log_bin[i] = dados_com_log_bin[i].fillna(0.0)
        #somabins = sum(dados_com_log_bin) 
        #raw1 = (somabins*100)/(netcdf.total_concentration.where((netcdf.status_flag==0), drop=False))
    ### SMPSb1:
    elif variavel1 == 'total_N_conc':
        raw1 = netcdf[variavel1].where((netcdf.status_flag==0) & (netcdf.qc_total_N_conc==0), drop=False)
    elif variavel1 == 'dN_dlogDp':
        if len(netcdf.diameter_mobility)==104:
            num_de_diametros_70 = 52
        if len(netcdf.diameter_mobility)==106:
            num_de_diametros_70 = 53
        elif len(netcdf.diameter_mobility)==108:
            num_de_diametros_70 = 54
        # Calculando a somabins, que equivale a 100%:
        dados_com_log_bin = []  # Lista de xarrays
        for i in range(len(netcdf.diameter_mobility)):
            if i != (len(netcdf.diameter_mobility)-1):
            #if i != 103:
                diamsup = float(netcdf.diameter_mobility[i+1].values)
                diambin = float(netcdf.diameter_mobility[i].values)
                #dif = diamsup-diambin
                log = np.log10(diamsup/diambin)
                dadobin = netcdf.dN_dlogDp.isel(diameter_mobility=i).where((netcdf.status_flag==0) & (netcdf.qc_dN_dlogDp.isel(diameter_mobility=i)==0),drop=False)
                resultbin = dadobin*log
                dados_com_log_bin.append(resultbin)
                if dados_com_log_bin[i].isnull().all() == True:
                    dados_com_log_bin[i] = dados_com_log_bin[i].fillna(0.0)
            else:
                diamsup = float(netcdf.diameter_mobility[i].values)
                diambin = float(netcdf.diameter_mobility[i-1].values)
                #diam = float(netcdf.diameter_mobility[i].values)
                #dif = diamsup-diambin
                log = np.log10(diamsup/diambin)
                dadobin = netcdf.dN_dlogDp.isel(diameter_mobility=i).where((netcdf.status_flag==0) & (netcdf.qc_dN_dlogDp.isel(diameter_mobility=i)==0),drop=False)
                resultbin = dadobin*log
                dados_com_log_bin.append(resultbin)
                if dados_com_log_bin[i].isnull().all() == True:
                    dados_com_log_bin[i] = dados_com_log_bin[i].fillna(0.0)
        somabins = sum(dados_com_log_bin)
        # Calculando a somabins7, somente referente aos diâmetros menores que 70:
        dados_com_log_bin7 = []  # Lista de xarrays
        for i in range(num_de_diametros_70):
            if i != (num_de_diametros_70-1):
            #if i != 51:
                diamsup7 = float(netcdf.diameter_mobility[i+1].values)
                diambin7 = float(netcdf.diameter_mobility[i].values)
                #dif7 = diamsup7-diambin7
                log7 = np.log10(diamsup7/diambin7)
                dadobin7 = netcdf.dN_dlogDp.isel(diameter_mobility=i).where((netcdf.status_flag==0) & (netcdf.qc_dN_dlogDp.isel(diameter_mobility=i)==0),drop=False)
                resultbin7 = dadobin7*log7
                dados_com_log_bin7.append(resultbin7)
                if dados_com_log_bin7[i].isnull().all() == True:
                    dados_com_log_bin7[i] = dados_com_log_bin7[i].fillna(0.0)
            else:
                diamsup7 = float(netcdf.diameter_mobility[i].values)
                diambin7 = float(netcdf.diameter_mobility[i-1].values)
                #diam7 = float(netcdf.diameter_mobility[i].values)
                #dif7 = diamsup7-diambin7
                log7 = np.log10(diamsup7/diambin7)
                dadobin7 = netcdf.dN_dlogDp.isel(diameter_mobility=i).where((netcdf.status_flag==0) & (netcdf.qc_dN_dlogDp.isel(diameter_mobility=i)==0),drop=False)
                resultbin7 = dadobin7*log7
                dados_com_log_bin7.append(resultbin7)
                if dados_com_log_bin7[i].isnull().all() == True:
                    dados_com_log_bin7[i] = dados_com_log_bin7[i].fillna(0.0)
        somabins7 = sum(dados_com_log_bin7)
        raw1 = (somabins7*100)/(somabins)
        #dados_com_log_bin = []  # Lista de xarrays
        #for i in range(52):
        #    diamsup = float(netcdf.diameter_mobility[i+1].values)
        #    diambin = float(netcdf.diameter_mobility[i].values)
        #    logaritmo = np.log10(diamsup/diambin)
        #    dadobin = netcdf.dN_dlogDp.isel(diameter_mobility=i).where((netcdf.status_flag==0) & (netcdf.qc_dN_dlogDp.isel(diameter_mobility=i)==0), drop=False)
        #    resultbin = dadobin*logaritmo
        #    dados_com_log_bin.append(resultbin)
        #    if dados_com_log_bin[i].isnull().all() == True:
        #        dados_com_log_bin[i] = dados_com_log_bin[i].fillna(0.0)
        #somabins = sum(dados_com_log_bin) 
        #raw1 = (somabins*100)/(netcdf.total_concentration.where((netcdf.status_flag==0) & (netcdf.qc_dN_dlogDp.isel(diameter_mobility=i)==0), drop=False))    
    
    ###################################### NUVENS ##################################################
    ### mwr3c:
    elif (variavel1 == 'lwp' or variavel1 == 'pwv') and dimensoes == ['time']:
        raw1 = netcdf[variavel1].where(netcdf.qc_time==0, drop=False)
    ### mwrlos:
    elif variavel1 == 'liq':
        raw1 = netcdf[variavel1].where((netcdf.qc_time==0) & (netcdf.qc_liq==0), drop=False)
    ### ldquants:
    elif variavel1 == 'lwc':
        raw1 = netcdf[variavel1]
    ### microbase:
    elif variavel1 == 'liquid_water_content':
        # raw1 = netcdf[variavel1].isel(height=0).where((netcdf.qc_liquid_water_content.isel(height=0)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=1).where((netcdf.qc_liquid_water_content.isel(height=1)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=2).where((netcdf.qc_liquid_water_content.isel(height=2)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=3).where((netcdf.qc_liquid_water_content.isel(height=3)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=4).where((netcdf.qc_liquid_water_content.isel(height=4)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=5).where((netcdf.qc_liquid_water_content.isel(height=5)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=6).where((netcdf.qc_liquid_water_content.isel(height=6)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=7).where((netcdf.qc_liquid_water_content.isel(height=7)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=8).where((netcdf.qc_liquid_water_content.isel(height=8)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=9).where((netcdf.qc_liquid_water_content.isel(height=9)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=10).where((netcdf.qc_liquid_water_content.isel(height=10)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=11).where((netcdf.qc_liquid_water_content.isel(height=11)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=12).where((netcdf.qc_liquid_water_content.isel(height=12)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=13).where((netcdf.qc_liquid_water_content.isel(height=13)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=14).where((netcdf.qc_liquid_water_content.isel(height=14)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=15).where((netcdf.qc_liquid_water_content.isel(height=15)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=16).where((netcdf.qc_liquid_water_content.isel(height=16)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=17).where((netcdf.qc_liquid_water_content.isel(height=17)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=18).where((netcdf.qc_liquid_water_content.isel(height=18)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=19).where((netcdf.qc_liquid_water_content.isel(height=19)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=20).where((netcdf.qc_liquid_water_content.isel(height=20)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=21).where((netcdf.qc_liquid_water_content.isel(height=21)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        raw1 = netcdf[variavel1].isel(height=22).where((netcdf.qc_liquid_water_content.isel(height=22)==0) & \
                                                                (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=23).where((netcdf.qc_liquid_water_content.isel(height=23)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=24).where((netcdf.qc_liquid_water_content.isel(height=24)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=25).where((netcdf.qc_liquid_water_content.isel(height=25)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=26).where((netcdf.qc_liquid_water_content.isel(height=26)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=27).where((netcdf.qc_liquid_water_content.isel(height=27)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=28).where((netcdf.qc_liquid_water_content.isel(height=28)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=29).where((netcdf.qc_liquid_water_content.isel(height=29)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=30).where((netcdf.qc_liquid_water_content.isel(height=30)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=31).where((netcdf.qc_liquid_water_content.isel(height=31)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=32).where((netcdf.qc_liquid_water_content.isel(height=32)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=33).where((netcdf.qc_liquid_water_content.isel(height=33)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=34).where((netcdf.qc_liquid_water_content.isel(height=34)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=35).where((netcdf.qc_liquid_water_content.isel(height=35)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=36).where((netcdf.qc_liquid_water_content.isel(height=36)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=37).where((netcdf.qc_liquid_water_content.isel(height=37)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=38).where((netcdf.qc_liquid_water_content.isel(height=38)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=39).where((netcdf.qc_liquid_water_content.isel(height=39)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=40).where((netcdf.qc_liquid_water_content.isel(height=40)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=41).where((netcdf.qc_liquid_water_content.isel(height=41)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=42).where((netcdf.qc_liquid_water_content.isel(height=42)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=43).where((netcdf.qc_liquid_water_content.isel(height=43)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=44).where((netcdf.qc_liquid_water_content.isel(height=44)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=45).where((netcdf.qc_liquid_water_content.isel(height=45)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=46).where((netcdf.qc_liquid_water_content.isel(height=46)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=47).where((netcdf.qc_liquid_water_content.isel(height=47)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=48).where((netcdf.qc_liquid_water_content.isel(height=48)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=49).where((netcdf.qc_liquid_water_content.isel(height=49)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=50).where((netcdf.qc_liquid_water_content.isel(height=50)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=51).where((netcdf.qc_liquid_water_content.isel(height=51)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=52).where((netcdf.qc_liquid_water_content.isel(height=52)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=53).where((netcdf.qc_liquid_water_content.isel(height=53)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=54).where((netcdf.qc_liquid_water_content.isel(height=54)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=55).where((netcdf.qc_liquid_water_content.isel(height=55)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=56).where((netcdf.qc_liquid_water_content.isel(height=56)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=57).where((netcdf.qc_liquid_water_content.isel(height=57)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=58).where((netcdf.qc_liquid_water_content.isel(height=58)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=59).where((netcdf.qc_liquid_water_content.isel(height=59)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=60).where((netcdf.qc_liquid_water_content.isel(height=60)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=61).where((netcdf.qc_liquid_water_content.isel(height=61)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=62).where((netcdf.qc_liquid_water_content.isel(height=62)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=63).where((netcdf.qc_liquid_water_content.isel(height=63)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=64).where((netcdf.qc_liquid_water_content.isel(height=64)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=65).where((netcdf.qc_liquid_water_content.isel(height=65)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=66).where((netcdf.qc_liquid_water_content.isel(height=66)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=67).where((netcdf.qc_liquid_water_content.isel(height=67)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=68).where((netcdf.qc_liquid_water_content.isel(height=68)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=69).where((netcdf.qc_liquid_water_content.isel(height=69)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=70).where((netcdf.qc_liquid_water_content.isel(height=70)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=71).where((netcdf.qc_liquid_water_content.isel(height=71)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=72).where((netcdf.qc_liquid_water_content.isel(height=72)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=73).where((netcdf.qc_liquid_water_content.isel(height=73)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=74).where((netcdf.qc_liquid_water_content.isel(height=74)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=75).where((netcdf.qc_liquid_water_content.isel(height=75)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=76).where((netcdf.qc_liquid_water_content.isel(height=76)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=77).where((netcdf.qc_liquid_water_content.isel(height=77)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=78).where((netcdf.qc_liquid_water_content.isel(height=78)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=79).where((netcdf.qc_liquid_water_content.isel(height=79)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=80).where((netcdf.qc_liquid_water_content.isel(height=80)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=81).where((netcdf.qc_liquid_water_content.isel(height=81)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=82).where((netcdf.qc_liquid_water_content.isel(height=82)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=83).where((netcdf.qc_liquid_water_content.isel(height=83)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=84).where((netcdf.qc_liquid_water_content.isel(height=84)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=85).where((netcdf.qc_liquid_water_content.isel(height=85)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=86).where((netcdf.qc_liquid_water_content.isel(height=86)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=87).where((netcdf.qc_liquid_water_content.isel(height=87)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=88).where((netcdf.qc_liquid_water_content.isel(height=88)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=89).where((netcdf.qc_liquid_water_content.isel(height=89)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=90).where((netcdf.qc_liquid_water_content.isel(height=90)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=91).where((netcdf.qc_liquid_water_content.isel(height=91)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=92).where((netcdf.qc_liquid_water_content.isel(height=92)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=93).where((netcdf.qc_liquid_water_content.isel(height=93)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=94).where((netcdf.qc_liquid_water_content.isel(height=94)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=95).where((netcdf.qc_liquid_water_content.isel(height=95)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=96).where((netcdf.qc_liquid_water_content.isel(height=96)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=97).where((netcdf.qc_liquid_water_content.isel(height=97)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=98).where((netcdf.qc_liquid_water_content.isel(height=98)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
        # raw1 = netcdf[variavel1].isel(height=99).where((netcdf.qc_liquid_water_content.isel(height=99)==0) & \
        #                                                         (netcdf.clear_cloud_flag==1), drop=False)
    ### mwrp:
    elif variavel1 == 'liquidWaterPath':
        raw1 = netcdf[variavel1].where((netcdf.qc_time==0) & (netcdf.qc_liquidWaterPath==0), drop=False)
    elif variavel1 == 'totalPrecipitableWater':
        raw1 = netcdf[variavel1].where((netcdf.qc_time==0) & (netcdf.qc_totalPrecipitableWater==0), drop=False)
    elif variavel1 == 'cape':
        raw1 = netcdf[variavel1].where((netcdf.qc_time==0) & (netcdf.qc_cape==0), drop=False)
    elif variavel1 == 'cloudBaseHeight':
        raw1 = netcdf[variavel1].where((netcdf.qc_time==0) & (netcdf.qc_cloudBaseHeight==0), drop=False)
    elif variavel1 == 'liftingCondensationLevel':
        raw1 = netcdf[variavel1].where((netcdf.qc_time==0) & (netcdf.qc_liftingCondensationLevel==0), drop=False)
    ### radflux1long:
    elif variavel1 == 'visible_cloud_optical_depth' or variavel1 == 'cloud_transmissivity_shortwave':
        #raw1 = netcdf[variavel1]
        raw1 = netcdf[variavel1].where((netcdf.cloudfraction_shortwave>=0.9) & (netcdf.clearsky_status==0), drop=False) 
        #raw1 = netcdf[variavel1].where((netcdf.cloudfraction_shortwave_status==8) & (netcdf.cloudfraction_shortwave>0.9), drop=False) 
    elif variavel1 == 'cloudfraction_shortwave':
        raw1 = netcdf[variavel1].where((netcdf.clearsky_status==0), drop=False)
    elif variavel1 == 'downwelling_shortwave':
        #raw1 = netcdf[variavel1].where((netcdf.qc_downwelling_shortwave==0), drop=False)
        raw1 = netcdf[variavel1].where((netcdf.qc_downwelling_shortwave==0) & (netcdf.cloudfraction_shortwave>=0.9) & \
                                       (netcdf.clearsky_status==0), drop=False)
    elif variavel1 == 'clearsky_downwelling_shortwave':
        raw1 = netcdf[variavel1]
    elif variavel1 == 'cosine_zenith':
        raw1 = netcdf[variavel1]
    elif variavel1 == 'upwelling_shortwave':
        #raw1 = netcdf[variavel1].where((netcdf.qc_upwelling_shortwave==0), drop=False)
        raw1 = netcdf[variavel1].where((netcdf.qc_upwelling_shortwave==0) & (netcdf.cloudfraction_shortwave>=0.9) & \
                                       (netcdf.clearsky_status==0), drop=False)
    elif variavel1 == 'direct_downwelling_shortwave':
        #raw1 = netcdf[variavel1].where((netcdf.qc_direct_downwelling_shortwave==0), drop=False)
        raw1 = netcdf[variavel1].where((netcdf.qc_direct_downwelling_shortwave==0) & (netcdf.cloudfraction_shortwave>=0.9) & \
                                       (netcdf.clearsky_status==0), drop=False)
    ### ceil - ceilômetro:
    elif variavel1 == 'first_cbh':
        raw1 = netcdf[variavel1].where((netcdf.qc_first_cbh==0) & (netcdf.status_flag==0), drop=False)
    elif variavel1 == 'second_cbh':
        raw1 = netcdf[variavel1].where((netcdf.qc_second_cbh==0) & (netcdf.status_flag==0), drop=False)
    elif variavel1 == 'third_cbh':
        raw1 = netcdf[variavel1].where((netcdf.qc_third_cbh==0) & (netcdf.status_flag==0), drop=False)
    ### MPLWang:
    elif variavel1 == 'cloud_base' or variavel1 == 'cloud_top':
        raw1 = netcdf[variavel1].where(netcdf[variavel1]>-1, drop=False)
    ### WACR1 e WACRBND1:
    elif variavel1 == 'cloud_base_best_estimate' and dimensoes != ['height', 'numlayers', 'time']:
        raw1 = netcdf[variavel1].where((netcdf.qc_cloud_base_best_estimate==0) & (netcdf.qc_time==0) & \
                                  (netcdf.missing_data_flag == 0), drop=False)
    elif variavel1 == 'cloud_layer_base_height' and dimensoes != ['height', 'numlayers', 'time']:
        #raw1 = netcdf[variavel1].sel(layer=1).where((netcdf.qc_cloud_layer_base_height.sel(layer=1)==0) & (netcdf.missing_data_flag==0), drop=False)
        raw1 = netcdf[variavel1].sel(layer=0,method='nearest').where((netcdf.qc_cloud_layer_base_height.sel(layer=0,method='nearest')==0) & (netcdf.missing_data_flag==0), drop=False)
    elif variavel1 == 'radar_first_top' and dimensoes != ['height', 'numlayers', 'time']:
        raw1 = netcdf[variavel1].where((netcdf.qc_radar_first_top==0) & (netcdf.qc_time==0) & \
                                  (netcdf.missing_data_flag == 0), drop=False)
    elif variavel1 == 'cloud_layer_top_height' and dimensoes != ['height', 'numlayers', 'time']:
        #raw1 = netcdf[variavel1].sel(layer=1).where((netcdf.qc_cloud_layer_top_height.sel(layer=1)==0) & (netcdf.missing_data_flag==0), drop=False)
        raw1 = netcdf[variavel1].sel(layer=0,method='nearest').where((netcdf.qc_cloud_layer_top_height.sel(layer=0,method='nearest')==0) & (netcdf.missing_data_flag==0), drop=False)
    ### TSISKYCOVER:
    elif variavel1 == 'percent_opaque':
        raw1 = netcdf[variavel1].where((netcdf.qc_percent_opaque==0) & (netcdf.qc_time==0), drop=False)
    elif variavel1 == 'percent_thin':
        raw1 = netcdf[variavel1].where((netcdf.qc_percent_thin==0) & (netcdf.qc_time==0), drop=False)
    elif variavel1 == 'sunny':
        raw1 = netcdf[variavel1].where((netcdf.qc_sunny==0) & (netcdf.qc_time==0), drop=False)
    ### MWRRETRIEVALS:
    elif variavel1 == 'be_lwp':
        raw1 = netcdf[variavel1].where((netcdf.qc_be_lwp==0) & (netcdf.qc_time==0), drop=False)
    elif variavel1 == 'be_pwv':
        raw1 = netcdf[variavel1].where((netcdf.qc_be_pwv==0) & (netcdf.qc_time==0), drop=False)
    ### FENG:
    elif variavel1 == 'cloud_base_best_estimate' and dimensoes == ['height', 'numlayers', 'time']:
        teste = 'reflectivity_WACR_MAX' in list(netcdf.variables)
        if teste == False:
            raw1 = netcdf[variavel1].where((netcdf.missing_data_flag==0), drop=False)
        elif teste == True:
            raw1 = netcdf[variavel1].where((netcdf.reflectivity_WACR_MAX<-17.0), drop=False)
    elif variavel1 == 'cloud_layer_base_height_WACR' and dimensoes == ['height', 'numlayers', 'time']:
        teste = 'reflectivity_WACR_MAX' in list(netcdf.variables)
        if teste == False:
            raw1 = netcdf[variavel1].sel(numlayers=0).where((netcdf.missing_data_flag==0), drop=False)
        elif teste == True:
            raw1 = netcdf[variavel1].sel(numlayers=0).where((netcdf.reflectivity_WACR_MAX<-17.0), drop=False)
    elif variavel1 == 'radar_first_top_WACR' and dimensoes == ['height', 'numlayers', 'time']:
        teste = 'reflectivity_WACR_MAX' in list(netcdf.variables)
        if teste == False:
            raw1 = netcdf[variavel1].where((netcdf.missing_data_flag==0), drop=False)
        elif teste == True:
            raw1 = netcdf[variavel1].where((netcdf.reflectivity_WACR_MAX<-17.0), drop=False)
        raw1 = netcdf[variavel1].where((netcdf.missing_data_flag==0), drop=False)
    elif variavel1 == 'cloud_layer_top_height_WACR' and dimensoes == ['height', 'numlayers', 'time']:
        teste = 'reflectivity_WACR_MAX' in list(netcdf.variables)
        if teste == False:
            raw1 = netcdf[variavel1].sel(numlayers=0).where((netcdf.missing_data_flag==0), drop=False)
        elif teste == True:
            raw1 = netcdf[variavel1].sel(numlayers=0).where((netcdf.reflectivity_WACR_MAX<-17.0), drop=False)
    elif variavel1 == 'lwp' and dimensoes == ['height', 'numlayers', 'time']:
        teste = 'reflectivity_WACR_MAX' in list(netcdf.variables)
        if teste == False:
            raw1 = netcdf[variavel1].where((netcdf.missing_data_flag==0), drop=False)
        elif teste == True:
            raw1 = netcdf[variavel1].where((netcdf.reflectivity_WACR_MAX<-17.0), drop=False)
    elif variavel1 == 'pressure' and dimensoes == ['height', 'numlayers', 'time']:
        #ttt = netcdf['time_offset'].values
        #raw = netcdf.assign_coords({"time": (['time'], ttt)})
        #raw1 = raw[variavel1].isel(height=599)
        ## Dados coletados a 18.23 m de altura:
        #raw1 = netcdf[variavel1].isel(height=599)
        ## Dados coletados a 10.01 m de altura:
        #raw1 = netcdf[variavel1].isel(height=325)
        ## Dados coletados a 5.0 m de altura:
        #raw1 = netcdf[variavel1].isel(height=158)
        ## Dados coletados a 2.0 m de altura:
        raw1 = netcdf[variavel1].isel(height=58)
    elif variavel1 == 'temperature' and dimensoes == ['height', 'numlayers', 'time']:
        #ttt = netcdf['time_offset'].values
        #raw = netcdf.assign_coords({"time": (['time'], ttt)})
        #raw1 = raw[variavel1].isel(height=599)
        ## Dados coletados a 18.23 m de altura:
        #raw1 = netcdf[variavel1].isel(height=599)
        ## Dados coletados a 10.01 m de altura:
        #raw1 = netcdf[variavel1].isel(height=325)
        ## Dados coletados a 5.0 m de altura:
        #raw1 = netcdf[variavel1].isel(height=158)
        ## Dados coletados a 2.0 m de altura:
        raw1 = netcdf[variavel1].isel(height=58)
    elif variavel1 == 'rh' and dimensoes == ['height', 'numlayers', 'time']:
        #ttt = netcdf['time_offset'].values
        #raw = netcdf.assign_coords({"time": (['time'], ttt)})
        #raw1 = raw[variavel1].isel(height=599)
        ## Dados coletados a 18.23 m de altura:
        #raw1 = netcdf[variavel1].isel(height=599)
        ## Dados coletados a 10.01 m de altura:
        #raw1 = netcdf[variavel1].isel(height=325)
        ## Dados coletados a 5.0 m de altura:
        #raw1 = netcdf[variavel1].isel(height=158)
        ## Dados coletados a 2.0 m de altura:
        raw1 = netcdf[variavel1].isel(height=58)
    elif variavel1 == 'reflectivity_WACR' and dimensoes == ['height', 'numlayers', 'time']:
        raw1 = netcdf[variavel1].isel(height=0).where((netcdf.missing_data_flag==0), drop=False)
    ### MFRSRCLDO1MIN:
    elif variavel1 == 'optical_depth_instantaneous':
        raw1 = netcdf[variavel1].where((netcdf.qc_optical_depth_instantaneous==0), drop=False)
    elif variavel1 == 'effective_radius_instantaneous':
        raw1 = netcdf[variavel1].where((netcdf.qc_effective_radius_instantaneous==0), drop=False)
    ###################################### Estado Atmosférico ##################################################
    ### AOSMETS1:
    elif variavel1 == 'P_Ambient' or variavel1 == 'T_Ambient' or variavel1 == 'RH_Ambient' or variavel1 == 'rain_amount' or variavel1 == 'rain_intensity':
        raw1 = netcdf[variavel1]
    ### FENG:
    elif variavel1 == 'rainrate_pwd' or variavel1 == 'rainrate_tippingbucket' or variavel1 == 'rainrate_disdrometer':
        raw1 = netcdf[variavel1]
    ### METM1:
    elif variavel1 == 'org_precip_rate_mean':
        ##raw1 = netcdf[variavel1].where((netcdf.qc_org_precip_rate_mean==0), drop=False)
        raw1 = netcdf[variavel1].where((netcdf.qc_org_precip_rate_mean==0) & (netcdf.pwd_pw_code_inst>0) & (netcdf.qc_pwd_pw_code_inst==0), drop=False)
    ### SONDE:
    elif variavel1 == 'tdry':
        raw1 = netcdf.where((netcdf.tdry>=-90) & (netcdf.tdry<=50) & (netcdf.qc_tdry==0) \
               & (netcdf.qc_pres==0) & (netcdf.pres<=1100.0) & (netcdf.pres>=1000.0), drop=True)[variavel1]
    ### INTERPOLATEDSONDE - o "isel(height=1)" é para pegar dados a 20m acima do nível do solo no T3:
    elif variavel1 == 'bar_pres':
        raw1 = netcdf[variavel1].where((netcdf.qc_bar_pres==0), drop=False).isel(height=1)
    elif variavel1 == 'temp':
        raw1 = netcdf[variavel1].where((netcdf.qc_temp==0), drop=False).isel(height=1)
    elif variavel1 == 'rh':
        raw1 = netcdf[variavel1].where((netcdf.qc_rh==0), drop=False).isel(height=1)
    elif variavel1 == 'theta_superficie':
        raw1 = netcdf[variavel1].where((netcdf.qc_potential_temp==0), drop=False).isel(height=0)
    elif variavel1 == 'theta_700hPa':
        raw1 = netcdf[variavel1].where((netcdf.qc_potential_temp==0), drop=False).isel(height=156)
    ### DLSTATSNEWS:    
    elif variavel1 == 'cbw':
        raw1 = netcdf[variavel1]
        
    return raw1