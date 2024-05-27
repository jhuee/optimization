# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:28:38 2024

@author: qwert
"""

from ortools.linear_solver import pywraplp
solver= pywraplp.Solver.CreateSolver("SAT")

infinity = solver.infinity()
BIGM = 100000000

x1 = solver.NumVar(0, infinity, "x1")
x2 = solver.NumVar(0, infinity, "x2")
x3 = solver.NumVar(0, infinity, "x3")

y1 = solver.NumVar(0, 1, "y1")
y2 = solver.NumVar(0, 1, "y2")

solver.Add(0.2*x1 + 0.4*x2 +0.2*x3 <= 1)
solver.Add(x1 <= BIGM*y1)
solver.Add(x2 <= BIGM*y2)
solver.Add(x1 <= 3)
solver.Add(x2 <= 2) 
solver.Add(x3 <= 5)
solver.Add(y1 + y2 == 1)


#목표함수
solver.Maximize(2*x1 + 3*x2 + 0.8*x3- 3*y1 -2*y2)
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print("OPTIMAL:") 
    print("목적 함수 값은 = %.1f" % solver.Objective().Value())
    print("x1 = %.1f" %(x1.solution_value()))
    print("x2 = %.1f" %(x2.solution_value()))
    print("x3 = %.1f" %(x3.solution_value()))
    print("y1 = %.1f" %(y1.solution_value()))
    print("y2 = %.1f" %(y2.solution_value()))
else:
    print("해를 찾을 수 없음")
