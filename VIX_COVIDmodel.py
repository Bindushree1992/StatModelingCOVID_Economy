# -*- coding: utf-8 -*-
"""
Created on Sat June 26 

@author: Bindushree
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

datadir     = 'D:/BINDUMS/Thesis/COVID-19-master/csse_covid_19_data/csse_covid_19_time_series/'
dataout     = 'D:/BINDUMS/Thesis/'
dataf       = pd.read_csv(datadir+'time_series_covid19_confirmed_global.csv')
#delete France and UK Province rows
dataf.drop([109,110,111,112,113,114,115,116,117,219,220,221,222,223,224])
countrytop5 = ['US','Brazil','Russia','Spain','United Kingdom','France']
npop        = [330838184,212430396,145929337,46753295,67855909,65261548]
START_DATE  = {'US': '1/22/20',
               'Brazil': '2/26/20',
               'Russia':'1/31/20',
               'Spain': '2/1/20',
               'United Kingdom':'1/31/20',
               'France':'1/24/20'}

#define function --statistical fit using generalized logistic model
def func(t,a,b,c):
    return c/(1+np.exp(-(t-b)/a))
