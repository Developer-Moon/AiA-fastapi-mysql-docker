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

def main() :
    calculatorService = CalculatorService()
    print_menu()

if __name__ == '__main__' : # 메인에서 사용하는 네임이라면
    main()
    
    