# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:19:44 2024

@author: bse07
"""

from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver("SAT")

x= {}

Ratings = [
[None,9,3,4,2,1,5,6],
[None,None,1,7,3,5,2,1],
[None,None,None,4,4,2,9,2],
[None,None,None,None,1,5,5,2],
[None,None,None,None,None,8,7,6],
[None,None,None,None,None,None,2,3],
[None,None,None,None,None,None,None,4]
]

# 의사결정 변수
nC = len(Ratings[0])
for i in range(nC):
    for j in range(nC):
        if i != j :
            x[i,j] = solver.IntVar(0, 1, "X" + str(i)+ str(j))

# 제약 조건
const_expr = []
for i in range(nC):
    const_expr =[x[i,j] for j in range(nC) if i != j]
    solver.Add(solver.Sum(const_expr) == 1)
    
for i in range(nC):
    for j in range(nC):
        if i < j:
            solver.Add(x[i,j] == x[j, i], 'x_' + str(i)+str(j))
            
obj_expr = []
for i in range(nC-1):
    for j in range(nC):
        if Ratings[i][j] != None:
            obj_expr.append(Ratings[i][j]*x[i,j])

objective = solver.Objective()

solver.Maximize(solver.Sum(obj_expr))

with open('or4-4.lp', "w") as out_f:
    lp_text = solver.ExportModelAsLpFormat(False)
    out_f.write(lp_text)
status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
   print("Objective value =", solver.Objective().Value())
   for i in range(nC):
       for j in range(nC):
           if i!=j:
               print(x[i,j], " = ", x[i,j].solution_value())
else:
    print("The problem does not have an optimal solution.")