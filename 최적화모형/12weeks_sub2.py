# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:41:32 2024

@author: qwert
"""

from ortools.linear_solver import pywraplp
solver= pywraplp.Solver.CreateSolver("SAT")

infinity = solver.infinity()
BIGM = 100000000

x1 = solver.NumVar(0, infinity, "x1")
x2 = solver.NumVar(0, infinity, "x2")
x3 = solver.NumVar(0, infinity, "x3")
x4 = solver.NumVar(0, infinity, "x3")

y1 = solver.NumVar(0, 1, "y1")
y2 = solver.NumVar(0, 1, "y2")
y3 = solver.NumVar(0, 1, "y3")
y4 = solver.NumVar(0, 1, "y4")
y5 = solver.NumVar(0, 1, "y5")

solver.Add(y1+y2+y3+y4 <= 2)
solver.Add(y3 + y4 <= y1+y2)
# solver.Add(y4 <= y1+y2)
solver.Add(5*x1 + 3*x2 + 6*x3 + 4*x4 <= 6000 + BIGM*y5)
solver.Add(4*x1 + 6*x2 + 3*x3 + 5*x4 <= 6000 + BIGM*(1-y5))

solver.Add(x1 <=BIGM*y1)
solver.Add(x2 <=BIGM*y2)
solver.Add(x3 <=BIGM*y3)
solver.Add(x4 <=BIGM*y4)
solver.Maximize(70*x1 - 50000*y1 + 60*x2 - 40000*y2 + 90*x3 - 70000*y3 + 80*x4 - 60000*y4)
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print("OPTIMAL:") 
    print("목적 함수 값은 = %.1f" % solver.Objective().Value())
    print("x1 = %.1f" %(x1.solution_value()))
    print("x2 = %.1f" %(x2.solution_value()))
    print("x3 = %.1f" %(x3.solution_value()))
    print("x4 = %.1f" %(x4.solution_value()))
    print("y1 = %.1f" %(y1.solution_value()))
    print("y2 = %.1f" %(y2.solution_value()))
    print("y3 = %.1f" %(y3.solution_value()))
    print("y4 = %.1f" %(y4.solution_value()))
    print("y5 = %.1f" %(y5.solution_value()))
else:
    print("해를 찾을 수 없음")
