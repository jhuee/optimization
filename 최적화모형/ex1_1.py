# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 17:49:50 2024

@author: bse07
"""
from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver("SCIP")

# 변수 정의: 각 원료의 사용량 (톤)
corn = solver.NumVar(0, 6, 'corn') # 옥수수 사용량 ≤ 6톤
limestone = solver.NumVar(0,10, 'limestone') # 석회석 사용량 ≤ 10톤
beans = solver.NumVar(0, 4, 'beans') # 콩 사용량 ≤ 4톤
fish_meal = solver.NumVar(0, 5, 'fish_meal') # 생선 가루 ≤ 5톤

# 목적 함수: 전체 사료 원료 비용 최소화
#원료 별 1톤 당 가격 
solver.Minimize(0.20*corn + 0.12*limestone + 0.24*beans + 0.12*fish_meal)

# 영양소별 최소 필요량 제약조건 추가
# 예시: 소의 사료
solver.Add(corn*8 + limestone*6 + beans*10 + fish_meal*4 >= 6) # 비타민 최소 6
solver.Add(corn*10 + limestone*5 + beans*12 + fish_meal*8 >= 6) # 단백질 최소 6
solver.Add(corn*6 + limestone*10 + beans*6 + fish_meal*6 >= 7) # 칼슘 최소 7
solver.Add(corn*8 + limestone*6 + beans*6 + fish_meal*9 >= 4) # 조지방 최대 8
solver.Add(corn*8 + limestone*6 + beans*6 + fish_meal*9 <= 8) # 조지방 최대 8

# 양의 사료 영양소별 최소 필요량 제약조건 추가
solver.Add(corn*6 + limestone*10 + beans*6 + fish_meal*6 >= 6) # 칼슘 최소 6
solver.Add(corn*8 + limestone*6 + beans*6 + fish_meal*9 <= 6) # 조지방 최대 6

# 닭의 사료 영양소별 최소 필요량 제약조건 추가
solver.Add(corn*8 + limestone*6 + beans*10 + fish_meal*4 >= 4) # 비타민 최소 4
solver.Add(corn*8 + limestone*6 + beans*10 + fish_meal*4 <= 6) # 비타민 최대 6
solver.Add(corn*6 + limestone*10 + beans*6 + fish_meal*6 >= 6) # 칼슘 최소 6
solver.Add(corn*8 + limestone*6 + beans*6 + fish_meal*9 <= 6) # 조지방 최대 6
# 문제 풀기 및 결과 출력
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print('최적 솔루션 찾음!')
    print("목적 함수 값 = " , solver.Objective().Value())
    print('옥수수 사용량: %.1f' %(corn.solution_value()), '톤')
    print('석회석 사용량:  %.1f' %(limestone.solution_value()), '톤')
    print('콩 사용량: %.1f' %(beans.solution_value()), '톤')
    print('생선 가루: %.1f' %(fish_meal.solution_value()), '톤')
else:
    print('최적 솔루션이 존재하지 않습니다.')