# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 23:07:50 2024

@author: qwert
"""


from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver("SCIP")

# 의사 결정 변수
A = solver.NumVar(0, solver.infinity(), "A")
C = solver.NumVar(0, solver.infinity(), "C")

#제약조건 A는 일간 60 이하, B는 50이하
#A노동 요구량은 1, C는 2
#
solver.Add(A<=6s0) 
solver.Add(C <= 50)
solver.Add(A + 2 * C <=120)

#목적함수
solver.Maximize(20*A + 30*C)

status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print("OPTIMAL")
    print("목적함수 값 = ", solver.Objective().Value())
    print("A = %.1f" %(A.solution_value()))
    print("C = %.1f" %(C.solution_value()))