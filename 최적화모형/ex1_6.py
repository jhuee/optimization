# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 13:57:55 2024

@author: bse07
"""

from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver("SCIP")

infinity = solver.infinity()

#의사 결정변수
x = {}
for i in range (11) :
    x[i] = solver.NumVar(0, infinity, "x"+str(i))
    
#제약 조건
solver.Add(x[0] + x[1] <=2200) # 1년차
solver.Add(x[2]+ x[3] + x[4] <= x[0]*1.08) #2년 1년 예금
solver.Add(x[5]+ x[6] + x[7] <= x[2]*1.08 + x[1]*1.17) #3년
solver.Add(x[8]+ x[9] <= x[5]*1.08 + x[3]*1.17) #4년
solver.Add(x[10] <= x[8]*1.08 + x[6]+ 1.17 + x[4]*1.27) #5년

#목적함수
solver.Maximize(x[10]*1.08 + x[9]*1.17 + x[7]*1.27)
status = solver.Solve()

#출력
if status == pywraplp.Solver.OPTIMAL:
    print("OPTIMAL")
    print("목적 함수 값 = " , solver.Objective().Value())
    for i in range (len(x)) :
        print("x", [i]," = ", x[i].solution_value())

