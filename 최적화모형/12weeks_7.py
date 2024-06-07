# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 18:07:31 2024

@author: bse07
"""

from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver("SCIP")
infinity = solver.infinity()
M = 10000000

x = {}
for i in range(2):
    for j in range(2):
        x[i,j] = solver.NumVar(0, infinity, "X" + str(i)+str(j))

y = {}
for i in range(3):
    y[i] = solver.IntVar(0,1, "Y" + str(i))

#제약
solver.Add(x[0,0]/50 + x[0,1]/40 <= 500+M*y[0]) 
solver.Add(x[1,0]/40 + x[1,1]/24 <= 700+M*(1-y[0]))
solver.Add(x[0,0] + x[0,1] <= M*y[1])
solver.Add(x[1,0] + x[1,1] <= M*y[2])
        
solver.Maximize(10*x[0,0]+ 15*[0,1] + 10*x[1,0] + 15*x[1,1] - 50000*y[1] - 80000*y[2])
with open('or4-7.lp', "w") as out_f:
    lp_text = solver.ExportModelAsLpFormat(False)
    out_f.write(lp_text)
status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
   print("Objective value =", solver.Objective().Value())
   for i in range(2):
       for j in range(2):
           print(x[i,j], " = ", x[i,j].solution_value())
else:
    print("The problem does not have an optimal solution.")