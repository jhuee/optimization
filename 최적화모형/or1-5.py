# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 15:36:29 2024

@author: qwert
"""

from ortools.linear_solver import pywraplp
# 모델을 solver애 넣는다
solver = pywraplp.Solver.CreateSolver("SCIP")

#의사결정변수
#IntVar(lowerbound, upperbound, *lp타입파일의 이름)
#비음 조건도 포함됨
X1 = solver.IntVar(0, solver.Infinity(), "X1")
X2 = solver.IntVar(0, solver.Infinity(), "X2")

#제약조건
#*(곱하기) 넣어줄 것
solver.Add(8*X1 + 3*X2 <= 240)
solver.Add(4*X1 + 4*X2 <= 200)
solver.Add(X1 <= 25)
solver.Add(X2<=40)


#목적함수
solver.Maximize(30*X1 + 20*X2)

#결과값을 status로 넘김
status = solver.Solve()

#OPTIMAL 
#INFEASLE  : 가능해가 없음
#UNBOUNDED : 무한대가 됨 -> 모델링 잘 못 됐다는 의미
if status == pywraplp.Solver.OPTIMAL:
    print("OPTIMAL")
    print("목적 함수 값 = %.1f" %(solver.Objective().Value()))
    print('X1 = %.1f' %(X1.solution_value())) #실수값 한 자리
    
    
 