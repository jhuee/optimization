# -*- coding: utf-8 -*-
"""
Created on Mon May 13 15:11:59 2024

@author: bse07
"""

from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver("SCIP")

infinity = solver.infinity()

#의사결정 변수 -> A, B 기계에서 part i 를 생산하는 양 (i = 0, 1, 2)
A = {}
B = {}

for i in range(3) :
    A[i] = solver.NumVar(0, infinity, "A" + str(i))
    B[i] = solver.NumVar(0, infinity, "B" + str(i))
    
#제약 조건
solver.Add(12*A[0] + 15*A[1] <= 24*3)
solver.Add(6*B[0] + 12*B[1] +25*B[2] <= 24*5)

solver.Maximize()