# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 15:51:18 2024

@author: bse07
"""

from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver("SAT")

infinity = solver.infinity()

x= {}
REQ = [2,2,2,2,2,2,8,8,8,8,4,4,3,3,3,3,6,6,5,5,5,5,3,3]
for i in range(24):
    x[i] = solver.IntVar(0, infinity, "x" + str(i))
    
#제약 조건
for i in range(24):
    const_expr = [x[(i-j) % 24 ] for j in range(9) if j !=4]
    solver.Add(solver.Sum(const_expr) >= REQ[i])


objective = solver.Objective()
solver.Minimize(solver.Sum([x[i] for i in range(24)]))
# 모델 파일 생성
with open('or4-3.lp', "w") as out_f:
    lp_text = solver.ExportModelAsLpFormat(False)
    out_f.write(lp_text)
status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
   print("Objective value =", solver.Objective().Value())
   for i in range(24):
       print(x[i].name(), " = ", x[i].solution_value())
else:
    print("The problem does not have an optimal solution.")