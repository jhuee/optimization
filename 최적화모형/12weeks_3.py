# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 17:43:59 2024

@author: bse07
"""

from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver("SAT")

x= {}
for i in range(4):
    x[i] = solver.IntVar(0,1,"x"+str(i))
values=[9,5,6,4]
solver.Add(x[0] + x[1] >= 1)
solver.Add(x[0] >= x[2])
solver.Add(x[1] >= x[3])
solver.Add(x[2] + x[3] == 1)
solver.Add(6*x[0] + 3*x[1] + 5*x[2] + 2*x[3] <= 11)
solver.Maximize(solver.Sum(values[i] *x[i] for i in range(4)))

with open('or13-1.lp', "w") as out_f:
    lp_text = solver.ExportModelAsLpFormat(False)
    out_f.write(lp_text)
status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
    print("OPTIMAL")
    print("목적함수값 = ", solver.Objective().Value())
    for i in range(4):
        print(x[i].name(), " = ", x[i].solution_value())
else:
    print("The problem does not have an optimal solution.")