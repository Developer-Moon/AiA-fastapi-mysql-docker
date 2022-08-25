# from typing import Union

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))

from app.services.calculator import CalculatorService

def print_menu() : 
    print("0. 전체 프로그램 종료")
    print("1. 계산기 프로그램")
    print("2. 로그인 프로그램") # 입력받은 아이디와 비번 콘솔에 출력하기
    menu = input('메뉴 선택')  # 콘솔 창에다가 값을 입력하라고 표시하는 값
    return menu

def main() :
    while 1:   # while 1: 는 무한                 
        menu = print_menu()                # print_menu() 함수
        if menu == '0' :
            print('전체 프로그램을 종료합니다')
            break # while문이라 limit가 없어서 사용
        
        elif menu == '1':
            calculatorService = CalculatorService() # CalculatorService : 식 - 값을 리턴       문 - if(브랜치?) for(룹 limit존재), while(룹 limit존재X)는 스테이트먼트
            first = int(input('첫번째 값 : '))
            second = int(input('두번째 값 : '))
            calculatorService.calculate(first, second)  # .calculate() 메소드
            
if __name__ == '__main__' : # 메인에서 사용하는 네임이라면
    main()
    
    