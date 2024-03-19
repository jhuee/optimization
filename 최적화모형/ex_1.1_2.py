# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:01:56 2024

@author: bse07
"""

from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver("SCIP")

infinity = solver.infinity()
#데이터

ing=['corn','limestone','soybeans','fish_meal']
nut=['vitamins','protein','calcium','fat']
product=['cattle','sheep','chicken']
demand=[10000,6000,8000]
contain = [
    [8,6,10,4],
    [10,5,12,8],
    [6,10,6,6],
    [8,6,6,9]
    ]
nut_min =[
    [6,6,4],
    [6,6,6],
    [7,6,6],
    [4,4,4]
    ]

nut_max =[
    [infinity, infinity,6],
    [infinity, infinity, infinity],
    [infinity, infinity, infinity],
    [8,6, 7]
    ]
cost = [0.20, 0.12, 0.24, 0.12]
#의사결정변수
#xij i는 소 닭 양 j는 ingredient
x={}

for i in range(len(product)):
    for j in range(len(ing)):
        x[i,j] = solver.NumVar(0, infinity, "X"+str(i)+str(j))
        
#제약조건
const_expr = []
#생산요구량
for i in range (len(product)):
    const_expr =[x[i,j] for j in range(len(ing))]
    solver.Add(sum(const_expr)>=demand[i], product[i] + "_demand")
    
#영양소 최소
const_expr1 = []
for i in range (len(nut)) :
    for j in range(len(product)):
        const_expr = [contain[i][k]*x[j,k] for k in range(len(ing))]
        const_expr1=[x[j,k] for k in range(len(ing))]
        solver.Add(sum(const_expr) >= nut_min[i][j]*sum(const_expr1), 'nutrient_min'+str(i)+str(j))
        
#영양소 최대
for i in range (len(nut)) :
    for j in range(len(product)):
        if nut_max[i][j] == infinity: continue
        const_expr = [contain[i][k]*x[j,k] for k in range(len(ing))]
        const_expr1=[x[j,k] for k in range(len(ing))]
        solver.Add(sum(const_expr) <= nut_max[i][j]*sum(const_expr1), 'nutrient_max'+str(i)+str(j))
        
#목적 함수: 최소 비용으로 사료 
obj_expr=[]
for i in range(len(product)):
    for j in range(len(ing)):
        obj_expr= [x[i,j]*cost[j]]
        solver.Minimize(solver.Sum(obj_expr))

#결과 출력
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print("OPTIMAL:") 
    print("목적 함수 값은 = %.1f" %solver.Objective().Value())
    for i in range(len(product)) :
        for j in range(len(ing)):
            print(x[i,j].name() ," = %.1f" %x[i,j].solution_value())
else : print("찾을 수 없음")
