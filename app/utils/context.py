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
    def path(self) -> str : return self._path # <-get      _ : 안에 감춰진 
    
    
    @path.setter
    def path(self, path) : self._path = path  # <-set