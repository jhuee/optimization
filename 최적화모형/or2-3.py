# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 18:32:02 2024

@author: qwert
"""

from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver("SCIP")

#의사 결정 변수
X1 = solver.NumVar(0,solver.infinity(), "X1")
X2 = solver.NumVar(0,solver.infinity(), "X2")
X3 = solver.NumVar(0,solver.infinity(), "X3")
X4 = solver.NumVar(0,solver.infinity(), "X4")
X5 = solver.NumVar(0,solver.infinity(), "X5")
X6 = solver.NumVar(0,solver.infinity(), "X6")

#제약식
solver.Add(10*X1 + 0*X2 + 20*X3 + 20*X4 + 10*X5 + 20*X6 >= 50 )
solver.Add(0*X1 + 10*X2 + 30*X3 + 10*X4 + 30*X5 + 20*X6 >= 60)

#목적함수

solver.Minimize(350*X1 + 300*X2 + 500*X3 + 240*X4 + 270*X5 + 400*X6)

#출력
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print("OPTIAML")
    print("목적 함수 값 = ", solver.Objective().Value())
    print('X1 = %.1f'%(X1.solution_value()))
    print('X2 = %.1f'%(X2.solution_value()))
    print('X3 = %.1f'%(X3.solution_value()))
    print('X4 = %.1f'%(X4.solution_value()))
    print('X5 = %.1f'%(X5.solution_value()))
    print('X6 = %.1f'%(X6.solution_value()))
