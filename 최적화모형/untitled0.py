# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 18:51:39 2024

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

# 의사 결정 변수 
SW = {}
PW = {}
TW = {}
NW = {}

for i in range(nWeeks) :
    SW[i] = solver.NumVar(0, infinity, "SW" +str(i))
    PW[i] = solver.NumVar(0, infinity, "PW"+str(i))
    TW[i] = solver.NumVar(0, infinity, "TW" + str(i))
    NW[i] = solver.NumVar(0, infinity, "NW" + str(i))
    
    
# 제약 조건

#수요제약
solver.Add(400*SW[0] >= 1000*demands[0][0], 'swiss_req_'+str(0)) # 첫 주에 관한 제약
solver.Add(240*PW[0] >= 1000*demands[0][0], 'sharp_req_'+str(0)) 

for i in range(1, nWeeks): # 첫 주 제외
    solver.Add(400*SW[i]*SW[i-1] >= 1000*(demands[0][i]+demands[0][i-1]),'swiss_req_' +str(i))
    solver.Add(240*PW[i]*PW[i-1] >= 1000*(demands[1][i]+demands[1][i-1]),'sharp_req_' +str(i))

solver.Add(SW[7] + PW[7] == 100, 'final_capa')

# 노동자 제약조건
for i in range(nWeeks):
    temp_expr = []
    if i >= 2:
        temp_expr.append(NW[i-2])
    solver.Add(NW[i] <= 3 * TW[i], 'new_emp_const_'+str(i))
    solver.Add(SW[i] + PW[i] + TW[i] <= 70 + sum(temp_expr), 'workers_const_'+str(i))

# 목적 함수 : 비용 최소화

obj_expr = []
for i in range(nWeeks):
    obj_expr.append(40*SW[i])
    obj_expr.append(40*PW[i])
    obj_expr.append(40*TW[i])
    obj_expr.append(40*NW[i])

# Solve the model and print the result
status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
    print("목적 함수 값은 %.1f ="  %solver.Objective().Value())
    for i in range(nWeeks):
        print(SW[i].name(), " = %.1f" %(SW[i].solution_value()))
        print(PW[i].name(), " = %.1f" %(PW[i].solution_value()))
        print(TW[i].name(), " = %.1f" %(TW[i].solution_value()))
        print(NW[i].name(), " = %.1f" %(NW[i].solution_value()))
else:
    print("최적값이 존재하지 않습니다.")
#목적 함수
