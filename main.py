from fastapi import FastAPI
from db import models
from db.database import engine
from routers.users import router as users_router



models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='My App: BBank')


app.include_router(users_router)

@app.get('/', tags=['BBank'])
def hello() -> str:
    return """Hello, it is my App: BBank"""

