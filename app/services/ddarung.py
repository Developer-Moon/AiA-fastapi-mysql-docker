from app.models.ddarung import DDarung

class DDarungService :
    
    ddarung = DDarung()
    
    def preprocess(self, path, train, test) -> object :
        model = self.ddarung
        this = model.context
        this.train = model.from_csv(path, train)
        this.test = model.from_csv(path, test)
        this.id = this.test['id']
        
        ''' this가 들어가서 
        this = model.missing_value_Process_median(this) 
        this = model.missing_value_Process_mean(this)
        this = model.missing_value_Process_drop(this) 여기로 나오는 구조라 생각
        '''
        
        return this
        
    
    def submit(self, path, train, test) :
        this = self.preprocess(path, train, test)
        print('### DF ### 구조보기')
        print(this.train.head())