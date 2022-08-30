from app.models.user import User

class UserService(object) :
    def __init__(self) -> None:
        pass
    
    def login(self, id , password) :# 여기에서 선언할때는 파라미터 - self, id, password
        user = User(id , password)
        print(f'id : {user.id}')
        print(f'password : {user.password}')        