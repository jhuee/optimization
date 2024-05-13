# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:40:36 2024

@author: bse07
"""

from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver("SCIP")

infinity = solver.infinity()

#의사 결정변수
x1 = solver.NumVar(0, infinity, "x1")
x2 = solver.NumVar(0, infinity, "x2")  
x3 = solver.NumVar(0, infinity, "x3")    
x4 = solver.NumVar(0, infinity, "x4")    
  
#제약 조건
solver.Add(x1+ 2*x2+ 3*x3 +x4 >= 2)
solver.Add(-2*x1 + x2- x3 +3*x4 <= 3)
#목적함수
solver.Minimize(2*x1 + 3*x2 + 5*x3 + 6*x4)
status = solver.Solve()

#출력
if status == pywraplp.Solver.OPTIMAL:
    print("OPTIMAL")
    print("목적 함수 값 = " , solver.Objective().Value())
    print("x1 = %.5f" %(x1.solution_value()))
    print("x2 = %.5f" %(x2.solution_value()))
    print("x3 = %.5f" %(x3.solution_value()))
    print("x4 = %.5f" %(x4.solution_value()))