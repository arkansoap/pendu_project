from fastapi import FastAPI
from fastapi import Query, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
from larousse_api import larousse

app = FastAPI()


class SubmitPayload(BaseModel):
    value: str


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello world !!"}


@app.get("/selectionMot")
async def selection_mot():
    with open("listeMot.txt", encoding="utf-8") as file:
        liste_mot = file.readlines()
    mot = random.choice(liste_mot).strip("\n")
    return {"mot": mot}


@app.get("/definitions/")
async def get_definition(
    mot: str = Query(None, title="definition du mot", min_length=1)
):
    liste_def = larousse.get_definitions(mot)
    return liste_def


@app.put("/submit")
async def receive_form(value: str):
    return {"received_value": value}
