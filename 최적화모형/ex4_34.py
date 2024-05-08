# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:49:29 2024

@author: qwert
"""

#의사결정변수

from ortools.linear_solver import pywraplp
solver = imsolver = pywraplp.Solver.CreateSolver("SCIP")

infinity = solver.infinity()


for i in range(11):
    x[i] = solver.Numvar(0, infinity, "x"+str(i))
# 제약조건
solver.Add()


# 목적함수
solver.Maximize(2*X1 + 2*X2 + 3*X3)

status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print("OPTIMAL:") 
    print("목적 함수 값은 = %.1f" % solver.Objective().Value())
    print("X1 = %.1f" %(X1.solution_value()))
    print("X2 = %.1f" %(X2.solution_value()))
    print("X3 = %.1f" %(X3.solution_value()))
else:
    print("해를 찾을 수 없음")
