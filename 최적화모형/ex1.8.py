# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 19:41:00 2024

@author: qwert
"""

from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver("SCIP")

infinity = solver.infinity()

nWeeks = 8

demands = [
 [12, 12, 12, 16, 16, 20, 20, 20],
 [8, 8, 10, 10, 12, 12, 12, 12]
 
 ]
 #의사결정 변수
SW = {}
PW = {}
TW = {}
NW = {}

for i in range(nWeeks) :
    SW[i] = solver.NumVar(0, infinity, "SW[%d]" % i)
    PW[i] = solver.NumVar(0, infinity, "PW[%d]" % i)
    TW[i] = solver.NumVar(0, infinity, "TW[%d]" % i)
    NW[i] = solver.NumVar(0, infinity, "NW[%d]" % i)
    
    
#수요 제약
#첫 주
solver.Add(400*SW[0] >= 1000*demands[0][0],'swiss_req_'+str(0))
solver.Add(240*PW[0] >= 1000*demands[1][0], 'sharp_req_'+str(0))

for i in range(1, nWeeks):
    solver.Add(400*(SW[i] + SW[i-1]) >= 1000*(demands[0][i] + demands[0][i-1]), 'swiss_req_'+str(i))
    solver.Add(240*(PW[i] + PW[i-1]) >= 1000*(demands[1][i] + demands[1][i-1]), 'sharp_req_'+str(i))
    
solver.Add(SW[7] + PW[7] == 100, 'final_capa')

temp_expr = []
for i in range(nWeeks):
    if i >= 2:
        temp_expr.append(NW[i-2])
        solver.Add(NW[i] <= 3 * TW[i], 'new_emp_const_'+str(i))
        solver.Add(SW[i] + PW[i] + TW[i] <= 70 + sum(temp_expr), 'workers_const_'+str(i))
        
#목적함수
obj_expr = []
for i in range(nWeeks):
    obj_expr.append(40*SW[i])
    obj_expr.append(40*PW[i])
    obj_expr.append(40*TW[i])
    obj_expr.append(40*NW[i])
    solver.Minimize(solver.Sum(obj_expr))
    
    
 
with open('ex1-8.lp', "w") as out_f:
     lp_text = solver.ExportModelAsLpFormat(False)
     out_f.write(lp_text)
     print(f"Solving with {solver.SolverVersion()}")
     
     
status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
    print("Objective value =", solver.Objective().Value())
    for i in range(nWeeks):
        print(SW[i].name(), " = ", SW[i].solution_value())
        print(PW[i].name(), " = ", PW[i].solution_value())
        print(TW[i].name(), " = ", TW[i].solution_value())
        print(NW[i].name(), " = ", NW[i].solution_value())
else:
    print("The problem does not have an optimal solution.")
