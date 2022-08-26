from app.models.score import Score
        
        
class ScoreService(object) :
    def __init__(self) -> None :  
        pass
        
    def score(self, name, korean, english, math) :
        score = Score(self, name, korean, english, math)
        
        print(f'이름 : {score.name}')
        print(f'국어점수 : {score.korean}')
        print(f'영어점수 : {score.english}')
        print(f'수학점수 : {score.math}')
        print(f'등급 = {score.mean()}')
        
        