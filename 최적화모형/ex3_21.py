# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 19:24:22 2024

@author: qwert
"""

from ortools.linear_solver import pywraplp
solver = imsolver = pywraplp.Solver.CreateSolver("SCIP")

infinity = solver.infinity()

#의사결정 변수
X1 = solver.NumVar(0, infinity, 'X1')
X2 = solver.NumVar(0, infinity, 'X2')
X3 = solver.NumVar(0, infinity, 'X3')

#제약조건
solver.Add(3*X1 + 4*X2 + 2*X3  <= 600)
solver.Add(2*X1 + X2 + 2*X3 <= 400)
solver.Add(X1 + 3*X2 + 3*X3 <= 300)

#목적함수
solver.Maximize(2*X1 + 4*X2 + 2.5*X3)

status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print("OPTIMAL:") 
    print("목적 함수 값은 = %.1f" % solver.Objective().Value())
    print("X1 = %.1f" %(X1.solution_value()))
    print("X2 = %.1f" %(X2.solution_value()))
    print("X3 = %.1f" %(X3.solution_value()))
else:
    print("해를 찾을 수 없음")
