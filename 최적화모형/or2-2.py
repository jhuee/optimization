# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 16:21:56 2024

@author: qwert
"""
#예제 2 식단 문제
from ortools.linear_solver import pywraplp
#의사 결정 변수 설정
solver = pywraplp.Solver.CreateSolver("SCIP")

data = {}

data["constraint_coeffs"] = [
    [10,0,20,20,10,20],
    [0,10,30,10,30,20],
    ]
data['supply'] = [50, 60]
data['num_vars'] = 6
data['prices'] = [350,300,500,340,270,400]
data['num_constraints'] = 2



x = {}

for j in range(data['num_vars']) :
    x[j] = solver.NumVar(0, solver.infinity(), "x[%i]"%j)
    
    
#제약 
for i in range(data['num_constraints']) : 
    constraint_expr = [data['constraint_coeffs'][i][j] * x[j] for j in range(data['num_vars'])]
    solver.Add(solver.Sum(constraint_expr) >= data['supply'][i])
    
#목적함수
object = solver.Objective()
obj_expr =[data['prices'][j] * x[j] for i in range(data['num_vars'])]
solver.Minimize(solver.Sum(obj_expr))

#출력
print(f"Solving with {solver.SolverVersion()}")

status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL :
    print("Object value = ", solver.Objective().Value()) 
    for j in range(data["num_vars"]) :
        print(x[j].name, " = ", x[j].solution_value())
else:
    print("The problem does not have an optimal solution")