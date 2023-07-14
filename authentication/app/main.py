import json
from decimal import Decimal
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


class Coordinates(BaseModel):
    longitude: float
    latitude: float


@app.get("/")
def read_root():
    return {"Welcome": "Authentication Service"}
