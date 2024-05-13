# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:18:15 2024

@author: bse07
"""

from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver("SCIP")

infinity = solver.infinity()

#의사 결정 변수
w1 = solver.NumVar(0, infinity, "w1")
w2 = solver.NumVar(0, infinity, "w2")
s1 = solver.NumVar(0, infinity,"s1")
s2 = solver.NumVar(0, infinity,"s2")
s3 = solver.NumVar(0, infinity,"s3")

#제약 조건
solver.Add(6*w1+ 3*w2 + s1 == 3)
solver.Add(3*w1 + 4*w2 + s2 ==1)
solver.Add(5* w1 + 5*w2 + s3 == 4)

#목적함수
solver.Maximize(25*w1 + 20*w2)
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print("OPTIMAL")
    print("목적 함수 값 = " , solver.Objective().Value())
    print("w1 = %.5f" %(w1.solution_value()))
    print("w2 = %.5f" %(w2.solution_value()))
    print("s1 = %.5f" %(s1.solution_value()))
    print("s2 = %.5f" %(s2.solution_value()))
    print("s3 = %.5f" %(s3.solution_value()))


