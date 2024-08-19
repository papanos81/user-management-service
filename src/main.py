from fastapi import FastAPI
from .controllers.user import router as user_router


app = FastAPI()
app.include_router(user_router)

