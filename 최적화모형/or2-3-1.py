# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 16:39:05 2024

@author: qwert
"""

from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver("SCIP")

#의사 결정 변수
x1 = solver.NumVar(0,10,"x1")
x2 = solver.NumVar(10,20,"x2")
x3 = solver.NumVar(0,10,"x3")
x4 = solver.NumVar(10,12,"x4")


#제약 조건
solver.Add(1800*x1 + 250*x2 + 500*x3 + 150*x4 <= 19800)
solver.Add(1800*x1 <= 10000)

#목적함수
solver.Maximize(90*x1 + 23*x2 + 30*x3 + 4*x4)


#출력
status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
    print("OPTIMAL")
    print("목적 함수 값 = ",  solver.Objective().Value())
    print("x1 = %.1f"%(x1.solution_value()))
    print("x2 = %.1f"%(x2.solution_value()))
    print("x3 = %.1f"%(x3.solution_value()))
    print("x4 = %.1f"%(x4.solution_value()))