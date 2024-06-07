# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 20:43:07 2024

@author: bse07
"""

from ortools.linear_solver import pywraplp
solver= pywraplp.Solver.CreateSolver("SCIP")

costs = [
[90, 76, 75, 70, 50, 74, 12, 68],
[35, 85, 55, 65, 48, 101, 70, 83],
[125, 95, 90, 105, 59, 120, 36, 73],
[45, 110, 95, 115, 104, 83, 37, 71],
[60, 105, 80, 75, 59, 62, 93, 88],
[45, 65, 110, 95, 47, 31, 81, 34],
[38, 51, 107, 41, 69, 99, 115, 48],
[47, 85, 57, 71, 92, 77, 109, 36],
[39, 63, 97, 49, 118, 56, 92, 61],
[47, 101, 71, 60, 88, 109, 52, 90],
]

nW = len(costs)
nT = len(costs[0])

task_sizes = [10, 7, 3, 12, 15, 4, 11, 5]

x = {}
for worker in range(nW):
    for task in range(nT):
        x[worker, task] = solver.BoolVar(f"x[{worker},{task}]")
        
for worker in range(nW):
    for task in range(nT):
        solver.Add(x[worker,task] <=15)
        
for task in range(nT) :
    for worker in range(nW):
        solver.Add(x[worker, task] == 1)
        
obj_expr = []
for i in range(nW):
    for j in range(nT):
        obj_expr.append(x[i,j] *costs[i][j])
# for worker in range(nW):
#     for task in range(nT):
#         obj_expr.append(costs[worker][task] * x[worker, task])
solver.Minimize(solver.Sum(obj_expr))
with open('or6-3.lp', "w") as out_f:
    lp_text = solver.ExportModelAsLpFormat(False)
    out_f.write(lp_text)
# Solve
status = solver.Solve()
# Print solution.
if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
    print(f"Total cost = {solver.Objective().Value()}\n")
    for worker in range(nW):
        for task in range(nT):
            if x[worker, task].solution_value() > 0.5:
                print(f"Worker {worker} assigned to task {task}." + f" Cost: {costs[worker][task]}")
else:
    print("No solution found.")