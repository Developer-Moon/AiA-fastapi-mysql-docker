import pandas as pd # 라이브러리고 pandas는 파일 그 안에 pd
import random
from icecream import ic
import numpy as np
import string
# Q1. 다음 결과 출력
#            a  b  c
#         1  1  3  5
#         2  2  4  6
#         ic| df1:    a  b  c    열로 뽑으면 딕셔너리 
#                  1  1  3  5    행으로 뽑으면 리스트 
#                  2  2  4  6

        
    
# Q2. 다음 결과 출력
#    A   B   C
# 1   1   2   3
# 2   4   5   6
# 3   7   8   9
# 4  10  11  12
# ic| df2:     A   B   C
#          1   1   2   3
#          2   4   5   6
#          3   7   8   9
#          4  10  11  12


               

# 스칼라량은 단지 하나의 크기량
# 백터량은 방향과 크기를 동시에 나타내는 표현도구


class PandasQuiz(object) :
    def __init__(self) -> None :
        pass

    def quiz_01(self) : # 딕셔너리
        df = pd.DataFrame.from_dict({'1' : [1, 3, 5], '2' : [2, 4, 6]},  # 1, 3, 5를 [1, 3, 5] - 스칼라를 묶어서 다시 스칼라화
                                    orient='index',                      # 전체를 {}로 묶어서 엘리먼트로 전환
                                    columns=['a', 'b', 'c'])             # 생성자 데이터를 변환할떄 이렇게 메소드를 쓴다 - 딕셔너리로부터 데이터프레임을 만들어라
                                                                         # orient='index -> 방향으로 해달라
        ic(df)


    def quiz_02(self) : 
        df = pd.DataFrame.from_dict({'1' : [1, 2, 3], '2' : ['4', '5', '6'], '3' : ['7', '8', '9'], '4' : ['10', '11', '12']},
                                    orient='index',
                                    columns=['A', 'B', 'C'])
        ic(df)
        
        
#  Q3 두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성
#         ic| df3:     0   1   2
#                  0  95  25  74
#                  1  44  24  97    

    def quiz_03(self) :
        df = pd.DataFrame.from_dict({'0': random.sample(range(10,100), 3), '1': random.sample(range(10,100), 3)}, orient='index')
        ic(df)

 

    def quiz_04(self) :
        name = ""   
        for i in range(5) :
            name +=random.choice(string.ascii_letters)      
        
        df = pd.DataFrame.from_dict({name : random.sample(range(10,100), 4)}, orient='index', columns=['국어', '영어', '수학', '사회'])

        for i in range(9) :
            name = ""   
            for i in range(5) :
                name +=random.choice(string.ascii_letters) 
                
            df = pd.concat([df, pd.DataFrame.from_dict({name : random.sample(range(10,100), 4)}, orient='index', columns=['국어', '영어', '수학', '사회'])], axis=0)
        ic(df)




# Q4 국어, 영어, 수학, 사회 4과목을 시험치른 10명의 학생들의 성적표 작성.
# 단 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID 로 표기
# ic| self.id(): 'HKKHc'
# ic| self.score(): 22
# ic| df4:        국어  영어  수학  사회
#         lDZid  57  90  55  24
#         Rnvtg  12  66  43  11
#         ljfJt  80  33  89  10
#         ZJaje  31  28  37  34
#         OnhcI  15  28  89  19
#         claDN  69  41  66  74
#         LYawb  65  16  13  20
#         QDBCw  44  32   8  29
#         PZOTP  94  78  79  96
#         GOJKU  62  17  75  49
    
