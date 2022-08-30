from dataclasses import dataclass
@dataclass # 데코레이터

class Context :      # 선택지가 하나일땐 초기 생성자 생략가능
    path  : str
    fname : str
    train : object 
    text  : object
    id    : str
    label : str    
    
    @property 
    def path(self) -> str : return self._path # <-get      _ : 안에 감춰진 - 외부로 노출을 하지 않는다
    
    @path.setter
    def path(self, path) : self._path = path  # <-set
    
    
    @property
    def fname(self) -> str : return self._fname
    
    @fname.setter
    def fname(self, fname) : self._fname = fname
    
    @property
    def train(self) -> object : return self._train
    
    @train.setter
    def train(self, train) : self._train = train
    
    @property
    def text(self) -> object : return self._text
    
    @text.setter
    def text(self, text) : self._text = text
    
    @property
    def id(self) -> str : return self._id
    
    @id.setter
    def id(self, id) : self._id = id
    
    @property
    def label(self) -> str : return self._label
    
    @label.setter
    def label(self, label) : self._label = label
    
    
    