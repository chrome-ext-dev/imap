from theApi import getEmail, randomUser
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {'Welcome To': 'Email Reader API'}

@app.get("/fakename/{gender}")
def read_root(gender: str, request: Request):
    theGender = str(gender)
    user = randomUser(theGender)
    return user

@app.post("/pinterest")
async def get_body(request: Request):
    email = await request.json()
    return getEmail(email)
