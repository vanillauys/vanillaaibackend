# ---------------------------------------------------------------------------- #
# --- Imports ---------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


import os
from dotenv import load_dotenv
from deta import Deta
from auth.auth_manager import Auth
from schemas import Schemas
from typing import Dict, Tuple


# ---------------------------------------------------------------------------- #
# --- Database Class --------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


schema = Schemas()

class Database():


    # ------------------------------------------------------------------------ #
    # --- Database Configuration --------------------------------------------- #
    # ------------------------------------------------------------------------ #


    load_dotenv()
    auth = Auth()
    PROJECT_KEY = os.environ.get('DETA_PROJECT_KEY')
    deta = Deta(PROJECT_KEY)
    users = deta.Base('users')
    history = deta.Base('history')


    # ------------------------------------------------------------------------ #
    # --- User CRUD ---------------------------------------------------------- #
    # ------------------------------------------------------------------------ #


    def create_user(self, user: schema.create_user()) -> Tuple[int, str]:
        # check if username exists
        code, _, _ = self.get_user_by_username(user.username) 
        if code == 200:
            return 409, f"username '{user.username}' already exists in db."
        if code == 500:
            return 500, "an error occured when checking if the username already exists in the db."
        
        # check if email exists
        code, _, _ = self.get_user_by_email(user.email)
        if code == 200:
            return 409, f"email '{user.email}' already exists in db."
        if code == 500:
            return 500, "an error occured when checking if the email already exists in the db."
        
        data = {
            'username': user.username,
            'email': user.email,
            'password': self.auth.hash_password(user.password),
            'verified': False,
            'tokens': 5,
            'disabled': False,
            'newsletter': False,
            'type': 'personal'
        }

        try:
            self.users.put(data)
            return 200, "successfully added user to the db."
        except Exception:
            return 500, "an error occured while adding user to the db."


    def get_user_by_email(self, email: str) -> Tuple[int, str, Dict]:
        try:
            results = self.users.fetch({'email': email})
            user = results.items

            if not user:
                return 404, f"email '{email}' not found in db.", None

            return 200, f"user '{email}' found in db.", user[0]

        except Exception:
            return 500, "a db error occured.", None


    def get_user_by_username(self, username: str) -> Tuple[int, str, Dict]:
        try:
            results = self.users.fetch({'username': username})
            user = results.items

            if not user:
                return 404, f"username '{username}' not found in db.", None

            return 200, f"user '{username}' found in db.", user[0]

        except Exception:
            return 500, "a db error occured.", None
