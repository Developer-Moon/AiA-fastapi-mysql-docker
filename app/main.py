import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))

from app.services.calculator import CalculatorService
from app.services.user import UserService
from app.services.grade import GradeService

def print_menu() : 
    print("0. 전체 프로그램 종료")
    print("1. 계산기 프로그램")
    print("2. 로그인 프로그램") 
    print("3. 성적표 프로그램") 
    menu = input('메뉴 선택')  
    return menu

def main() :                                           # main() 
    while 1:                
        menu = print_menu()                
        if menu == '0' :
            print('전체 프로그램을 종료합니다')
            break
        
        elif menu == '1':
            calculatorService = CalculatorService() 
            first = int(input('첫번째 값 : ')) # 여기서 쓸땐 아규먼트 
            second = int(input('두번째 값 : '))
            calculatorService.calculate(first, second) # calculate()  식
            
        elif menu == '2' :
            userService = UserService()
            id = input('id입력 :')
            password = input('비번입력 :')
            userService.user_input(id, password) # id, password 아규먼트 
            
        elif menu == '3' :
            gradeService = GradeService() # 생성자
            name = input('이름 :')
            korean = int(input('국어 :'))
            english = int(input('영어 :'))
            math = int(input('수학 :'))
            grade = gradeService.get_grade(name, korean, english, math)
            print(f'이름 : {name} 학점 : {grade}')
            
            
            
            
if __name__ == '__main__' : 
    main()
    
    