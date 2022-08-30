from app.models.grade import Grade

class GradeService(object):
    
    def __init__(self):
        self.avg = 0.0
        
    def set_avg(self):
        pass
    
    def get_avg(self):
        pass
    
    def set_grade(self):
        pass
    
    def get_grade(self):
        pass
    

       


'''
from app.models.grade import Grade


class GradeService(object) :
    def __init__(self) -> None:
        self.credit = 0   # 전역변수
    
    def set_grade(self, name, korean, english, math) :
        grade = Grade(name, korean, english, math)
        grade.set_avg()       # 여기서 에버리지 계산
        avg = grade.get_avg() # 그 값을 읽어온다
        
        
        if avg >= 90:
            self.credit = 'A'
        elif avg >= 80:
            self.credit = 'B'
        elif avg >= 70:
            self.credit = 'C'
        elif avg >= 60:
            self.credit = 'D'
        elif avg >= 50:
            self.credit = 'E'            
        else :
            self.credit = 'F'
        
    
    def get_grade(self, name, korean, english, math) :    # 파라미터
        self.set_grade(name, korean, english, math) # 아규먼츠
        return self.credit                                # 식은 set에서  return 은 get에서
    
'''