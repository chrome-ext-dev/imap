from theApi import getEmail
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

@app.post("/pinterest")
async def get_body(request: Request):
    email = await request.json()
    return getEmail(email)