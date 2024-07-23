#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 11:26:42 2021

@author: andre
"""
import os
import glob

rootS = '/mnt/HD_500GB_WD/01_Dados_ARM/'
rootD = '/mnt/HD_500GB_WD/01_Dados_ARM/'

folder = ['Gases','Aerossois','Estado_Atmosferico','Nuvens']

gas = ['aosnoxS1', 'aoscoS1', 'aoso3S1']
aero = ['aosaeth1spotS1','aoscpcfS1','aosnephdry1mM1','aosnephdry1mS1','aospsap3w1mM1','aospsap3w1mS1','aossmpsS1','aossp2rbc1mS1',
        'aosnephdryM1_Glauber','aoscpcM1b1','aossmpsS1b1','aip1ogrenM1','aosuhsasS1','aosmfrsraod1michM1','aosccn1colM1_b1',
        'aosccn100M1_a1','aosacsmS1']
cloud = ['30smplcmask1zwangM1','arsclwacr1kolliasM1','arsclwacrbnd1kolliasM1','mfrsrM1','mwr3cM1','mwrlosM1','mwrpM1','tsiskycoverM1','ceilM1',
         'radflux1longM1','tsicldmaskM1','mwrret1liljclouM1','arsclwacrrwp1fengM1','visstpxg13minnisX1','mfrsrcldod1minM1','ldquantsS10','microbasewM1']
atmo = ['aosmetS1','metM1','sondewnpnM1','pblhtsonde1mcfarlM1','interpolatedsondeM1','dlprofwstats4newsM1']

def instrumento():
    escolha0 = input('Escolha o conjunto de dados que irá analisar. Para gases digite 1, aerossois 2, nuvens 3 e estado atmosferico 4: ')
    if escolha0 == '4':
        escolha1 = input('Ok, ATMOSFERA. Agora escolha entre met, aosmet, feng, sonde, pblhsonde, interpolatedsonde ou dlnews: ')
        if escolha1 == 'met':
            freq = 1
            categoria = folder[2]
            instrumento = atmo[1]
            print(u'A única variavel no metM1 é org_precip_rate_mean.')
            var1 = 'org_precip_rate_mean'
            var1_unity = u'Optical Rain Gauge (ORG) precipitation rate mean (mm/hr)'
        elif escolha1 == 'aosmet':
            freq = 1/60
            categoria = folder[2]
            instrumento = atmo[0]
            escolha2 = input('Ok, AOSMET, mas qual variavel? Escolha "P", "T", "RH", "rain_amount" ou "rain_rate": ')
            if escolha2 == 'P':
                var1 = 'P_Ambient'
                var1_unity = 'Ambient pressure (hPa)'
            elif escolha2 == 'T':
                var1 = 'T_Ambient'
                var1_unity = u'Ambient air temperature (°C)'
            elif escolha2 == 'RH':
                var1 = 'RH_Ambient'
                var1_unity = 'Ambient air relative humidity (%)'
            elif escolha2 == 'rain_amount':
                var1 = 'rain_amount'
                var1_unity = 'Rain amount (mm/s)'
            elif escolha2 == 'rain_rate':
                var1 = 'rain_intensity'
                var1_unity = 'Rain intensity (mm/hr)'
        elif escolha1 == 'feng':
            freq = 0.5 
            categoria = folder[3]
            instrumento = cloud[12]
            escolha1_1 = input('Ok, FENG, mas qual variavel? Escolha "rairate_pwd", "rainrate_tippingbucket" ou "rainrate_disdrometer": ')
            if escolha1_1 == 'rainrate_pwd':
                var1 = 'rainrate_pwd'
                var1_unity = u'Rain intensity from PWD (mm/hr)'
            elif escolha1_1 == 'rainrate_tippingbucket':
                var1 = 'rainrate_tippingbucket'
                var1_unity = u'Rain intensity from tipping bucket (mm/hr)'
            elif escolha1_1 == 'rainrate_disdrometer':
                var1 = 'rainrate_disdrometer'
                var1_unity = u'Rain intensity from disdrometer (mm/hr)'
        elif escolha1 == 'sonde':
            freq = 1
            categoria = folder[2]
            instrumento = atmo[2]
            print(u'A única variavel no sondewnpnM1 é tdry.')
            var1 = 'tdry'
            var1_unity = u'Dry Bulb Temperature (°C)'
        elif escolha1 == 'pblhsonde':
            freq = 2/60
            categoria = folder[2]
            instrumento = atmo[3]
            escolha1_1 = input('Ok, pblhsonde, mas qual variavel? Escolha "heffter" ou "liuliang": ')
            if escolha1_1 == 'heffter':
                var1 = 'pbl_height_heffter'
                var1_unity = u'PBLH above mean sea level calculated using the Heffter (1980) method (m)'
            elif escolha1_1 == 'liuliang':
                var1 = 'pbl_height_liu_liang'
                var1_unity = u'PBLH above mean sea level calculated by Liu and Liang (2010) method (m)'
        elif escolha1 == 'interpolatedsonde':
            freq = 1
            categoria = folder[2]
            instrumento = atmo[4]
            escolha2 = input('Ok, INTERPOLATEDSONDE, mas qual variavel? Escolha "P", "T", "RH", "theta_superficie" ou "theta_700hPa": ')
            if escolha2 == 'P':
                var1 = 'bar_pres'
                var1_unity = 'Barometric pressure (kPa)'
            elif escolha2 == 'T':
                var1 = 'temp'
                var1_unity = u'Temperature (°C)'
            elif escolha2 == 'RH':
                var1 = 'rh'
                var1_unity = 'Relative humidity (%)'
            elif escolha2 == 'theta_superficie':
                var1 = 'theta_superficie'
                var1_unity = 'Potential temperature (K)'
            elif escolha2 == 'theta_700hPa':
                var1 = 'theta_700hPa'
                var1_unity = 'Potential temperature (K)'
        elif escolha1 == 'dlnews':
            freq = 10
            categoria = folder[2]
            instrumento = atmo[5]
            print(u'A única variavel no dlnews é cbw.')
            var1 = 'cbw'
            var1_unity = u'Median Doppler lidar cloud base vertical velocity (m/s)'
    elif escolha0 == '1':
        escolha1 = input('Ok, GASES. Agora escolha entre no, co ou o3: ')
        if escolha1 == 'no':
            freq = 1
            categoria = folder[0]
            instrumento = gas[0]
            escolha2 = input('Ok, NO. Escolha a variavel (no, noy ou nox): ')
            if escolha2 == 'no':
                var1 = 'no'
                var1_unity = 'NO volumetric concentration (ppbv)'
            elif escolha2 == 'nox':
                var1 = 'nox'
                var1_unity = 'NOx volumetric concentration (ppbv)'
            elif escolha2 == 'noy':
                var1 = 'noy'
                var1_unity = 'NOy volumetric concentration (ppbv)'
        elif escolha1 == 'co':
            freq = 1/60
            categoria = folder[0]
            instrumento = gas[1]
            escolha2 = input('Ok, CO. Escolha a variavel (co, co_dry, n2o ou n2o_dry): ')
            if escolha2 == 'co':
                var1 = 'co'
                var1_unity = 'CO mixing ratio (ppmv)'
            elif escolha2 == 'co_dry':
                var1 = 'co_dry'
                var1_unity = 'CO mixing ratio corrected for water vapor (ppmv)'
            elif escolha2 == 'n2o':
                var1 = 'n2o'
                var1_unity = 'N2O mixing ratio (ppmv)'
            elif escolha2 == 'n2o_dry':
                var1 = 'n2o_dry'
                var1_unity = 'N2O mixing ratio corrected for water vapor (ppmv)'
        elif escolha1 == 'o3':
            freq = 1/60
            categoria = folder[0]
            instrumento = gas[2]
            print(u'A única variável no maoaoso3S1.a1 é Ozone concentration (em ppbv).')
            var1 = 'o3'
            var1_unity = u'Ozone concentration (ppbv)'            
    elif escolha0 == '2':
        escolha1 = input('Ok, AEROSSOIS. Agora escolha entre aetalometro, smps, smpsb1, cpcf, cpc, nefelometro, psap, sp2, aipogren, uhsas, \
                         mfrsraod1mich, ccncol1b1, ccn100 ou acsm: ')
        if escolha1 == 'aetalometro':
            freq = 5
            categoria = folder[1]
            instrumento = aero[0]
            print(u'A única variavel no aetalometro é Equivalent BC concentration.')
            var1 = 'equivalent_black_carbon'
            var1_unity = u'Equivalent BC concentration (ng/m³)'
        elif escolha1 == 'smps':
            freq = 5
            categoria = folder[1]
            instrumento = aero[6]
            escolha1_1 = input('Ok, SMPS, mas qual variavel? Escolha "total_conc" ou "distribuicao_tamanho": ')
            if escolha1_1 == 'total_conc':
                var1 = 'total_concentration'
                var1_unity = u'Aerossol total concentration (count/cm³)'
            elif escolha1_1 == 'distribuicao_tamanho':
                var1 = 'number_size_distribution'
                var1_unity = u'Number size distribution - dN/dlogDp (count/cm³)'
        elif escolha1 == 'smpsb1':
            freq = 5
            categoria = folder[1]
            instrumento = aero[10]
            escolha1_1 = input('Ok, SMPSb1, mas qual variavel? Escolha "total_N_conc" ou "dN_dlogDp": ')
            if escolha1_1 == 'total_N_conc':
                var1 = 'total_N_conc'
                var1_unity = u'Aerossol total concentration (count/cm³)'
            elif escolha1_1 == 'dN_dlogDp':
                var1 = 'dN_dlogDp'
                var1_unity = u'Number size distribution - dN/dlogDp (count/cm³)'
        elif escolha1 == 'cpcf':
            freq = 1/60
            categoria = folder[1]
            instrumento = aero[1]
            print(u'A única variavel no cpcf é Particle concentration.')
            var1 = 'concentration'
            var1_unity = u'Particle concentration (1/cm³)'
        elif escolha1 == 'cpc':
            freq = 1/60
            categoria = folder[1]
            instrumento = aero[9]
            print(u'A única variavel no cpc é Particle concentration.')
            var1 = 'concentration'
            var1_unity = u'Particle concentration (1/cm³)'
        elif escolha1 == 'nefelometro':
            freq = 1
            escolha1_1 = input('Ok, NEFELOMETRO, mas qual? Escolha entre m1 e s1: ')
            if escolha1_1 == 'm1':
                categoria = folder[1]
                instrumento = aero[2]
                escolha2 = input('Ok, o m1. Agora escolha se quer PM2,5, PM10 ou no_impactor: ')
            else:
                categoria = folder[1]
                instrumento = aero[3]
                escolha2 = input('Ok, o s1. Agora escolha se quer PM2,5, PM10 ou no_impactor: ')
            if escolha2 == 'PM2,5':
                escolha3 = input('Ok, PM2,5. Escolha a variavel (bs450, bs550, bs700 ou bbs550): ')
                if escolha3 == 'bs450':
                    var1 = 'Bs_B_Dry_Neph3W'
                    var1_unity = u'Aerosol total light scattering coefficient at 450nm (Mm⁻¹)'
                if escolha3 == 'bs550':
                    var1 = 'Bs_G_Dry_Neph3W'
                    var1_unity = u'Aerosol total light scattering coefficient at 550nm (Mm⁻¹)'
                if escolha3 == 'bs700':
                    var1 = 'Bs_R_Dry_Neph3W'
                    var1_unity = u'Aerosol total light scattering coefficient at 700nm (Mm⁻¹)'
                if escolha3 == 'bbs550':
                    var1 = 'Bbs_G_Dry_Neph3W'
                    var1_unity = u'Aerosol back-hemispheric light scattering coefficient at 550nm (Mm⁻¹)'
            elif escolha2 == 'PM2,5':
                escolha3 = input('Ok, PM10. Escolha a variavel (bs450, bs550, bs700 ou bbs550): ')
                if escolha3 == 'bs450':
                    var1 = 'Bs_B_Dry_Neph3W'
                    var1_unity = u'Aerosol total light scattering coefficient at 450nm (Mm⁻¹)'
                if escolha3 == 'bs550':
                    var1 = 'Bs_G_Dry_Neph3W'
                    var1_unity = u'Aerosol total light scattering coefficient at 550nm (Mm⁻¹)'
                if escolha3 == 'bs700':
                    var1 = 'Bs_R_Dry_Neph3W'
                    var1_unity = u'Aerosol total light scattering coefficient at 700nm (Mm⁻¹)'
                if escolha3 == 'bbs550':
                    var1 = 'Bbs_G_Dry_Neph3W'
                    var1_unity = u'Aerosol back-hemispheric light scattering coefficient at 550nm (Mm⁻¹)'
            else:
                escolha3 = input('Ok, no_impactor. Escolha a variavel (bs450, bs550, bs700 ou bbs550): ')
                if escolha3 == 'bs450':
                    var1 = 'Bs_B_Dry_Neph3W'
                    var1_unity = u'Aerosol total light scattering coefficient at 450nm (Mm⁻¹)'
                if escolha3 == 'bs550':
                    var1 = 'Bs_G_Dry_Neph3W'
                    var1_unity = u'Aerosol total light scattering coefficient at 550nm (Mm⁻¹)'
                if escolha3 == 'bs700':
                    var1 = 'Bs_R_Dry_Neph3W'
                    var1_unity = u'Aerosol total light scattering coefficient at 700nm (Mm⁻¹)'
                if escolha3 == 'bbs550':
                    var1 = 'Bbs_G_Dry_Neph3W'
                    var1_unity = u'Aerosol back-hemispheric light scattering coefficient at 550nm (Mm⁻¹)'
        elif escolha1 == 'psap':
            freq = 1
            escolha1_1 = input('Ok, PSAP, mas qual? Escolha entre m1 e s1: ')
            if escolha1_1 == 'm1':
                categoria = folder[1]
                instrumento = aero[4]
                escolha2 = input('Ok, o m1. Agora escolha se quer PM2,5 ou PM10: ')
            else:
                categoria = folder[1]
                instrumento = aero[5]
                escolha2 = input('Ok, o s1. Agora escolha se quer PM2,5 ou PM10: ')
            if escolha2 == 'PM2,5':
                escolha3 = input('Ok, PM2,5. Escolha a variavel (ba470, ba522 ou ba660): ')
                if escolha3 == 'ba470':
                    var1 = 'Ba_B_Weiss'
                    var1_unity = u'Aerosol light absorption coefficient at 470nm (Mm⁻¹)'
                if escolha3 == 'ba522':
                    var1 = 'Ba_G_Weiss'
                    var1_unity = u'Aerosol light absorption coefficient at 522nm (Mm⁻¹)'
                if escolha3 == 'ba660':
                    var1 = 'Ba_R_Weiss'
                    var1_unity = u'Aerosol light absorption coefficient at 660nm (Mm⁻¹)'
            elif escolha2 == 'PM10':
                escolha3 = input('Ok, PM10. Escolha a variavel (ba470, ba522 ou ba660): ')
                if escolha3 == 'ba470':
                    var1 = 'Ba_B_Weiss'
                    var1_unity = u'Aerosol light absorption coefficient at 470nm (Mm⁻¹)'
                if escolha3 == 'ba522':
                    var1 = 'Ba_G_Weiss'
                    var1_unity = u'Aerosol light absorption coefficient at 522nm (Mm⁻¹)'
                if escolha3 == 'ba660':
                    var1 = 'Ba_R_Weiss'
                    var1_unity = u'Aerosol light absorption coefficient at 660nm (Mm⁻¹)'
        elif escolha1 == 'aipogren':
            freq = 1
            categoria = folder[1]
            instrumento = aero[11]
            escolha1_1 = input('Ok, AIPOGREN, mas qual variavel? Escolha "ba1um_g_psap3w", "bs1um_g_neph3w", "bbs1um_g_neph3w", "ssa1um_g", \
                               "hbsf1um_g", "bsangstromexponent1um_bg_neph3w", "ba10um_g_psap3w", "bs10um_g_neph3w", "bbs10um_g_neph3w" ou \
                               "bs1um_b_neph3w": ')
            if escolha1_1 == 'ba1um_g_psap3w':
                var1 = 'Ba_G_Dry_1um_PSAP3W_1'
                var1_unity = u'Absorption coefficient, green wavelength, 3 wavelength PSAP, low RH, 1 um size cut (1/Mm)'
            elif escolha1_1 == 'bs1um_g_neph3w':
                var1 = 'Bs_G_Dry_1um_Neph3W_1'
                var1_unity = u'Total scattering coefficient, green wavelength, low RH, 1 um size cut (1/Mm)'
            elif escolha1_1 == 'bbs1um_g_neph3w':
                var1 = 'Bbs_G_Dry_1um_Neph3W_1'
                var1_unity = u'Back-scattering coefficient, green wavelength, low RH, 1 um size cut (1/Mm)'
            elif escolha1_1 == 'ssa1um_g':
                var1 = 'ssa_G_Dry_1um'
                var1_unity = u'Single scattering albedo, green wavelength, low RH, 1 um size cut (unitless)'
            elif escolha1_1 == 'hbsf1um_g':
                var1 = 'bsf_G_Dry_1um'
                var1_unity = u'Hemispheric backscatter fraction, green wavelength, 1 um size cut (unitless)'
            elif escolha1_1 == 'bsangstromexponent1um_bg_neph3w':
                var1 = 'Bs_angstrom_exponent_BG_Dry_1um'
                var1_unity = u'Angstrom exponent computed from blue/green ratio, 1 um size cut, Neph3W total scatter data (unitless)'
            elif escolha1_1 == 'ba10um_g_psap3w':
                var1 = 'Ba_G_Dry_10um_PSAP3W_1'
                var1_unity = u'Absorption coefficient, green wavelength, 3 wavelength PSAP, low RH, 10 um size cut (1/Mm)'
            elif escolha1_1 == 'bs10um_g_neph3w':
                var1 = 'Bs_G_Dry_10um_Neph3W_1'
                var1_unity = u'Total scattering coefficient, green wavelength, low RH, 10 um size cut (1/Mm)'
            elif escolha1_1 == 'bbs10um_g_neph3w':
                var1 = 'Bbs_G_Dry_10um_Neph3W_1'
                var1_unity = u'Back-scattering coefficient, green wavelength, low RH, 10 um size cut (1/Mm)'
            elif escolha1_1 == 'bs1um_b_neph3w':
                var1 = 'Bs_B_Dry_1um_Neph3W_1'
                var1_unity = u'Total scattering coefficient, blue wavelength, low RH, 1 um size cut (1/Mm)'
        elif escolha1 == 'sp2':
            freq = 1 
            categoria = folder[1]
            instrumento = aero[7]
            print(u'A única variavel no sp2 é Refractory BC concentration.')
            var1 = 'rBC'
            var1_unity = u'Refractory BC concentration (ng/m³)'
        elif escolha1 == 'uhsas':
            freq = 1/6
            categoria = folder[1]
            instrumento = aero[12]
            escolha1_1 = input('Ok, uhsas, mas qual variavel? Escolha "udN_dlogDp", "utotal_N_conc", "total_SA_conc" ou "total_V_conc": ')
            if escolha1_1 == 'utotal_N_conc':
                var1 = 'utotal_N_conc'
                var1_unity = u'Aerossol total number concentration from integrated size distribution (count/cm³)'
            elif escolha1_1 == 'udN_dlogDp':
                var1 = 'udN_dlogDp'
                var1_unity = u'Number size distribution, optical scattering diameter at 1054 nm - dN/dlogDp (count/cm³)'
            elif escolha1_1 == 'total_SA_conc':
                var1 = 'total_SA_conc'
                var1_unity = u'Total surface area concentration from integrated size distribution (nm²/cm³)'
            elif escolha1_1 == 'total_V_conc':
                var1 = 'total_V_conc'
                var1_unity = u'Total volume concentration from integrated size distribution (nm³/cm³)'
        elif escolha1 == 'mfrsraod1mich':
            freq = 1/3
            categoria = folder[1]
            instrumento = aero[13]
            escolha1_1 = input('Ok, aod, mas qual variavel? Escolha "aod1_415", "aod2_500", "aod3_615", "aod4_673" ou "aod5_870": ')
            if escolha1_1 == 'aod1_415':
                var1 = 'aerosol_optical_depth_filter1'
                var1_unity = u'aerosol optical depth filter 1 (unitless)'
            elif escolha1_1 == 'aod2_500':
                var1 = 'aerosol_optical_depth_filter2'
                var1_unity = u'aerosol optical depth filter 2 (unitless)'
            elif escolha1_1 == 'aod3_615':
                var1 = 'aerosol_optical_depth_filter3'
                var1_unity = u'aerosol optical depth filter 3 (unitless)'
            elif escolha1_1 == 'aod4_673':
                var1 = 'aerosol_optical_depth_filter4'
                var1_unity = u'aerosol optical depth filter 4 (unitless)'
            elif escolha1_1 == 'aod5_870':
                var1 = 'aerosol_optical_depth_filter5'
                var1_unity = u'aerosol optical depth filter 5 (unitless)'
        elif escolha1 == 'ccncol1b1':
            freq = 1
            categoria = folder[1]
            instrumento = aero[14]
            print(u'A única variavel no ccncol1b1 é Number concentration of CCN.')
            var1 = 'N_CCN'
            var1_unity = u'Number concentration of CCN (1/cm³)'
        elif escolha1 == 'ccn100':
            freq = 1
            categoria = folder[1]
            instrumento = aero[15]
            print(u'A única variavel é Number concentration of CCN.')
            var1 = 'N_CCN'
            var1_unity = u'AOS number concentration of CCN (1/cm³)'
        elif escolha1 == 'acsm':
            freq = 1/60
            categoria = folder[1]
            instrumento = aero[16]
            print(u'A única variavel é total organics.')
            var1 = 'total_organics'
            var1_unity = 'Mass concentration of total organics, ambient aerosol in air (ug/m³)'
    elif escolha0 == '3':
        escolha1 = input('Ok, NUVENS. Escolha entre mwr3c, mwrlos, mwrp, mwrretrievals, radflux, ceil, WACR1, WACRBND1, mplwang, tsiskycover, \
                          feng, mfrsr_cod, goes, ldquants ou microbase: ')
        if escolha1 == 'mwr3c':
            freq = 0.206244629
            categoria = folder[3]
            instrumento = cloud[4]
            escolha1_1 = input('Ok, MWR3C, mas qual variavel? Escolha "lwp" ou "pwv": ')
            if escolha1_1 == 'lwp':
                var1 = 'lwp'
                var1_unity = u'Liquid Water Path (mm)'
            elif escolha1_1 == 'pwv':
                var1 = 'pwv'
                var1_unity = u'Precipitable Water Vapor (cm)'
            #print(u'A única variavel no mwr3c é lwp.')
            #var1 = 'lwp'
            #var1_unity = u'mm'
        elif escolha1 == 'mwrlos':
            freq = 1/3 # Equivale a 20 segundos, pois 20/60=1/3
            categoria = folder[3]
            instrumento = cloud[5]
            print(u'A única variavel no mwrlos é "liq" (lwp).')
            var1 = 'liq'
            var1_unity = u'cm'
        elif escolha1 == 'mwrp':
            freq = 1.0065 
            categoria = folder[3]
            instrumento = cloud[6]
            escolha1_1 = input('Ok, MWRProfiler, mas qual variavel? Escolha "lwp", "aguaprecipitavel", "cape", "cbh" ou "LCL": ')
            if escolha1_1 == 'lwp':
                var1 = 'liquidWaterPath'
                var1_unity = u'Liquid Water Path (mm)'
            elif escolha1_1 == 'aguaprecipitavel':
                var1 = 'totalPrecipitableWater'
                var1_unity = u'Retrieved total precipitable water vapor (cm)'
            elif escolha1_1 == 'cape':
                var1 = 'cape'
                var1_unity = u'Convective available potential energy (J/Kg)'
            elif escolha1_1 == 'cbh':
                var1 = 'cloudBaseHeight'
                var1_unity = u'Derived Cloud Base Height (m)'
            elif escolha1_1 == 'LCL':
                var1 = 'liftingCondensationLevel'
                var1_unity = u'Lifting condensation level (m)'    
            #print(u'A única variavel no mwrp é "liquidWaterPath" (lwp).')
            #var1 = 'liquidWaterPath'
            #var1_unity = u'mm'
        elif escolha1 == 'mwrretrievals':
            freq = 1/3 # Equivale a 20 segundos, pois 20/60=1/3 
            categoria = folder[3]
            instrumento = cloud[11]
            escolha1_1 = input('Ok, MWR Retrievals, mas qual variavel? Escolha "lwp" ou "pwv": ')
            if escolha1_1 == 'lwp':
                var1 = 'be_lwp'
                var1_unity = u'Liquid water path best-estimate value (g/m²)'
            elif escolha1_1 == 'pwv':
                var1 = 'be_pwv'
                var1_unity = u'Precipitable water vapor best-estimate value (cm)'    
        elif escolha1 == 'radflux':
            freq = 1 
            categoria = folder[3]
            instrumento = cloud[9]
            escolha1_1 = input('Ok, RADFLUX, mas qual variavel? Escolha "COD_visivel", "cf", "down_sw", "clear_sky_dsw" \
                               "up_sw", "cloud_transmissivity_sw", "direct_down_sw" ou "costheta": ')
            if escolha1_1 == 'COD_visivel':
                var1 = 'visible_cloud_optical_depth'
                var1_unity = u'Estimated effective visible cloud optical depth (unitless)'
            elif escolha1_1 == 'cloud_transmissivity_sw':
                var1 = 'cloud_transmissivity_shortwave'
                var1_unity = u'Shortwave cloud transmissivity (unitless)'
            elif escolha1_1 == 'direct_down_sw':
                var1 = 'direct_downwelling_shortwave'
                var1_unity = u'Measured direct downwelling shortwave irradiance (W/m²)'
            elif escolha1_1 == 'cf':
                var1 = 'cloudfraction_shortwave'
                var1_unity = 'Estimated shortwave fractional sky cover'
            elif escolha1_1 == 'down_sw':
                var1 = 'downwelling_shortwave'
                var1_unity = 'Broadband all-sky Downwelling shortwave irradiance (W/m²)'
            elif escolha1_1 == 'clear_sky_dsw':
                var1 = 'clearsky_downwelling_shortwave'
                var1_unity = 'Broadband clear-sky Downwelling shortwave irradiance (W/m²)'
            elif escolha1_1 == 'up_sw':
                var1 = 'upwelling_shortwave'
                var1_unity = 'Broadband all-sky Upwelling shortwave irradiance (W/m²)'
            elif escolha1_1 == 'costheta':
                var1 = 'cosine_zenith'
                var1_unity = 'Cosine of solar zenith angle (unitless)'
            #print(u'A única variavel no radflux é "visible_cloud_optical_depth" (COD).')
            #var1 = 'visible_cloud_optical_depth'
            #var1_unity = u'unitless'
        elif escolha1 == 'ceil':
            freq = 4/15 # Equivale a 16 segundos, pois 16/60=8/30=4/15
            categoria = folder[3]
            instrumento = cloud[8]
            escolha1_1 = input('Ok, Ceilometro, mas qual variavel? Escolha "firstCBH", "secondCBH" ou "thirdCBH": ')
            if escolha1_1 == 'firstCBH':
                var1 = 'first_cbh'
                var1_unity = u'First Cloud Base Height (m)'
            elif escolha1_1 == 'secondCBH':
                var1 = 'second_cbh'
                var1_unity = u'Second Cloud Base Height (m)'
            elif escolha1_1 == 'thirdCBH':
                var1 = 'third_cbh'
                var1_unity = u'Third Cloud Base Height (m)'
            #print(u'A única variavel no ceilometro é "first_cbh" (CBH).')
            #var1 = 'first_cbh'
            #var1_unity = u'm'
        elif escolha1 == 'mplwang':
            freq = 0.5
            categoria = folder[3]
            instrumento = cloud[0]
            escolha1_1 = input('Ok, MPL_Wang, mas qual variavel? Escolha "CBH" ou "cloud_top": ')
            if escolha1_1 == 'CBH':
                var1 = 'cloud_base'
                var1_unity = u'Lowest cloud base height above ground level (km)'
            elif escolha1_1 == 'cloud_top':
                var1 = 'cloud_top'
                var1_unity = u'Highest cloud top height above ground level (km)'
            #elif escolha1_1 == 'cloud_location':
            #    var1 = 'cloud_mask'
            #    var1_unity = u'Cloud Location'
        elif escolha1 == 'WACR1':
            freq = 5/60
            categoria = folder[3]
            instrumento = cloud[1]
            print(u'A única variavel no WACR1 é CBH.')
            var1 = 'cloud_base_best_estimate'
            var1_unity = u'Best estimate of CBH from ceilometer and MPL (m)'
        elif escolha1 == 'ldquants':
            freq = 1
            categoria = folder[3]
            instrumento = cloud[15]
            print(u'A única variavel no ldquants é lwc.')
            var1 = 'lwc'
            var1_unity = u'Liquid Water Content (g/m³)'
        elif escolha1 == 'microbase':
            freq = 5/60
            categoria = folder[3]
            instrumento = cloud[16]
            print(u'A única variavel no microbase é liquid_water_content.')
            var1 = 'liquid_water_content'
            var1_unity = u'Retrieved Liquid Water Concentration (g/m³)'
        elif escolha1 == 'WACRBND1':
            freq = 5/60
            categoria = folder[3]
            instrumento = cloud[2]
            escolha1_1 = input('Ok, WACRBND1, mas qual variavel? Escolha "CBH_ceil_mpl", "CBH_radar_mpl", "CTH_radar" ou "CTH_radar_mpl": ')
            if escolha1_1 == 'CBH_ceil_mpl':
                var1 = 'cloud_base_best_estimate'
                var1_unity = u'Best estimate of CBH from ceilometer and MPL (m)'
            elif escolha1_1 == 'CBH_radar_mpl':
                var1 = 'cloud_layer_base_height'
                var1_unity = u'Time series of 95GHz-radar/MPL CBH for up to 10 cloud layers (m)'
            elif escolha1_1 == 'CTH':
                var1 = 'radar_first_top'
                var1_unity = u'First detected cloud top by the 95GHz radar (m)'
            elif escolha1_1 == 'CTH_radar_mpl':
                var1 = 'cloud_layer_top_height'
                var1_unity = u'Time series of 95GHz-radar/MPL cloud top height for up to 10 cloud layers (m)'
        elif escolha1 == 'tsiskycover':
            freq = 0.5 
            categoria = folder[3]
            instrumento = cloud[7]
            escolha1_1 = input('Ok, TSISKYCOVER, mas qual variavel? Escolha "percent_opaque", "percent_thin" ou "sunny": ')
            if escolha1_1 == 'percent_opaque':
                var1 = 'percent_opaque'
                var1_unity = u'Percent opaque cloud (%)'
            elif escolha1_1 == 'percent_thin':
                var1 = 'percent_thin'
                var1_unity = u'Percent thin cloud (%)'
            elif escolha1_1 == 'sunny':
                var1 = 'sunny'
                var1_unity = u'Sunshine meter (unitless)'
        elif escolha1 == 'feng':
            freq = 0.5 
            categoria = folder[3]
            instrumento = cloud[12]
            escolha1_1 = input('Ok, FENG, mas qual variavel? Escolha "best_CBH", "CLBH", "rairate_pwd", "rainrate_tippingbucket" \
                               "rainrate_disdrometer", "p", "t", "rh", "radar_first_CTH", "CLTH", "lwp" ou "Z": ')
            if escolha1_1 == 'best_CBH':
                var1 = 'cloud_base_best_estimate'
                var1_unity = u'Best estimate of cloud base from ceilometer and MPL (km)'
            elif escolha1_1 == 'CLBH':
                var1 = 'cloud_layer_base_height_WACR'
                var1_unity = u'Time series of 95GHz-radar/MPL cloud base height for up to 10 cloud layers (km)'
            elif escolha1_1 == 'radar_first_CTH':
                var1 = 'radar_first_top_WACR'
                var1_unity = u'First detected cloud top by WACR (km)'
            elif escolha1_1 == 'CLTH':
                var1 = 'cloud_layer_top_height_WACR'
                var1_unity = u'Time series of 95GHz-radar/MPL cloud top height for up to 10 cloud layers (km)'
            elif escolha1_1 == 'rainrate_pwd':
                var1 = 'rainrate_pwd'
                var1_unity = u'Rain intensity from PWD (mm/hr)'
            elif escolha1_1 == 'rainrate_tippingbucket':
                var1 = 'rainrate_tippingbucket'
                var1_unity = u'Rain intensity from tipping bucket (mm/hr)'
            elif escolha1_1 == 'rainrate_disdrometer':
                var1 = 'rainrate_disdrometer'
                var1_unity = u'Rain intensity from disdrometer (mm/hr)'
            elif escolha1_1 == 'p':
                var1 = 'pressure'
                var1_unity = u'Barometric pressure (kPa)'
            elif escolha1_1 == 't':
                var1 = 'temperature'
                var1_unity = u'Temperature (°C)'
            elif escolha1_1 == 'rh':
                var1 = 'rh'
                var1_unity = u'Relative humidity (%)'
            elif escolha1_1 == 'lwp':
                var1 = 'lwp'
                var1_unity = u'Liquid water path from MWRRET (g/m²)'
            elif escolha1_1 == 'Z':
                var1 = 'reflectivity_WACR'
                var1_unity = u'WACR equivalent reflectivity factor (dBZ)'
        elif escolha1 == 'goes':
            freq = 30
            categoria = folder[3]
            instrumento = cloud[13]
            escolha1_1 = input('Ok, Goes, mas qual variavel? Escolha "cod", "lwp" ou "reff": ')
            if escolha1_1 == 'cod':
                var1 = 'visible_optical_depth'
                var1_unity = u'Cloud optical depth'
            elif escolha1_1 == 'lwp':
                var1 = 'liquid_water_path'
                var1_unity = u'Liquid water path (g/m²)'
            elif escolha1_1 == 'reff':
                var1 = 'particle_size'
                var1_unity = u'Effective particle radius (micrometers)'
        elif escolha1 == 'mfrsr_cod':
            freq = 1/3 # Equivale a 20 segundos, pois 20/60=1/3 
            categoria = folder[3]
            instrumento = cloud[14]
            escolha1_1 = input('Ok, mfrsr_cld, mas qual variavel? Escolha "cod" ou "reff": ')
            #print(u'A única variavel é COD.')
            if escolha1_1 == 'cod':
                var1 = 'optical_depth_instantaneous'
                var1_unity = u'Cloud Optical Depth (Instantaneous)'
            elif escolha1_1 == 'reff':
                var1 = 'effective_radius_instantaneous'
                var1_unity = 'Unitless'
    
    ## Setando o path, o path_nc e o pasta_dfs:
    if categoria=='Gases' or categoria=='Aerossois' or categoria=='Estado_Atmosferico':
        path = os.path.expanduser(rootD+categoria+'/mao'+instrumento)
        #path = os.path.expanduser(rootD+categoria+'/mao'+instrumento+'_status_filtered')
        pasta_dfs = rootD+categoria+'/Dataframes/'
        if instrumento=='aossmpsS1' or instrumento=='aosnephdryM1_Glauber' or instrumento=='aosnoxS1' or instrumento=='aoscoS1' or instrumento=='aosmetS1' or instrumento=='metM1' or instrumento=='sondewnpnM1' or instrumento=='pblhtsonde1mcfarlM1' or instrumento=='aip1ogrenM1' or instrumento=='aosmfrsraod1michM1' or instrumento=='aosacsmS1':
            path_nc = sorted(glob.glob(rootD+categoria+'/mao'+instrumento+'/*.cdf'))            
            #path_nc = sorted(glob.glob(rootD+categoria+'/mao'+instrumento+'_status_filtered'+'/*.cdf'))
        else:
            path_nc = sorted(glob.glob(rootD+categoria+'/mao'+instrumento+'/*.nc'))
            #path_nc = sorted(glob.glob(rootD+categoria+'/mao'+instrumento+'_status_filtered'+'/*.nc'))
    elif categoria=='Nuvens':
        path = os.path.expanduser(rootS+categoria+'/mao'+instrumento)
        pasta_dfs = rootS+categoria+'/Dataframes/'
        if instrumento=='ceilM1' or instrumento=='radflux1longM1' or instrumento=='ldquantsS10' or instrumento=='microbasewM1':
            path_nc = sorted(glob.glob(rootS+categoria+'/mao'+instrumento+'/*.nc'))
        else:
            path_nc = sorted(glob.glob(rootS+categoria+'/mao'+instrumento+'/*.cdf'))
        
    ## Colocando todos os outputs de interesse em um dicionario e o retornando:    
    if escolha1 == 'nefelometro' or escolha1 == 'psap':
        outputs = {'Caminho_instrumento': path, 'Lista_netcdfs': path_nc, 'Instrumento': instrumento,
                   'Frequencia': freq, 'Caminho_para_dataframes': pasta_dfs, 
                   'Variavel': var1, 'Unidade': var1_unity, 'Corte': escolha2}
    else:
        outputs = {'Caminho_instrumento': path, 'Lista_netcdfs': path_nc, 'Instrumento': instrumento,
                   'Frequencia': freq, 'Caminho_para_dataframes': pasta_dfs, 
                   'Variavel': var1, 'Unidade': var1_unity}
    return  outputs