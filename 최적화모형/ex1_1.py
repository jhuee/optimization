
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 17:49:50 2024

@author: bse07
"""
from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver("SCIP")

infinity = solver.infinity()
# 변수 정의
feed = ['cattle','sheep','chicken']
ing = ['corn','limestone','soybeans','fish_meal']
nut = ['vitamin','protein','calcium','crude_fat']
req = [10000, 6000, 8000] # kg

nuts = [
        [8, 6, 10, 4],
        [10, 5, 12, 8],
        [6, 10, 6, 6],
        [8, 6, 6, 9]
        ]

price = [0.2, 0.12, 0.24, 0.12] #kg
#영양소 별 최솟값
nut_min = [
    [6, 6, 4],
    [6, 6, 6], 
    [7, 6, 6], 
    [4, 4, 4]
    ]
#영양소 별 최댓값
nut_max =[
    [infinity, infinity, 6],
    [infinity, infinity, infinity],
    [infinity, infinity, infinity],
    [8, 6, 7]
    ]

data = {}

for i in range(len(feed)) : #3
    for j in range(len(ing)) : #4
        data[i, j] = solver.NumVar(0,infinity,"data" + str(i)+","+str(j))


#제약조건
const_expr = []

for i in range(len(feed)) : 
    const_expr = [data[i, j] for j in range(len(ing))]
    solver.Add(sum(const_expr) >= req[i], feed[i]+'_requirement')

# 영양소 최
for i in range(len(nut)):
    for j in range(len(feed)):
        const_expr = [nuts[i][k] * data[j,k] for k in range(len(ing))]  
        const_expr1 = [data[j,k] for k in range(len(ing))]
        solver.Add(sum(const_expr) >= nut_min[i][j]*sum(const_expr1), 'nutrient_min'+str(i)+","+str(j))


# 영양소 최댓값
for i in range(len(nut)):
    for j in range(len(feed)):
        if nut_max[i][j] == infinity: continue
        const_expr = [nuts[i][k] * data[j,k] for k in range(len(ing))]
        const_expr1 = [data[j,k] for k in range(len(ing))]
        solver.Add(sum(const_expr) <= nut_max[i][j]*sum(const_expr1), 'nutrient_max'+str(i)+","+str(j))
        

# 목적 함수: 전체 사료 원료 비용 최소화
obj_expr = []
for i in range(len(feed)):
    for j in range(len(ing)):
        obj_expr.append(price[j]*data[i, j])

solver.Minimize(solver.Sum(obj_expr))  

#결과 출력
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print('OPTIMAL')
    print("목적 함수 값 = %.1f" %(solver.Objective().Value()))
    for i in range(len(feed)):  
        for j in range(len(ing)):  
            print(data[i,j].name(), " = %.1f" %(data[i,j].solution_value()))
else:
    print("최적 값이 존재하지 않습니다.")