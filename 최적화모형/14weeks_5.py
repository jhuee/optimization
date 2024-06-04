#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 18:55:13 2024

@author: juhee
"""

from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver("SAT")

DIST= [
    [0,10,12,5,17,9,13,7,0],
    [10,0,9,20,8,11,3,5,0],
    [12,9,0,14,4,10,1,16,0],
    [5,20,14,0,20,5,28,10,0],
    [17,8,4,20,0,21,4,9,0],
    [9,11,10,5,21,0,2,3,0],
    [13,3,1,28,4,2,0,2,0],
    [7,5,16,10,9,3,2,0,0],
    [0,0,0,0,0,0,0,0,0]
    ]
nCity = len(DIST)

X = {}
for i in range(nCity):
    for j in range(nCity):
        if i != j:
            X[i,j] = solver.IntVar(0, 1, "X" + str(i)+str(j))
            
U = {}
for i in range(1, nCity):
    U[i] = solver.IntVar(1, nCity-1, "U[%i]"%i)
    
# 도시 j로 한 번ㄷ은 들어와야 함
for j in range(nCity):
    solver.Add(solver.Sum([X[i, j] for i in range (nCity) if i != j]) == 1, 'in_' +str(i))
    
# 도시 j로 한 번은 나가야함
for i in range(nCity):
    solver.Add(solver.Sum([X[i, j] for j in range (nCity) if i != j]) == 1, 'out_' +str(i))

# 방문 제약
for i in range(1,nCity):
    for j in range(1, nCity):
        if i != j:
            solver.Add(U[i] - U[j] + 1 - (nCity-1)*(1-X[i,j])<= 0, 'U_'+str(i) + str(j))
             
objective_terms = []
for i in range(nCity) :
    for j in range(nCity):
        if i != j:
            objective_terms.append(DIST[i][j] *X[i,j])

solver.Minimize(solver.Sum(objective_terms))

#3 5 7 1 6 2 4 8
if 1:
    with open('or9-1.lp', "w") as out_f:
        lp_text = solver.ExportModelAsLpFormat(False)
        out_f.write(lp_text)
status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE :
    print(f"Total cost = {solver.Objective().Value():.1f}\n",)
    for i in range(nCity):
        for j in range(nCity):
            if i != j :
                if X[i,j].solution_value() > 0.5 :
                    print(f"X{i} --> X{j}")
    for i in range(1, nCity):
        print(f"회원{i} 방문 순서: ", U[i].solution_value())
else :
    print("No solution found")