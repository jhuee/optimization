#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 18:37:28 2024

@author: juhee
"""


from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver("SCIP")

infinity = solver.infinity()

#의사 결정변수
w1 = solver.NumVar(0, infinity, "w1")
w2 = solver.NumVar(0, infinity, "w2")    
s1 = solver.Numvar(0, infinity, "s1")
s2 = solver.Numvar(0, infinity, "s2")
s3 = solver.Numvar(0, infinity, "s3")
s4 = solver.Numvar(0, infinity, "s4")

#제약 조건
solver.Add(w1 + 2*w2 +s1 == 2)
solver.Add(2*w1 -w2 + s2 == 3)
solver.Add(3*w1 + w2 + s3 == 5)
solver.Add(w1 - 3*w2 +s4 == 6) 
#목적함수
solver.Maximize(2*w1 + 3*w2)
status = solver.Solve()

#출력
if status == pywraplp.Solver.OPTIMAL:
    print("OPTIMAL")
    print("목적 함수 값 = " , solver.Objective().Value())
    print("w1 = %.5f" %(w1.solution_value()))
    print("w2 = %.5f" %(w2.solution_value()))
    print("s1 = %.5f" %(s1.solution_value()))
    print("s2 = %.5f" %(s2.solution_value()))
    print("s3 = %.5f" %(s3.solution_value()))
    print("s4 = %.5f" %(s4.solution_value()))



