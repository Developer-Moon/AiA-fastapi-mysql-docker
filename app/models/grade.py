# 모델 식이 있는 곳 
class Grade(object) :
    def __init__(self, name, korean, english, math): # 파라미터 선언 
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math
        self.avg = 0.0 # 내부에서 사용
        
    def set_avg(self) :
        self.avg = (self.korean + self.english + self.math) / 3 # 프린트에 넣으면 연산속도가 느려진다
    
    def get_avg(self) :
        return self.avg