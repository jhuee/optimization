# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:09:50 2024

@author: bse07
"""

from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver("SCIP")

infinity = solver.infinity()

# 의사결정 변수

x1 = solver.NumVar(0, infinity, "x1")
x2 = solver.NumVar(0, infinity, "x2")
x3 = solver.NumVar(0, infinity, "x3")

#제약조건
solver.Add(6* x1 + 3* x2 + 5*x3 <= 25)
solver.Add(3*x1 + 4*x2 + 5*x3 <= 20)

#목적함수
solver.Maximize(3*x1 + x2 + 4*x3)

status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print("OPTIMAL")
    print("목적 함수 값 = " , solver.Objective().Value())
    print("x1 = %.4f" %(x1.solution.value()))