#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 15:42:57 2019

@author: StOnEChAn
"""
import random
import time
import pandas as pd
import numpy as np


researcher_names = ['Cindy Shaheen', 'Daniel Berard', 'Francis Stabile', 'Kim Metera',
                    'Radin Tahvildari', 'Sabrina Leslie']

researchassist_names = ['Stone Chen', 'Wendy Ji',
                        'Zach Friedenberger', 'Zhi Zhang'  ]

analysisType = ['rough', 'decent', 'accurate']

status = ['active', 'inactive']

microscope = ['Nikon01','Nikon02']

#generate random date
def random_dates(start, end):
    start_u = start.value//10**9
    end_u = end.value//10**9
    return pd.to_datetime(np.random.randint(start_u, end_u), unit='s')


text_file = open("autoDataGen.sql", "w")
start = pd.to_datetime('2018-05-01')
end = pd.to_datetime('2019-02-27')

for i in range(200):
    
    # protocol: id, path, name
    rand_num = random.randint(0,(len(researcher_names)-1))
    
    text_file.write("INSERT INTO protocol VALUES(%d, 'C:\\Protocol\%s.pdf', '%s');\n" % (i+1, str(i+1), researcher_names[rand_num]))

for i in range(200):
    # CLiC raw data: id, dates in the format of "xxxx-xx-xx", path
    text_file.write("INSERT INTO CliCRawData VALUES(%d,'%s', 'C:\\CliCRawData\%s.mat');\n" %(i+1, random_dates(start, end).strftime('%Y-%m-%d'), str(i+1)))

for i in range(200):
    # NanoparticleData: id
    text_file.write("INSERT INTO NanoparticleData VALUES(%d);\n" %(i+1));

for i in range(200):
    # DNAUnwindingData:id
    text_file.write("INSERT INTO DNAUnwindingData VALUES(%d);\n" %(i+1));

for i in range(200):
    # NanoparticleAnalysisResults: id, dates, paths, avgRadius, crid, name
    rand_num_ra = random.randint(0, len(researchassist_names)-1)
    text_file.write("INSERT INTO NanoparticleAnalysisResults VALUES(%d, '%s', 'C:\\NanoparticleAnalysisResults\%s', %6.2f, %d, '%s');\n" % (i, random_dates(start, end).strftime('%Y-%m-%d'), str(i+1), random.uniform(20, 50), random.randint(1, 200), researchassist_names[rand_num_ra]))

for i in range(200):
    # BindingAnalysisResults: id, dates, paths, analysisType, crid, name
    rand_num_ra = random.randint(0, len(researchassist_names)-1)
    text_file.write("INSERT INTO BindingAnalysisResults VALUES(%d, '%s', 'C:\\BindingAnalysisResults\%s', '%s', %d, '%s');\n" %(i+1, random_dates(start, end).strftime('%Y-%m-%d'), str(i+1), analysisType[random.randint(0, len(analysisType)-1)], random.randint(1, 200), researchassist_names[rand_num_ra]))

for i in range(200):
    # CLiCDashBoard: id, dates, paths, focus, SNR, contaminants, crid, name
    rand_num_ra = random.randint(0, len(researchassist_names)-1)
    text_file.write("INSERT INTO CLiCDashBoard VALUES(%d, '%s', 'C:\\CLiCDashBoard\%s', %5.2f, %6.2f, %8.2f, %d, '%s');\n" %(i+1, random_dates(start, end).strftime('%Y-%m-%d'), str(i+1), random.uniform(1,5), random.uniform(1,10), random.randint(100, 5000), random.randint(1, 200), researchassist_names[rand_num_ra]))

for i in range(200):
    # experiment: protocolid, trynumber, microscopeid, crid, name
    rand_num = random.randint(0,(len(researcher_names)-1))
    tryRange = random.randint(1, 5)
    for j in range(1, tryRange):
        text_file.write("INSERT INTO Experiment VALUES(%d, %d, '%s', %d, '%s');\n" %(i+1, j, microscope[random.randint(0,1)], random.randint(1, 200), researcher_names[rand_num]))





text_file.close();

