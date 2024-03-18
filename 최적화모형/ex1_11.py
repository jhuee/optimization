# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 07:06:10 2024

@author: qwert
"""
from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver("SCIP")
infinity = solver.infinity()

weeks = 8

demands = [
    [12, 12, 12, 16, 16, 20, 20, 20],  # Swiss
    [8, 8, 10, 10, 12, 12, 12, 12]     # Sharp
]


# 의사 결정 변수 -> 딕셔너리 형태로
SwissWeek = {}
SharpWeek = {}
TotalWorkers = {}
NewWorkers = {}


for i in range(weeks):
    SwissWeek[i] = solver.NumVar(0, infinity, "SwissWeek[%d]" % i)
    SharpWeek[i] = solver.NumVar(0, infinity, "SharpWeek[%d]" % i)
    TotalWorkers[i] = solver.NumVar(0, infinity, "TotalWorkers[%d]" % i)
    NewWorkers[i] = solver.NumVar(0, infinity, "NewWorkers[%d]" % i)

# 수요 제약조건
solver.Add(400*SwissWeek[0] >= 1000*demands[0][0], 'swiss_req_0') 
solver.Add(240*SharpWeek[0] >= 1000*demands[1][0], 'sharp_req_0')

for i in range(1, weeks):
    solver.Add(400*(SwissWeek[i] + SwissWeek[i-1]) >= 1000*(demands[0][i] + demands[0][i-1]), 'swiss_req_'+str(i))
    solver.Add(240*(SharpWeek[i] + SharpWeek[i-1]) >= 1000*(demands[1][i] + demands[1][i-1]), 'sharp_req_'+str(i))

solver.Add(SwissWeek[7] + SharpWeek[7] == 100, 'final_capa')

# 노동자 제약조건
for i in range(weeks):
    temp_expr = []
    if i >= 2:
        temp_expr.append(NewWorkers[i-2])
    solver.Add(NewWorkers[i] <= 3 * TotalWorkers[i], 'new_emp_const_'+str(i))
    solver.Add(SwissWeek[i] + SharpWeek[i] + TotalWorkers[i] <= 70 + sum(temp_expr), 'workers_const_'+str(i))

# 목적 함수 : 비용 최소화
obj_expr = []
for i in range(weeks):
    obj_expr.append(40*SwissWeek[i] + 40*SharpWeek[i] + 40*TotalWorkers[i] + 40*NewWorkers[i])                
solver.Minimize(solver.Sum(obj_expr))

# Solve the model and print the result
status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
    print("목적 함수 값은 %.1f ="  %solver.Objective().Value())
    for i in range(weeks):
        print(SwissWeek[i].name(), " = %.1f" %(SwissWeek[i].solution_value()))
        print(SharpWeek[i].name(), " = %.1f" %(SharpWeek[i].solution_value()))
        print(TotalWorkers[i].name(), " = %.1f" %(TotalWorkers[i].solution_value()))
        print(NewWorkers[i].name(), " = %.1f" %(NewWorkers[i].solution_value()))
else:
    print("최적값이 존재하지 않습니다.")