#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 18:47:36 2024

@author: juhee
"""

from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver("SAT")
BIGM = 100000
COST = [
        [50, 55, 42, 57, 48, 52],
        [66,70, BIGM, 68, 75, 63],
        [81, 78, 72, 80,85, 78],
        [40, 42, 38, 45, 46, 42],
        [62,55, 58, 60, 56, 65],
        [0,0,0,0,0,0]]

DEMANDS = [1,1,1,1,1,1]
SUPPLIES = [1,1,1,1,1,1]

nW = len(COST)
nC = len(COST[0])

#의사결정변수
X = {}
for i in range(nW):
    for j in range(nC):
        X[i, j] = solver.NumVar(0, solver.infinity(), "X"+str(i)+str(j))
    
    
#제약조건
# 제약조건: 각 도시 수요는 만족되어야 한다.

for j in range(nC):

    solver.Add(solver.Sum([X[i, j] for i in range(nW)]) == DEMANDS[j], 'demands_'+str(i))



# 제약조건: 각 창고의 공급량은 최대 공급량을 초과할 수 없다.

for i in range(nW):

    solver.Add(solver.Sum([X[i, j] for j in range(nC)]) == SUPPLIES[i], 'out_'+str(i))



# Objective

objective_terms = []

for i in range(nW):

    for j in range(nC):

        objective_terms.append(COST[i][j] * X[i, j])
        

solver.Minimize(solver.Sum(objective_terms))



if 1:

    with open('or11-1.lp', "w") as out_f:

        lp_text = solver.ExportModelAsLpFormat(False)

        out_f.write(lp_text)



# Solve

status = solver.Solve()



# Print solution.

if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:

    print(f"Total cost = {solver.Objective().Value():.1f}\n", )

    for i in range(nW):

        for j in range(nC):

                if X[i, j].solution_value() > 0.5:

                    print("x[%d,%d]: %d" %(i, j, X[i, j].solution_value()))

else:

    print("No solution found.")
