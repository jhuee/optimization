# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 17:21:57 2024

@author: bse07
"""

from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver("SAT")

profit = [17,10,15,19,7,13,9]
req = [43,28,34,48,17,32,23]

x={}

for i in range(7):
    x[i] = solver.IntVar(0,1, "x"+str(i))
    
solver.Add(x[0] + x[1] == 1)
solver.Add(x[2] + x[3] == 1)
solver.Add(x[0] + x[1] >= x[2] + x[3])
solver.Add(solver.Sum(req[i] * x[i] for i in range(7)) <= 100)

# obj_expr = []
# for i in range(len(profit)):
#     obj_expr.append = [profit[i] * x[i]]

solver.Maximize(solver.Sum(profit[i] * x[i] for i in range(7)))
with open('or4-5.lp', "w") as out_f:
    lp_text = solver.ExportModelAsLpFormat(False)
    out_f.write(lp_text)
status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
   print("Objective value =", solver.Objective().Value())
   for i in range(7):
       print(x[i], " = ", x[i].solution_value())
else:
    print("The problem does not have an optimal solution.")