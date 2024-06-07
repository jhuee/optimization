# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 17:10:49 2024

@author: bse07
"""

from ortools.linear_solver import pywraplp
solver= pywraplp.Solver.CreateSolver("SAT")

ME = solver.IntVar(0,1 ,"ME")
MS = solver.IntVar(0, 1, "MS")
CE = solver.IntVar(0, 1, "MS")
CS = solver.IntVar(0, 1, "MS")
DE = solver.IntVar(0, 1, "MS")
DS = solver.IntVar(0, 1, "MS")
LE = solver.IntVar(0, 1, "MS")
LS = solver.IntVar(0, 1, "MS")

solver.Add(MS+ ME == 1)
solver.Add(DS+ DE == 1)
solver.Add(CS+ CE == 1)
solver.Add(LS+ LE == 1)
solver.Add(MS+DS+CS+LS == 2)
solver.Add(ME + DE + CE + LE == 2)

solver.Minimize(4.5*ME + 7.8*CE + 3.6*DE + 2.9*LE + 4.9*MS + 7.2*CS + 4.3*DS + 3.1*LS)

with open('or4-5.lp', "w") as out_f:
    lp_text = solver.ExportModelAsLpFormat(False)
    out_f.write(lp_text)
status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
   print("Objective value =", solver.Objective().Value())
   print(ME, " = ", ME.solution_value())
   print(MS, " = ", ME.solution_value())
   print(CE, " = ", ME.solution_value())
   print(CS, " = ", ME.solution_value())
   print(DE, " = ", ME.solution_value())
   print(DS, " = ", ME.solution_value())
   print(LE, " = ", ME.solution_value())
   print(LS, " = ", ME.solution_value())
else:
    print("The problem does not have an optimal solution.")