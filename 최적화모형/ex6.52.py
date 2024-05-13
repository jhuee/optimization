#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 19:08:04 2024

@author: juhee
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
solver.Add(6*x1 + 8*x2+ 10*x3 <= 5000 +x4)
solver.Add(100*x1 + 150*x2 + 120*x3 <= 60000)
#목적함수
solver.Maximize(60*x1 + 100*x2 + 80*x3 - 24*x4)
status = solver.Solve()

#출력
if status == pywraplp.Solver.OPTIMAL:
    print("OPTIMAL")
    print("목적 함수 값 = " , solver.Objective().Value())
    print("x1 = %.5f" %(x1.solution_value()))
    print("x2 = %.5f" %(x2.solution_value()))
    print("x3 = %.5f" %(x3.solution_value()))
    print("x4 = %.5f" %(x4.solution_value()))
