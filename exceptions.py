from fastapi import HTTPException

class UserAlreadyExistException(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, message='User already exist')
        


