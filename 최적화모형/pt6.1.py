#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 18:29:26 2024

@author: juhee
"""


from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver("SCIP")
infinity = solver.infinity()
X1 = solver.NumVar(0, infinity, "X1")
X2 = solver.NumVar(0, infinity, "X2")

# 제약 조건
solver.Add(X1<= 60)
solver.Add(X2 <= 50)
solver.Add(X1 + 2*X2 <= 120)

solver.Maximize(20*X1 + 30*X2) 
status = solver.Solve()


#출력
if status == pywraplp.Solver.OPTIMAL:
    print("OPTIMAL")
    print("목적 함수 값 = " , solver.Objective().Value())
    print("X1 = %.5f" %(X1.solution_value()))
    print("X2 = %.5f" %(X2.solution_value()))