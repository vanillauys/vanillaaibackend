# ---------------------------------------------------------------------------- #
# --- Imports ---------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


from pydantic import BaseModel, Field, EmailStr


# ---------------------------------------------------------------------------- #
# --- Schemas Class ---------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


class Schemas():


    # ------------------------------------------------------------------------ #
    # --- General Schemas ---------------------------------------------------- #
    # ------------------------------------------------------------------------ #


    class DetailClass(BaseModel):
        detail: str = Field(default=None)
    
    Detail: DetailClass = DetailClass

    def detail(self):
        return self.Detail


    # ------------------------------------------------------------------------ #
    # --- User Schemas ------------------------------------------------------- #
    # ------------------------------------------------------------------------ #


    class UserClass(BaseModel):
        key: str = Field(default=None)
        username: str = Field(default=None)
        email: EmailStr = Field(default=None)
        password: str = Field(default=None)
        verified: bool = Field(default=False)
        tokens: int = Field(default=0)
        disabled: bool = Field(default=False)
        newsletter: bool = Field(default=False)
        type: str = Field(default='personal')

    class CreateUserClass(BaseModel):
        username: str = Field(default=None)
        email: EmailStr = Field(default=None)
        password: str = Field(default=None)
    
    class LoginUserClass(BaseModel):
        username: str = Field(default=None)
        password: str = Field(default=None)
    
    class LoginUserSuccessClass(BaseModel):
        username: str = Field(default=None)
        access_token: str = Field(default=None)
        refresh_token: str = Field(default=None)

    User: UserClass = UserClass
    CreateUser: CreateUserClass = CreateUserClass
    LoginUser: LoginUserClass = LoginUserClass
    LoginUserSuccess: LoginUserSuccessClass = LoginUserSuccessClass

    def user(self) -> User:
        return self.User

    def create_user(self) -> CreateUser:
        return self.CreateUser
    
    def login_user(self) -> LoginUser:
        return self.LoginUser
    
    def login_user_success(self) -> LoginUserSuccess:
        return self.LoginUserSuccess
