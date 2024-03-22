# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 18:48:10 2024

@author: bse07
"""

from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver("SCIP")

infinity = solver.infinity()

oil_type = [
    [0.4, 0.2, 0.35],  # light_crude 기름 비율
    [0.32, 0.4, 0.2]   # heavy_crude 기름 비율
]
crude = ['light_crude', 'heavy_crude']
oil = ['gasoline', 'kerosene', 'jet_fuel']
demand = [1000000, 400000, 250000]  # 각 연료별 수요량
cost = [11, 9]  # 각 원유별 비용


# 의사 결정 변수
x = {}
for i in range(len(crude)):
    for j in range(len(oil)):
        x[i, j] = solver.NumVar(0, infinity, f"x{i}{j}")

# 제약조건 추가
for j in range(len(oil)):
    # 각 연료별 수요량을 충족시키는 제약 조건
    solver.Add(sum(oil_type[i][j] * x[i, j] for i in range(len(crude))) >= demand[j])

# 목적함수
solver.Minimize(sum(cost[i] * sum(x[i, j] for j in range(len(oil))) for i in range(len(crude))))

# 결과 출력
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print("OPTIMAL:") 
    print("목적 함수 값은 = %.1f" % solver.Objective().Value())
    
    for i in range(len(crude)):
        for j in range(len(oil)):
            print(f"{x[i,j].name()} = {x[i,j].solution_value()}")
else:
    print("해를 찾을 수 없음")
