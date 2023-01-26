# ---------------------------------------------------------------------------- #
# --- Imports ---------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


from fastapi import APIRouter, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.responses import JSONResponse
from auth.auth_manager import Auth
from db.database import Database
from schemas import Schemas


# ---------------------------------------------------------------------------- #
# --- Route Configuration ---------------------------------------------------- #
# ---------------------------------------------------------------------------- #


router = APIRouter()
security = HTTPBearer()
auth = Auth()
db = Database()
schemas = Schemas()


# ---------------------------------------------------------------------------- #
# --- App Routes : User and authentication ----------------------------------- #
# ---------------------------------------------------------------------------- #


@router.post('/users/register', tags=['Users'],
    response_model=schemas.detail(),
    responses = {
        409: {"model": schemas.detail()},
        500: {"model": schemas.detail()}
    }
)
def register(user: schemas.create_user()):
    code, response = db.create_user(user)
    return JSONResponse(status_code=code, content={'detail': response})
