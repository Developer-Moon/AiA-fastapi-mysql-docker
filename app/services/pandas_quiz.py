from calendar import c
import pandas as pd # 라이브러리고 pandas는 파일 그 안에 pd
import random
from icecream import ic
import numpy as np
import string


        
    



               

# 스칼라량은 단지 하나의 크기량
# 백터량은 방향과 크기를 동시에 나타내는 표현도구


class PandasQuiz(object) :
    def __init__(self) -> None :
        pass
    
##############################################################################################################  
# Q1. 다음 결과 출력
#        a  b  c
#     1  1  3  5
#     2  2  4  6
#     ic| df1:    a  b  c    열로 뽑으면 딕셔너리 
#              1  1  3  5    행으로 뽑으면 리스트 
#              2  2  4  6

    def quiz_01(self) : # 딕셔너리
        df = pd.DataFrame.from_dict({'1' : [1, 3, 5], '2' : [2, 4, 6]},  # 1, 3, 5를 [1, 3, 5] - 스칼라를 묶어서 다시 스칼라화
                                    orient='index',                      # 전체를 {}로 묶어서 엘리먼트로 전환
                                    columns=['a', 'b', 'c'])             # 생성자 데이터를 변환할떄 이렇게 메소드를 쓴다 - 딕셔너리로부터 데이터프레임을 만들어라
        ic(df)                                                           # orient='index -> 방향으로 해달라
        

############################################################################################################## 
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
    def quiz_02(self) : 
        df = pd.DataFrame.from_dict({'1' : [1, 2, 3], '2' : ['4', '5', '6'], '3' : ['7', '8', '9'], '4' : ['10', '11', '12']},
                                    orient='index',
                                    columns=['A', 'B', 'C'])
        ic(df)
##############################################################################################################              
#  Q3 두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성
#         ic| df3:     0   1   2
#                  0  95  25  74
#                  1  44  24  97    
    def quiz_03(self) :
        df = pd.DataFrame.from_dict({'0': random.sample(range(10,100), 3), '1': random.sample(range(10,100), 3)}, orient='index')
        ic(df)
##############################################################################################################
    def id(self) : # 내가 아이디 가져올꺼다# 기본틀 - id = ['' for i in []]
        return ["".join([random.choice(string.ascii_letters) for i in range(5)]) for i in range(10)]
       
    def score(self) :
        return np.random.randint(0, 101, (10, 4))
        # return random.sample(range(0, 101), 4)

    def df(self) :
        return pd.DataFrame(self.score(), index=self.id(), columns=['국어', '영어', '수학', '사회'])

# Q4 국어, 영어, 수학, 사회 4과목을 시험치른 10명의 학생들의 성적표 작성. 단 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID 로 표기
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
    def quiz_04(self) :
        ic(self.df())

############################################################################################################## 
# Q5 원하는 과목 점수만 출력하시오. (만약 국어라고 입력하면 아래와 같이 출력됨)
# hVoGW    93
# QkpKK    25
# oDmky    82
# qdTeX    51
# XGzWk    34
# PAwgj    85
# vnTmB    28
# wuxIm    58
# AOQFG    32
# jHChe    59
# Name: 국어, dtype: int64
    def quiz_05(self) :
        print(self.df()[input('과목입력 : ')] ) # self.quiz_04()[]        input('과목입력 : ')
############################################################################################################## 
# Q6 원하는 학생점수만 출력하시오. (아이디가 랜덤이므로 맨 위에 학생점수 출력으로 대체함)
#     lDZid  57  90  55  24
    def quiz_06(self) :
        first_df = self.df()
        print(first_df)
        print(f'첫번째의 성적', first_df.iloc[0:1]) # 당연히 id 가 일치할리 없음. 형식적으로 출력함
##############################################################################################################  
# Q7 각 학생들의 점수의 총합과 마지막 행은 과목총점 추가해서 출력
#     ic| df5:  국어   영어   수학   사회   과학    총점
#                 hVoGW   93   44   14   94   86   331
#                 QkpKK   25   54   29   10    8   126
#                 oDmky   82   65   31   31    2   211
#                 qdTeX   51   56   56    3   13   179
#                 XGzWk   34   32   67   48   23   204
#                 PAwgj   85   24   16    8   22   155
#                 vnTmB   28   80   52   43   48   251
#                 wuxIm   58   94   93   54   83   382
#                 AOQFG   32   50   95    1   52   230
#                 jHChe   59   37   80   27   39   242
#                 과목총점   547  536  533  319  376  2311
    def quiz_07(self) :
        self.df().append(columns=['과학', '총점'])
        # self.score().append()
        print(self.df())
        

    
    
    
    
    
        

  

# 오버로딩   - 덮어쓰기  "".join 지역변수를 제거했다[속도가 빨라진다]
# 오버라이드 - ???????        
        
    

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


#-----------------------------------------------------------
# None                              
# def quiz_04(self) : Predicate                                                                      # 파라미터 없이 return만 있는거
#    retrun Boolean

# setter -> write ==> Consumer                                                                       # return 없이 파라미터만 있는거
# def quiz_04(self, a, b) :
#   self.c = d
    
    
# getter => read only ==> Supplier         api사용 및 랜덤하여 라는 말은 Supplier                      # 파라미터 없이 return만 있는거 - 외부에서 값을 get한다
# def quiz_04(self) -> c : 
#    return c

# setter + getter ==> Function                                                                       # return과 파라미터 모두 있는거
# def quiz_04(self, a, b) -> c : 
#     return c

# constant : 디스크에
# variable : a메모리에
#-----------------------------------------------------------
