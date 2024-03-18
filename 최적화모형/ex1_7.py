# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 22:42:08 2024

@author: qwert
"""

from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver("SCIP")

infinity = solver.infinity()

beam = ['Small','Medium','Large','ExLarge']
machine = ['A','B','C']
cost = [30, 50, 80]
req = [1000, 8000, 6000, 6000]

rates = [
    [300, 600, 800], 
    [250, 400, 700], 
    [200, 350, 600], 
    [100, 200, 300]
    ]


#의사결정 변수
data = {}

for i in range (len(beam)):
    for j in range (len(machine)):
        data[i, j] = solver.NumVar(0, infinity, "data" + str(i) + ", "+ str(j))

#제약 조건
const_expr = []

for i in range(len(beam)) :
    const_expr = [rates[i][j] * data[i,j] for j in range(len(machine))]
    solver.Add(sum(const_expr) >= req[i], beam[i]+'_requirement')
    
for i in range(len(machine)) :
    const_expr = [data [j,i] for j in range(len(beam))]
    solver.Add(sum(const_expr) <= 50, beam[i]+'_capa')
    
obj_expr = []
for i in range(len(beam)) :
    for j in range(len(machine)) :
        obj_expr.append(cost[j]*data[i,j])
        
solver.Minimize(solver.Sum(obj_expr))

status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL : 
    print("목적 함수 값은 = %.1f" %(solver.Objective().Value()))
    for i in range(len(beam)) :
        for j in range(len(machine)) :
            print(beam[i], '/', machine[j], ': ', \
                  data[i, j].name(), " = %.1f" % data[i, j].solution_value())