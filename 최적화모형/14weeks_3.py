#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 18:07:21 2024

@author: juhee
"""

import pandas as pd
from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver("SAT")

import math

def calDist(x1,y1,x2,y2) :
    dist= math.sqrt((x1-x2)**2 +(y1-y1)**2)
    return dist

def makeDist(nP):
    DIST = list()
    nCity = len(nP)
    
    for i in range(nCity):
        DIST.append([])
        for j in range(nCity):
            if j != i :
                temp = calDist(nP['xc'][i], nP['yc'][i], nP['xc'][j], nP['yc'][j])
                DIST[i].append(temp)
            else :
                DIST[i].append(0)
    return DIST

nPos = pd.DataFrame(columns=['xc','yc'])

f = open("./TSP_data\boys29.tsp", "r")

flag = 0

while True :
    line = f.readLine().strip()
    if not line: break
    
    if line == "DISPLAY_DATA_SECTION":
        flag = 1
        continue
    
    if line == "EOF":
        continue
    
    if flag :
        ss = line.split()
        nPos.loc[len(nPos)] = [float(ss[1]), float((ss[2]))]
        
DIST = makeDist(nPos)
final_sol = []

print(DIST)

f.close()

                                                   
        

                                    