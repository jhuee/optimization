# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:30:11 2024

@author: qwert
"""

from ortools.linear_solver import pywraplp

data = {}

data['constraint_coeffs'] = [
    [5,7,9,2,1],
    [18,4,-9,10,12],
    [4,7,3,8,5],
    [5,13,16,3,-7],
    ]

data['bounds'] = [250,285,211,315]
#maximize의 계수
data["obj_coeffs"] = [7,8,2,9,6]
#변수의 개수
data["num_vars"] = 5
data["num_constraints"] = 4

##create the mip solver with the SCIP backend

solver = pywraplp.Solver.CreateSolver("SCIP")

infinity = solver.infinity()

x = {}
#변수 개수 만큼 반복
#범위 지정 -> 변수 생성
for j in range(data["num_vars"]) :
    x[j] = solver.IntVar(0,infinity, "x[%i]" %j)
    

#제약 조건
for i in range(data["num_constraints"]) :
    constraint_expr = [data['constraint_coeffs'][i][j] * x[j] for j in range(data['num_vars'])]
    #제약조건 추가
    solver.Add(sum(constraint_expr) <= data['bounds'][i])
    

#목적 함수
objcetive = solver.Objective()
obj_expr = [data['obj_coeffs'][j] *x[i] for j in range(data['num_vars'])]
solver.Maximize(solver.Sum(obj_expr))

#문제풀이
print(f"Solving with {solver.SolverVersion()}")
status = solver.Solve()

#출력
if status == pywraplp.Solver.OPTIMAL:
    print("objective value =", solver.Objective().Value())
    for j in range(data["num_vars"]):
        print(x[j].name(), " = ", x[j].solution_value())
else : 
    print("The problem does not have an optimal solution")
    
    
#최댓값은 832.0, 최적값은 260