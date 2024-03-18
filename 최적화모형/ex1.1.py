# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:45:43 2024

@author: bse07
"""

from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver("SCIP")

#의사결정 변수
X1 =solver.NumVar(0, solver.infinity(), "X1")
X2 = solver.NumVar(0, solver.infinity(), "X2")

#제약 조건
solver.Add(X1+X2 >= 6)
solver.Add(-X1 - 2*X2 >= -18)

#목적함수
solver.Minimize(2*X1 + 5*X2)

status = solver.Solve()

#출력
if status == pywraplp.Solver.OPTIMAL:
    print("OPTIMAL")
    print("목적 함수 값 = " , solver.Objective().Value())
    print("X1 = %.1f" %(X1.solution_value()))
    print("X2 = %.1f" %(X2.solution_value()))