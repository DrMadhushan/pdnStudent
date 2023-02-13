# main.py

from fastapi import Depends, FastAPI, status, Form, HTTPException
from fastapi.security import OAuth2PasswordBearer

import services.database as db
import services.auth as auth
from router import user, student
from router.public import public

app = FastAPI()
app.include_router(user.router)
app.include_router(student.router)
app.include_router(public.router)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/")
async def root(token: str = Depends(oauth2_scheme)):
    user_details = await auth.getCurrentUser(token)
    return user_details


@app.get("/controls/admin/profile_updates")
async def getAllProfileUpdateRequests():
    return await db.getAllProfileUpdateRequests()
