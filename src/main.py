# ---------------------------------------------------------------------------- #
# --- Imports ---------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from schemas import Schemas
from db.database import Database
from routers import users


# ---------------------------------------------------------------------------- #
# --- App Configuration ------------------------------------------------------ #
# ---------------------------------------------------------------------------- #

load_dotenv()
schemas = Schemas()
db = Database()

TAGS_METADATA = [
    {
        "name": "Testing",
        "description": "Routes to test functionality.",
        "externalDocs": {
            "description": "FastAPI Documentation",
            "url": "https://fastapi.tiangolo.com/",
        }
    },
    {
        "name": "Users",
        "description": "User handling and authentication"
    }
]


# Configure the API with detailed description
app = FastAPI(
    title="Vanillai Backend Documentation",
    description="OpenAI API implementation",
    version="0.0.0",
    terms_of_service="https://vanillai.vercel.app/terms",
    contact={
        "name": "Wihan Uys",
        "url": "https://vanillauys.vercel.app/about",
        "email": "wihan@duck.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://spdx.org/licenses/MIT.html",
    },
    openapi_tags=TAGS_METADATA,
    openapi_url="/openapi.json",
)

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add routers from different files here, to keep things tidy.
app.include_router(users.router)


# ---------------------------------------------------------------------------- #
# --- Basic API Route -------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


@app.get('/', tags=['Testing'],
    response_model=schemas.Detail,
    responses={
        500: {"model": schemas.Detail}
    }
)
def info():
    """
    ### Basic route to test functionality.
    """
    response = {
        'detail': "https://vanillaai.deta.dev/docs"
    }
    return JSONResponse(status_code=200, content=response)


# ---------------------------------------------------------------------------- #
# --- Main ------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


def main():
    load_dotenv()
    # Nothing to do here...


if __name__ == "__main__":
    main()
