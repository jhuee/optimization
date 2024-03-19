# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:09:02 2024

@author: bse07
"""

from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver("SCIP")
infinity = solver.infinity()

#i가 smlxl j가 abc
beam = ['Small','Medium','Large','Exlarge']
machine = ['A','B','C']
rates = [
    [300, 600, 800],
    [250, 400, 700],
    [200, 350, 600],
    [100, 200, 300]
    ]
demands = [10000, 8000, 6000, 6000]
cost = [30, 50, 80]


#의사 결정 변수 Xij
x= {}
for i in range(len(beam)) :
    for j in range(len(machine)):
        x[i,j] = solver.NumVar(0, infinity,"X"+str(i)+str(j))
        
#제약 조건
const_expr=[]
#생산요구량 
for i in range(len(beam)) :
    const_expr = [rates[i][j] * x[i,j] for j in range(len(machine))]
    solver.Add(sum(const_expr)>= demands[i], beam[i] + '_demand')            
    
#기계시간 제약
for i in range(len(machine)) :
    const_expr = [x[j, i] for j in range(len(beam))]
    solver.Add(sum(const_expr)<= 50, beam[i]+'_capa')

#목적함수
obj_expr=[]
for i in range(len(beam)):
    for j in range(len(machine)):
        obj_expr.append(cost[j]*x[i,j])
        solver.Minimize(solver.Sum(obj_expr))
        
status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
    print("목적 함수 값은 = %.1f" %solver.Objective().Value())
    for i in range(len(beam)) :
        for j in range(len(machine)) :
            print(beam[i], "/" , machine[j], " = %.1f"  %x[i,j].solution_value() )