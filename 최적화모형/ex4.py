# -*- coding: utf-8 -*-
"""
Created on Sat May  4 23:56:05 2024

@author: qwert
"""

from ortools.linear_solver import pywraplp



solver = pywraplp.Solver.CreateSolver("GLOP")



scosts = [[3, 5], [2, 3], [6, 3]]

avails = [

          [60, 80, 50], # stove

          [80, 50, 50]  # oven

          ]

required = [[100, 90], # stove

            [60, 120]  # oven

            ]



nWare = len(scosts)

nStore = len(scosts[0])



X = {}

for i in range(nWare):

    for j in range(nStore):

        X[i, j] = solver.NumVar(0, solver.infinity(), "X"+str(i)+str(j))

            



Y = {}

for i in range(nWare):

    for j in range(nStore):

        Y[i, j] = solver.NumVar(0, solver.infinity(), "Y"+str(i)+str(j))





# 제약조건

for i in range(nWare):

    c_expr1 = []

    c_expr2 = []

    for j in range(nStore):

        c_expr1.append(X[i, j])

        c_expr2.append(Y[i, j])

        

    solver.Add(sum(c_expr1) <= avails[0][i], '_'+str(i))

    solver.Add(sum(c_expr2) <= avails[1][i], '_'+str(i))



for i in range(nStore):

    c_expr1 = []

    c_expr2 = []

    for j in range(nWare):

        c_expr1.append(X[j, i])

        c_expr2.append(Y[j, i])

        

    solver.Add(sum(c_expr1) <= required[0][i], '_'+str(i))

    solver.Add(sum(c_expr2) <= required[1][i], '_'+str(i))



# 목적함수

obj_expr = []

for i in range(nWare):

    for j in range(nStore):

        obj_expr.append(scosts[i][j]*(X[i, j]+Y[i, j]))



solver.Maximize(solver.Sum(obj_expr))





with open('or9-3.lp', "w") as out_f:

    lp_text = solver.ExportModelAsLpFormat(False)

    out_f.write(lp_text)



status = solver.Solve()



if status == pywraplp.Solver.OPTIMAL:

    print("Objective value = %.1f" % solver.Objective().Value())

    for i in range(nWare):

        for j in range(nStore):

            if X[i, j].solution_value() > 0.5:

                print('X[%i, %i] = %.1f' %(i, j, X[i, j].solution_value()))

    for i in range(nWare):

        for j in range(nStore):

            if Y[i, j].solution_value() > 0.5:

                print('Y[%i, %i] = %.1f' %(i, j, Y[i, j].solution_value()))

else:

    print("The problem does not have an optimal solution.")