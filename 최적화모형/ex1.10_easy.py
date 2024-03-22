# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 18:48:10 2024

@author: bse07
"""


from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver("SCIP")

infinity = solver.infinity()

oil_type = [
    [0.4, 0.2, 0.35],
    [0.32, 0.4, 0.2]
    ]
crude = ['light_crude','heavy_crude']
oil = ['gasoline','kerosene','jet_fuel']
demand = [1000000, 500000, 300000]
cost = [20, 15]
lost = [0.95, 0.92]

#의사 결정 변수
#xij i는 light,heavy crude oil, j는 gas, ker, jet
x = {}
for i in range(len(crude)) :
    for j in range(len(oil)) :
        x[i,j] = solver.NumVar(0, infinity, "x"+str(i)+str(j))
        
#제약조건
const_expr = []
#손실량

#연료 별 수요량
solver.Add(0.4*x[0,0] +  0.32* x[1,0] >= 1000000)
solver.Add(0.2*x[0,1] +  0.4* x[1,1] >= 500000)
solver.Add(0.35*x[0,2] +  0.2* x[1,2] >= 300000)

#목적함수
solver.Minimize(20*(x[0,0]+x[0,1]+x[0,2]) + 15*(x[1,0]+x[1,1]+x[1,2]))
#결과 출력
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print("OPTIMAL:") 
    print("목적 함수 값은 = %.1f" %solver.Objective().Value())
    
    for i in range(len(crude)) :
        for j in range(len(oil)):
            print(x[i,j].name() ," = " ,x[i,j].solution_value())
else : print("찾을 수 없음")
