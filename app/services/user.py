from app.models.user import User

class UserService(object) : 
    def __init__(self) -> None :                                                       
        pass
    
    def user_input(self, id, password) : # 여기에서 선언할때는 파라미터 - self, id, password
        user_input = User(id, password)
        print(f'입력한 id: {user_input.id}')
        print(f'입력한 password: {user_input.password}')
        