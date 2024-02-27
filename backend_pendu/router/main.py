from fastapi import FastAPI
from fastapi import Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
from larousse_api import larousse
from fucntions.params_difficulty import update_params, get_params
from fucntions.high_score import save_score, get_score
from database.database import get_session
from environs import Env

env = Env()
env.read_env()

app = FastAPI()

from pydantic import BaseModel


class ScoreData(BaseModel):
    value: int
    name: str


# if env == "prod":
#     origins = [
#         "http://pendu.arkansoap.tech",
#     ]
# else:
#     origins = [
#         "http://localhost:8080",
#     ]

origins = [
    "http://penduflex.arkansoap.tech",
    "http://localhost:8081",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello world on the flex !!"}


@app.get("/selectionMot")
async def selection_mot():
    with open("router/listeMot.txt", encoding="utf-8") as file:
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
async def get_diff_value(value: str):
    print(value.strip('"'))
    update_params(db=get_session(), id=2, level=value.strip('"'))
    return {"received_value": value}


@app.get("/params")
async def get_diff_params():
    diff = get_params(db=get_session(), id=2)
    return {"params": diff}


@app.put("/savescore")
async def save_highscore(score_data: ScoreData):
    score = save_score(db=get_session(), pseudo=score_data.name, score=score_data.value)
    return score


@app.get("/highscore")
async def get_highscore():
    score = get_score(db=get_session())
    return score
