from app.models.calculator import Calculator

class CalculatorService(object) : # Calculator가 없으면 CalculatorService가 생길 수 없다 부모:Calculator, 자식:CalculatorService
    def __init__(self) -> None :                  # 전역변수                   () 표시는 __init__표시  self.calculator = Calculator()
                                                   
        pass
    
    def calculate(self, first, second) : # 파라미터
        calculator = Calculator(first, second)
        print(f'첫번째수: {calculator.first}')
        print(f'두번째수: {calculator.second}')
        print(f'{calculator.first} + {calculator.second} = {calculator.sum()}')
        print(f'{calculator.first} - {calculator.second} = {calculator.subtract()}')
        print(f'{calculator.first} * {calculator.second} = {calculator.mutliple()}')
        print(f'{calculator.first} / {calculator.second} = {calculator.divide()}')
