#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 18:44:46 2024

@author: juhee
"""

from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver("SAT")
DIST = [
        [0,20,15,19,24,14,21,11],
        [20,0,18,22,23,22,9,10],
        [15,18,0,11,21,14,32,12],
        [19,22,11,0,20,27,18,15],
        [24,23,21,20,0,14,25,20],
        [14,22,14,27,14,0,26,17],
        [21,9,32,18,25,26,0,20],
        [11,10,12,15,20,17,20,0]
        ]
nVisit=8
X = {}
for i in range(nVisit):
    for j in range(nVisit):
        if i != j:
            X[i,j] = solver.IntVar(0, 1, "X" + str(i)+str(j))
            
U = {}
for i in range(1, nVisit):
    U[i] = solver.IntVar(1, nVisit-1, "U[%i]"%i)
    
# 도시 j로 한 번ㄷ은 들어와야 함
for j in range(nVisit):
    solver.Add(solver.Sum([X[i, j] for i in range (nVisit) if i != j]) == 1, 'in_' +str(i))
    
# 도시 j로 한 번은 나가야함
for i in range(nVisit):
    solver.Add(solver.Sum([X[i, j] for j in range (nVisit) if i != j]) == 1, 'out_' +str(i))

# 방문 제약
for i in range(1,nVisit):
    for j in range(1, nVisit):
        if i != j:
            solver.Add(U[i] - U[j] + 1 - (nVisit-1)*(1-X[i,j])<= 0, 'U_'+str(i) + str(j))
            
solver.Add(U[2] <= 2)
solver.Add(U[3] <= 2)
solver.Add(X[2,6] == 1)
# solver.Add(U[2] +1 == U[6])             
objective_terms = []
for i in range(nVisit) :
    for j in range(nVisit):
        if i != j:
            objective_terms.append(DIST[i][j] *X[i,j])

solver.Minimize(solver.Sum(objective_terms))


if 1:
    with open('or9-1.lp', "w") as out_f:
        lp_text = solver.ExportModelAsLpFormat(False)
        out_f.write(lp_text)
status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE :
    print(f"Total cost = {solver.Objective().Value():.1f}\n",)
    for i in range(nVisit):
        for j in range(nVisit):
            if i != j :
                if X[i,j].solution_value() > 0.5 :
                    print(f"X{i} --> X{j}")
    for i in range(1, nVisit):
        print(f"{i}고객 방문 순서: ", U[i].solution_value())
else :
    print("No solution found")