# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 18:54:16 2024

@author: qwert
"""

from ortools.linear_solver import pywraplp
solver = imsolver = pywraplp.Solver.CreateSolver("SCIP")

infinity = solver.infinity()

#의사결정변수
corn = solver.NumVar(0, infinity, 'corn')
lime = solver.NumVar(0, infinity, 'lime')
fishmeal = solver.NumVar(0, infinity, 'fishmeal')

#제약조건
solver.Add(25*corn + 15*lime + 25*fishmeal >= 18)
solver.Add(25*corn + 15*lime + 25*fishmeal <= 22)
solver.Add(15*corn + 30* lime + 20*fishmeal >= 20)
solver.Add(5*corn + 12*lime + 8*fishmeal >= 6)
solver.Add(5*corn + 12*lime + 8*fishmeal <= 12)
solver.Add(corn + lime + fishmeal == 1)

#목적함수
solver.Minimize(0.1*corn+0.08*lime+0.12*fishmeal)
status = solver.Solve()

#출력
if status == pywraplp.Solver.OPTIMAL:
    print("OPTIMAL")
    print("목적 함수 값 = " , solver.Objective().Value())
    
    print("corn : %.1f " %(corn.solution_value()))
    print("lime : %.1f " %(lime.solution_value()))
    print("fishmeal : %.1f " %(fishmeal.solution_value()))


