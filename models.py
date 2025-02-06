from pydantic import EmailStr, field_validator
from sqlmodel import Relationship, SQLModel , Field #Este seria el schema
# El field hace conectar pydantic y sqlmodel
# class ___(BaseModel): #Esto es para validar datos
#     name: str


class Base(SQLModel):
    name: str = Field(default=None)

class BaseSchema( Base, table=True ):
    id: int | None = Field(default=None, primary_key=True)

class User(SQLModel, table=True):
    id: int | None = Field( default=None, primary_key=True)
    email: str = Field(default= None, min_length=5, unique=True)
    name: str | None = Field(default=None, min_length=4)

    wishes: list["Wish"] = Relationship(back_populates="user")

    @field_validator('email')
    def validate_email(cls, email):
        if not EmailStr.validate(email):
            raise ValueError("Invalid email address")    
        return email

class Wish(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    wish: str | None = Field(default=None)
    
    user_id: int | None = Field( default=None, foreign_key="user.id")
    user: User | None = Relationship(back_populates="wishes")