class User(object) :
    def __init__(self, id, password) :
        self.id = id
        self.password = password

    def input_id(self) :
        return self.id
    
    def input_id(self) :
        return self.password

class Calculator(object) :                   # object를 넣으므로 Calculator 클래스는 객체가 된다
    def __init__(self, first, second) :      # 생성자, first, second 는 속성    init는 계산기라는 공간           def __init__(self) -> None :
        self.first = first   # 
        self.second = second
    
    def sum(self) :                          # ()가 있는건 메소드 - self는 class Calculator(object)에 종속 되어있다 라는 말 
        return self.first + self.second
    
    def subtract(self) :                          
        return self.first - self.second
    
    def mutliple(self) :                          
        return self.first * self.second
    
    def divide(self) :                          
        return self.first / self.second      