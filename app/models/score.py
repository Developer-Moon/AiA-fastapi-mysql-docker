
# 클래스에 학생의 이름을 입력하면
# 해당 학생이 얻은 '국어','영어','수학' 3과목의 평균점수에 따라 A - F 가지 출력하시오.

class Score(object) :
    def __init__(self, name, korean, english, math) : # 
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math
        
    def set_avg(self) :
        if (self.korean + self.english + self.math) / 3 >= 80 : 
            return 'A'
        
        elif 80 > (self.korean + self.english + self.math) / 3 >= 60 : 
            return 'B'
        
        elif 60 > (self.korean + self.english + self.math) / 3 >= 45 : 
            return 'C'
        
        elif 45 > (self.korean + self.english + self.math) / 3 >= 30 : 
            return 'D'
        
        elif 30 > (self.korean + self.english + self.math) / 3 >= 15 : 
            return 'E'
    
        elif 15 > (self.korean + self.english + self.math) / 3 >= 0 : 
            return 'F'
    
     