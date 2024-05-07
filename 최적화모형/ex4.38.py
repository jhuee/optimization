# -*- coding: utf-8 -*-
"""
Created on Tue May  7 15:50:11 2024

@author: bse07
"""

from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver("SCIP")

infinity = solver.infinity()

#의사 결정변수
x = {}
for i in range (6) :
    x[i] = solver.NumVar(0, infinity, "x"+str(i))
#제약 조건
solver.Add(x[0] + x[1] + x[2] - x[3] == 12)
solver.Add(x[1] + 2*x[2] - x[4] == 10) 
solver.Add(2*x[0] + x[1] + x[2] - x[5] == 16)


#목적함수
solver.Minimize(400*x[0] + 600*x[1] + 900*x[2])
status = solver.Solve()

#출력
if status == pywraplp.Solver.OPTIMAL:
    print("OPTIMAL")
    print("목적 함수 값 = " , solver.Objective().Value())
    for i in range (len(x)) :
        print("x", [i]," = ", x[i].solution_value())
else:
    print("The problem does not have an optimal solution.")