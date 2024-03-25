# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:22:16 2024

@author: bse07
"""
from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver("SCIP")

infinity = solver.infinity()

#의사 결정 변수
S = solver.NumVar(0,infinity,"S")
F = solver.NumVar(0,infinity,"F")

#제약 조건
solver.Add(0.5*S + 0.8*F <= 20*2400)
solver.Add(0.2*S <= 5*2400)
solver.Add(0.3*S + 0.5*F <= 10*2400)
solver.Add(0.1*F <= 3*2400)
solver.Add(0.3*F <= 6*2400)

#목표함수
solver.Maximize(S+F)
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print("OPTIMAL:") 
    print("목적 함수 값은 = %.1f" % solver.Objective().Value())
    print("S = %.1f" %(S.solution_value()))
    print("F = %.1f" %(F.solution_value()))
else:
    print("해를 찾을 수 없음")
