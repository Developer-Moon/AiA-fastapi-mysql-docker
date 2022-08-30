from fnmatch import fnmatchcase
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from app.utils.context import Context
import pandas as pd
#----------------------------------------------------------------------------------------------------------------#
from sklearn.pipeline import make_pipeline
#----------------------------------------------------------------------------------------------------------------#
# ___2.1.3. 모델의 선정과 파라미터 정리
# ___2.1.4. 전처리
# ___2.1.5. 학습
# ___2.1.6. 평가

class DDarung :
    
    context = Context() # 전역객체
    
    def __init__(self) -> None:
        self.train_set = None 
        self.test_set = None
        self.x_test = None
        self.y_test = None
        self.x_train = None
        self.y_train = None
        self.model = None
        
    def hook(self, path, train, test) :
        self.from_csv(path, train, test)
        self.preprocess()
        self.learning()
        self.test()
        self.missing_value_Process_median()
    
    #1. 데이터
    def from_csv(self, path, fname) :            
        this = self.context
        this.path = path
        this.fname = fname
        return pd.read_csv(this.path + this.fname)
        train_set = pd.read_csv(path + train, index_col=0)                                                               
        test_set = pd.read_csv(path + test, index_col=0) 
        
    # 결측지
    def missing_value_Process_median(self) : 
        train_set = train_set.fillna(train_set.mean())
        test_set = test_set.fillna(test_set.mean())                                                                                                  
        train_set = train_set.dropna() 
        x = train_set.drop(['count'], axis=1)        
        y = train_set['count']                  
        x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.75, random_state=1234)    
    
    
    #2. 모델구성
    # def preprocess(self) :
    #     pass
        
        
    def learning(self) :
        x_train = self.x_train
        y_train = self.y_train
        model = make_pipeline(MinMaxScaler(), RandomForestRegressor()) 
        model.fit(x_train, y_train) 
    
    def test(self) :
        x_test = self.x_test
        y_test = self.y_test
        model = self.model
        result = model.score(x_test, y_test)
        print('model.score :', result)
    
    
        
