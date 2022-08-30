import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))

from app.services.calculator import CalculatorService
from app.services.user import UserService
from app.services.grade import GradeService
from app.services.pandas_quiz import PandasQuiz


def print_menu() : 
    print("0. 전체 프로그램 종료")
    print("1. 계산기 프로그램")
    print("2. 로그인 프로그램") 
    print("3. 성적표 프로그램") 
    print("4. 판다스 퀴즈풀기") 
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
            
        elif menu == '4' : 
            quiz = PandasQuiz()
            while 1:  # while true 무한반복
                quiz_number = input('퀴즈번호 선택, 종료는 0 : ')
                if quiz_number == '0' :
                    break
                elif quiz_number == '1' :
                    quiz.quiz_01()
                elif quiz_number == '2' :
                    quiz.quiz_02()
                elif quiz_number == '3' :
                    quiz.quiz_03()
                elif quiz_number == '4' :
                    quiz.quiz_04() 
                elif quiz_number == '5' :
                    quiz.quiz_05()
                elif quiz_number == '6' :
                    quiz.quiz_06()  
                elif quiz_number == '7' :
                    quiz.quiz_07()   
        
            
            
            
            
            
if __name__ == '__main__' : 
    main()
    
    