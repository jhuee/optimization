#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 17:50:07 2024

@author: juhee
"""

from ortools.linear_solver import pywraplp
import pandas as pd
solver = pywraplp.Solver.CreateSolver("SAT")

# DIST = [
#         [0,702, 454,842,2396,1196],
#         [702,0,324,1093, 2136, 764],
#         [454,324,0,1137,2180,798],
#         [842, 1093, 1137, 0, 1616, 1857],
#         [2396, 2136, 2180,1616,0,2900],
#         [1196, 764, 798,1857, 2900,0]
#         ]


df= pd.read_excel('./tsp_ex_data1.xlsx', index_col = 'Unnamed:0')
DIST = df.values.tolist()
nCity = len(DIST)

X = {}
for i in range(nCity):
    for j in range(nCity):
        if i != j:
            X[i,j] = solver.IntVar(0, 1, "X" + str(i)+str(j))
            
U = {}
for i in range(1, nCity):
    U[i] = solver.NumVar(1, nCity-1, "U[%i]"%i)
    
# 도시 j로 한 번ㄷ은 들어와야 함
for j in range(nCity):
    solver.Add(solver.Sum([X[i, j] for i in range (nCity) if i != j]) == 1, 'in_' +str(i))
    
# 도시 j로 한 번은 나가야함
for i in range(nCity):
    solver.Add(solver.Sum([X[i, j] for j in range (nCity) if i != j]) == 1, 'out_' +str(i))

# 방문 제약
for i in range(1,nCity):
    if j in range(1, nCity):
        if i != j:
            solver.Add(U[i] - U[j] + nCity*X[i,j] - (nCity-1)<= 0, 'U_'+str(i) + str(j))
             
objective_terms = []
for i in range(nCity) :
    for j in range(nCity):
        if i != j:
            objective_terms.append(DIST[i][j] *X[i,j])

solver.Minimize(solver.Sum(objective_terms))


status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE :
    print(f"Total cost = {solver.Objective().Value():.1f}\n",)
    for i in range(nCity):
        for j in range(nCity):
            if i != j :
                if X[i,j].solution_value() > 0.5 :
                    print(f"X{i} --> X{j}")
    for i in range(1, nCity):
        print(f"{i}도시 방문 순서: ", U[i].solution_value())
else :
    print("No solution found")